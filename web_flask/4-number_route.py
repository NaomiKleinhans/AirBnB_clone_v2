#!/usr/bin/python3
"""
This module starts a Flask web application with multiple routes.

The application listens on 0.0.0.0:5000 and has the following routes:
- '/' which returns the message "Hello HBNB!"
- '/hbnb' which returns the message "HBNB"
- '/c/<text>' which returns the string "C " followed by the value of <text>,
  with underscores replaced by spaces.
- '/python/(<text>)' which returns the string "Python " followed by the value
  of <text>, with underscores replaced by spaces. If no <text> is provided,
  it defaults to "is cool".
- '/number/<int:n>' which returns a string confirming that <n> is a number.

This module demonstrates basic Flask route handling with dynamic URL parameters,
default parameter values, and type-specific routing.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Handle the root route '/'.

    Returns:
        str: A simple greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handle the route '/hbnb'.

    Returns:
        str: A simple greeting message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Handle the route '/c/<text>' where <text> is a dynamic URL parameter.

    Args:
        text (str): The text to be displayed after "C ". Underscores in the text
                    are replaced by spaces.

    Returns:
        str: The string "C " followed by the value of <text> with underscores
             replaced by spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Handle the route '/python/' or '/python/<text>' where <text> is an optional
    dynamic URL parameter.

    Args:
        text (str): The text to be displayed after "Python ". Underscores in the
                    text are replaced by spaces. Defaults to "is cool" if not
                    provided.

    Returns:
        str: The string "Python " followed by the value of <text> with
             underscores replaced by spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Handle the route '/number/<int:n>' where <n> is a dynamic URL parameter.

    Args:
        n (int): The number to be confirmed.

    Returns:
        str: The string "<n> is a number", confirming that <n> is a valid number.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    """
    Run the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
