#!/usr/bin/python3
"""
scripts to starts a Flask
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display an HTML page with filters for the HBNB web app."""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=sorted(states, key=lambda s: s.name),
                           cities=sorted(cities, key=lambda c: c.name),
                           amenities=sorted(amenities, key=lambda a: a.name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
