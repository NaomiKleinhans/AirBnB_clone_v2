#!/usr/bin/python3
"""
This script starts a Flask web application with several routes that
display different text or render HTML templates based on the URL.
The web application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' at the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' at the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Displays 'C ' followed by the value of the text variable at
    the /c/<text> route.
    Underscores in the text variable are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Displays 'Python ' followed by the value of the text variable
    at the /python/(<text>) route.
    The default value of text is 'is cool'. Underscores in the
    text variable are replaced with spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'n is a number' at the /number/<n> route, but only
    if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with an H1 tag saying 'Number: n'
    at the /number_template/<n> route.
    The HTML page is rendered only if n is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page at the /number_odd_or_even/<n> route,
    showing whether
    the number n is odd or even. The page contains an H1 tag with
    'Number: n is odd/even'.
    """

    status = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', number=n, status=status)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
