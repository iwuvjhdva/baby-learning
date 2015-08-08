from datetime import datetime, timedelta

import cherrypy

from backend.db import db
from backend.exercises.take_a_break import TakeABreak
from backend.exercises.math import Math


class Exercises:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def next(self):
        profile = db.client.profiles.find_one({
            'user': 'linoy'
        })

        bits = None
        time_passed = None

        if profile['last_exercised'] is not None:
            time_passed = datetime.now() - profile['last_exercised']

        # if time_passed is not None and time_passed < timedelta(minutes=30):
        #     minutes_left = 30 - time_passed.seconds / 60.
        #     bits = TakeABreak(minutes=minutes_left).perform()
        # else:
        exercise = Math(profile['courses']['math'])
        bits = exercise.perform()

        return {
            'bits': bits
        }
