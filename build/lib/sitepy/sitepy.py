import os
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
import inspect

class SitePy:
    def __init__(self, static_dir='static'):
        self.routes = {}
        self.middleware = [self.logger_middleware]
        self.static_dir = static_dir

    def route(self, path, methods=['GET']):
        def wrapper(handler):
            self.routes[(path, tuple(methods))] = handler
            return handler
        return wrapper

    def use(self, middleware):
        self.middleware.append(middleware)

    def logger_middleware(self, environ):
        print(f"Request received for {environ['PATH_INFO']}")

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        for middleware in self.middleware:
            middleware(environ)
        handler = None
        for route, methods in self.routes.keys():
            if path == route and method in methods:
                handler = self.routes[(route, methods)]
                break
        if handler:
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            except ValueError:
                request_body_size = 0
            request_body = environ['wsgi.input'].read(request_body_size)
            params = parse_qs(request_body) if request_body else {}
            handler_args = inspect.signature(handler).parameters
            response_body = handler(params) if handler_args else handler()
            status = '200 OK'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return [response_body.encode()]
        elif path.startswith('/' + self.static_dir):
            try:
                with open(path[1:], 'rb') as f:
                    response_body = f.read()
                status = '200 OK'
                headers = [('Content-type', 'application/octet-stream')]
                start_response(status, headers)
                return [response_body]
            except FileNotFoundError:
                status = '404 NOT FOUND'
                headers = [('Content-type', 'text/plain')]
                start_response(status, headers)
                return ['File not found'.encode()]
        else:
            status = '404 NOT FOUND'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            return ['Route not found'.encode()]

    def run(self, host='localhost', port=8080):
        try:
            server = make_server(host, port, self)
            print(f'Serving on {host}:{port}')
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nServer shutting down...')
            server.server_close()
