#!/usr/bin/python3
"""
This module starts a simple Flask web application.

The application listens on 0.0.0.0:5000 and has a single route:
- '/' which returns the message "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Return the message 'Hello HBNB!' when accessing the root route.

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """
    Run the Flask application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
