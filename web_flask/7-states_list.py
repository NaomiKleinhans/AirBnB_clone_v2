from flask import Flask, render_template
from models import storage
from models.state import State

# Create an instance of the Flask class
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Handle requests to the /states_list route.

    Retrieves a sorted list of State objects from the storage and renders
    them using the '7-states_list.html' template.

    Returns:
        str: Rendered HTML template containing the list of states.
    """
    # Retrieve all State objects from storage and sort them by name
    states = sorted(storage.all(State).values(), key=lambda state: state.name)

    # Render the '7-states_list.html' template with the sorted list of states
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage connection after each request.

    Args:
        exception (Exception or None): Exception raised during request handling, if any.
    """
    storage.close()


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
