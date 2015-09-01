from functools import wraps
from datetime import datetime, timedelta

import cherrypy

from backend.db import db


class ExerciseException(Exception):
    pass


class TakeABreakException(ExerciseException):
    def __init__(self, time_passed):
        self.time_passed = time_passed


class WaitForTomorrowException(ExerciseException):
    pass


def no_debug_only(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if not cherrypy.config['general']['debug']:
            return f(*args, **kwds)
    return wrapper


class BaseExercise:
    def __init__(self):
        self._last_exercised = cherrypy.request.profile['last_exercised']

    def perform(self):
        self._verify_no_break_needed()

    @no_debug_only
    def _verify_no_break_needed(self):
        if self._last_exercised is not None:
            now = datetime.now()

            time_passed = datetime.now() - self._last_exercised

            if time_passed < timedelta(minutes=30):
                raise TakeABreakException(time_passed)

            if now.date() > self._last_exercised.date():
                self._profile['state']['carried_over'] = True

    @no_debug_only
    def _verify_day_passed(self):
        now = datetime.now()
        carried_over = self._profile['state'].get('carried_over', False)
        if self._last_exercised and not carried_over and (
                self._last_exercised.date() >= now.date() or now.hour < 6):
            raise WaitForTomorrowException
        self._profile['state']['carried_over'] = False

    def _save_state(self, state):
        db.client.profiles.update(
            {
                'user': 'linoy'
            },
            {
                '$set': {
                    'courses.{}.state'.format(self.bit_type): state,
                    'last_exercised': datetime.now()
                }
            })
