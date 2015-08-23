from backend.exercises.base import BaseExercise


class TakeABreak(BaseExercise):
    def __init__(self, time_passed):
        self._time_passed = time_passed

    def perform(self):
        minutes_left = 30 - int(self._time_passed.seconds / 60)
        exercise = {
            'type': 'message',
            'bits': [{
                'message': "Take a break",
                'comment': "Just {} minutes left".format(minutes_left)
            }]
        }
        return exercise
