#!/usr/bin/python3
"""
This module starts a Flask web application with three routes.

The application listens on 0.0.0.0:5000 and has the following routes:
- '/' which returns the message "Hello HBNB!"
- '/hbnb' which returns the message "HBNB"
- '/c/<text>' which returns the string "C " followed by the value of `<text>`,
  with underscores replaced by spaces.

This module demonstrates basic Flask route handling dynamic URL parameters.
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
        text (str): The text displayed after "C ". Underscores in the text
                    are replaced by spaces.

    Returns:
        str: The string "C " followed by the value of <text> with underscores
             replaced by spaces.
    """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    """
    Run the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
