from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    if id:
        state = next((state for state in states if state.id == id), None)
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
