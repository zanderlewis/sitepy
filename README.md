# sitepy

A simple web framework for Python.

![Alt](https://repobeats.axiom.co/api/embed/951ba2337639530ee37774d8f84233efcc45eb02.svg "Repobeats analytics image")

## Installation

You can install sitepy with pip:

```sh
pip install sitepy
```

## Usage

Here's a basic example of a sitepy application:

```python
from sitepy import SitePy

app = SitePy()

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
```

Render Templates:

```python
from sitepy import SitePy

app = SitePy()

@app.route("/", methods=['GET', 'POST'])
def index():
    someVar = "Hello, World!"
    return app.render_template("index.html", someVar)

if __name__ == "__main__":
    app.run()
```

This will start a server on localhost:8080 and respond with "Hello, world!" to GET and POST requests at the root URL.

## Features

- Simple routing: Use decorators to define routes.

- Middleware support: Use app.use to add middleware functions.

- Static file serving: Files in the static directory are served at /static.

- Template serving: Files in the templates/ directory will act as a template.

- Built in features for checking profanity, using Postgres, Mysql, and SQLite, using the openai library, and more.

## Built-Ins

To learn how to use the built-in features, check out the [examples.](examples/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache](sitepy/LICENSE)
