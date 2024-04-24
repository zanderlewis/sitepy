import os
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server
import inspect
from jinja2 import Environment, FileSystemLoader

fof = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @import 'https://fonts.googleapis.com/css?family=Inconsolata';

        html {
            min-height: 100%;
        }

        body {
            box-sizing: border-box;
            height: 100%;
            background-color: #000000;
            background-image: radial-gradient(#11581E, #041607), url("https://media.giphy.com/media/oEI9uBYSzLpBK/giphy.gif");
            background-repeat: no-repeat;
            background-size: cover;
            font-family: 'Inconsolata', Helvetica, sans-serif;
            font-size: 1.5rem;
            color: rgba(128, 255, 128, 0.8);
            text-shadow:
                0 0 1ex rgba(51, 255, 51, 1),
                0 0 2px rgba(255, 255, 255, 0.8);
        }

        .noise {
            pointer-events: none;
            position: absolute;
            width: 100%;
            height: 100%;
            background-image: url("https://media.giphy.com/media/oEI9uBYSzLpBK/giphy.gif");
            background-repeat: no-repeat;
            background-size: cover;
            z-index: -1;
            opacity: .02;
        }

        .overlay {
            pointer-events: none;
            position: absolute;
            width: 100%;
            height: 100%;
            background:
                repeating-linear-gradient(180deg,
                    rgba(0, 0, 0, 0) 0,
                    rgba(0, 0, 0, 0.3) 50%,
                    rgba(0, 0, 0, 0) 100%);
            background-size: auto 4px;
            z-index: 1;
        }

        .overlay::before {
            content: "";
            pointer-events: none;
            position: absolute;
            display: block;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            width: 100%;
            height: 100%;
            background-image: linear-gradient(0deg,
                    transparent 0%,
                    rgba(32, 128, 32, 0.2) 2%,
                    rgba(32, 128, 32, 0.8) 3%,
                    rgba(32, 128, 32, 0.2) 3%,
                    transparent 100%);
            background-repeat: no-repeat;
            animation: scan 7.5s linear 0s infinite;
        }

        @keyframes scan {
            0% {
                background-position: 0 -100vh;
            }

            35%,
            100% {
                background-position: 0 100vh;
            }
        }

        .terminal {
            box-sizing: inherit;
            position: absolute;
            height: 100%;
            width: 1000px;
            max-width: 100%;
            padding: 4rem;
            text-transform: uppercase;
        }

        .output {
            color: rgba(128, 255, 128, 0.8);
            text-shadow:
                0 0 1px rgba(51, 255, 51, 0.4),
                0 0 2px rgba(255, 255, 255, 0.8);
        }

        .output::before {
            content: "> ";
        }

        a {
            color: #fff;
            text-decoration: none;
        }

        a::before {
            content: "[";
        }

        a::after {
            content: "]";
        }

        .errorcode {
            color: white;
        }
    </style>
</head>

<body>
    <div class="noise"></div>
    <div class="overlay"></div>
    <div class="terminal">
        <h1>Error <span class="errorcode">404</span></h1>
        <p class="output">The page you are looking for might have been removed, had its name changed or is temporarily
            unavailable.</p>
        <p class="output">Please <a href="/">return to the homepage</a>.</p>
        <p class="output">Good luck.</p>
        <p class="output">Credits to <a href='https://codepen.io/code2rithik' target="_blank">Rithik Samanthula (@code2rithik)!</a></p>
    </div>
</body>

</html>
"""

f00 = """
<!DOCTYPE html>
<html lang="en">
<head>
<style>
*,
*::after,
*::before {
	box-sizing: border-box;
}

html,
body {
	align-items: center;
	background: linear-gradient(#003eff, #0028a9);
	color: white;
	display: flex;
	font: 2rem "Poiret One";
	height: 100vh;
	justify-content: center;
	margin: 0;
	padding: 0;
}

.box {
	height: 100px;
	margin: 0 10px;
	overflow: hidden;
	position: relative;
	transform: rotateZ(270deg) scale(1.05);
	width: 100px;
}

.box:nth-of-type(2) {
	left: -28px;
	transform: rotateX(-180deg) rotateY(180deg) rotateZ(270deg) scale(1.05);
}

.box span {
	animation: loader 4.8s infinite both;
	display: block;
	height: 100%;
	position: absolute;
	width: 100%;
}

.box span:nth-child(1) {
	animation-delay: 0.2s;
}

.box span:nth-child(2) {
	animation-delay: 0.4s;
}

.box span:nth-child(3) {
	animation-delay: 0.6s;
}

.box span:nth-child(4) {
	animation-delay: 0.8s;
}

.box span:nth-child(5) {
	animation-delay: 1s;
}

.box span:nth-child(6) {
	animation-delay: 1.2s;
}

.box span::after {
	background: #fff;
	border-radius: 50%;
	content: "";
	left: 50%;
	padding: 6px;
	position: absolute;
	top: 0;
	transform: translateX(-50%);
}

@keyframes loader {
	0% {
		opacity: 0;
		transform: rotate(180deg);
		animation-timing-function: ease-out;
	}
	5% {
		opacity: 1;
		transform: rotate(300deg);
		animation-timing-function: linear;
	}
	30% {
		transform: rotate(420deg);
		animation-timing-function: ease-in-out;
	}
	35% {
		transform: rotate(625deg);
		animation-timing-function: linear;
	}
	70% {
		transform: rotate(800deg);
		animation-timing-function: ease-out;
		opacity: 1;
	}
	75% {
		opacity: 0;
		transform: rotate(900deg);
		animation-timing-function: ease-out;
	}
	76% {
		opacity: 0;
		transform: rotate(900deg);
	}
	100% {
		opacity: 0;
		transform: rotate(900deg);
	}
}

h1 {
	text-shadow: 0 0 10px #fff;
	animation: blink 4.8s infinite both;
}

h1:nth-of-type(2) {
	animation: none;
	letter-spacing: -14px;
	margin: 0 auto;
	opacity: 0.1;
	padding-left: 41px;
	position: absolute;
	top: 50%;
	transform: translatey(-50%);
}

@keyframes blink {
	0%,
	50%,
	100% {
		opacity: 0.2;
	}
	25%,
	75% {
		opacity: 1;
	}
}

h5,
p {
	position: absolute;
	font-family: monospace;
}

h5 {
	top: 10%;
	font-size: 0.4em;
	
}

p {
	font-size: 0.3em;
	bottom: 10%;
	width: 50%;
	text-align: center;
}

p a {
	color: cyan;
}

</style>
</head>
<body>
<h5>Internal Server error !</h5>
    <h1>5</h1>
    <h1>00</h1>
    <div class="box">
			<span></span><span></span>
			<span></span><span></span>
			<span></span>
		</div>
    <div class="box">
			<span></span><span></span>
			<span></span><span></span>
			<span></span>
		</div>
    <p> We're unable to find out what's happening! We suggest you to
			<br/>
			<a href="/">Go Home</a>
			or visit here later. Credits to <a href='https://codepen.io/adsingh14' target="_blank">AMAN (@adsingh14)!</a></p>
</body>
</html>
"""


class SitePy:
    def __init__(
        self, static_dir="static", templates_dir="templates", custom_404_page=None, custom_500_page=None
    ):
        self.routes = {}
        self.middleware = [self.logger_middleware]
        self.static_dir = static_dir
        self.templates_dir = templates_dir
        self.custom_404_page = custom_404_page
        self.custom_500_page = custom_500_page

    def render_template(self, template_name, **context):
        env = Environment(loader=FileSystemLoader(self.templates_dir))
        template = env.get_template(template_name)
        return template.render(**context)

    def route(self, path, methods=["GET"]):
        def wrapper(handler):
            self.routes[(path, tuple(methods))] = handler
            return handler

        return wrapper

    def use(self, middleware):
        self.middleware.append(middleware)

    def logger_middleware(self, environ):
        print(f"Request received for {environ['PATH_INFO']}")

    def __call__(self, environ, start_response):
        try:
            path = environ["PATH_INFO"]
            method = environ["REQUEST_METHOD"]
            for middleware in self.middleware:
                middleware(environ)
            handler = None
            for route, methods in self.routes.keys():
                if route == path and method in methods:
                    handler = self.routes[(route, methods)]
                    break
            if handler:
                try:
                    request_body_size = int(environ.get("CONTENT_LENGTH", 0))
                except ValueError:
                    request_body_size = 0
                request_body = environ["wsgi.input"].read(request_body_size)
                body_params = parse_qs(request_body.decode()) if request_body else {}
                params = parse_qs(request_body.decode()) if request_body else {}
                params.update(body_params)
                handler_args = inspect.signature(handler).parameters
                response_body = handler(params) if handler_args else handler()
                status = "200 OK"
                headers = [("Content-type", "text/html")]
                start_response(status, headers)
                return [response_body.encode()]
            elif path.startswith("/" + self.static_dir):
                try:
                    with open(path[1:], "rb") as f:
                        response_body = f.read()
                    status = "200 OK"
                    headers = [("Content-type", "application/octet-stream")]
                    start_response(status, headers)
                    return [response_body]
                except FileNotFoundError:
                    status = "404 NOT FOUND"
                    headers = [("Content-type", "text/html")]
                    start_response(status, headers)
                    return [
                        (
                            self.custom_404_page.encode()
                            if self.custom_404_page
                            else fof.encode()
                        )
                    ]
            else:
                status = "404 NOT FOUND"
                headers = [("Content-type", "text/html")]
                start_response(status, headers)
                return [
                    (
                        self.custom_404_page.encode()
                        if self.custom_404_page
                        else fof.encode()
                    )
                ]
        except KeyboardInterrupt:
            print("\nServer shutting down...")
        except Exception as e:
            status = "500 INTERNAL SERVER ERROR"
            headers = [("Content-type", "text/html")]
            start_response(status, headers)
            print(e)
            return [
                (
                    self.custom_500_page.encode()
                    if self.custom_500_page
                    else f00.encode()
                )
            ]
    
    def tojson(self, data):
        import json
        return json.dumps(data)

    def run(self, host="localhost", port=8080):
        try:
            server = make_server(host, port, self)
            print(f"Serving on {host}:{port}")
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            server.server_close()
