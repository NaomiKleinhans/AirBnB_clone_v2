#!/usr/bin/python3
"""
This script starts a Flask web application with the following routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB"
- /c/<text>: displays "C " followed by the value of the text variable
- /python/(<text>): displays "Python " followed by the value of the
text variable
- /number/<n>: displays "n is a number" only if n is an integer
- /number_template/<n>: displays an HTML page only if n is an integer,
  with an H1 tag that says "Number: n" inside the BODY tag.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays 'C ' followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable.
    The default value of text is 'is cool'. Underscores in the text
    variable are replaced with spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if n is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer, with an H1 tag
    that says 'Number: n' inside the BODY tag.
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
