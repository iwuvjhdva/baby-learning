from datetime import datetime, timedelta

import cherrypy

from backend.db import db
from backend.exercises.math import Math


class Exercises:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def next(self):
        profile = db.profiles.find_one({
            'user': 'linoy'
        })

        time_passed = datetime.now() - profile['last_exercised']

        bits = None

        if time_passed < timedelta(minutes=20):
            bits = [{
                'type': 'take_a_rest',
                'minutes_left': time_passed.minutes
            }]
        elif profile['state'] is None:
            bits = Math('quantity', range(1, 6), shuffle=False)

        return {
            'bits': bits
        }
