from datetime import datetime

from backend.db import db


class ExerciseException(Exception):
    pass


class TakeABreakException(ExerciseException):
    pass


class WaitForTomorrowException(ExerciseException):
    pass


class BaseExercise:
    def perform(self):
        raise NotImplemented

    def _update_state(self, state):
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
