from datetime import datetime, timedelta

import cherrypy

from backend.db import db
from backend.exercises.take_a_break import TakeABreak
from backend.exercises.math import Math


class Exercises:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def next(self):
        profile = db.profiles.find_one({
            'user': 'linoy'
        })

        bits = None

        time_passed = datetime.now() - profile['last_exercised']

        if time_passed < timedelta(minutes=20):
            bits = TakeABreak(minutes=time_passed.minutes).get_bits()
        else:
            exercise = Math(profile['courses']['math'])
            bits = exercise.get_bits()

        return {
            'bits': bits
        }
