#!/usr/bin/python3
"""
This module starts a basic Flask web application with two routes.

The application listens on 0.0.0.0:5000 and has the following routes:
- '/' which returns the message "Hello HBNB!"
- '/hbnb' which returns the message "HBNB"

This module demonstrates a simple Flask setup with multiple routes.
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


if __name__ == "__main__":
    """
    Run the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
