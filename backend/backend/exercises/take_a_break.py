from backend.exercises.base import BaseExercise


class TakeABreak(BaseExercise):
    def __init__(self, time_passed):
        self._time_passed = time_passed

    def perform(self):
        bits = [{
            'type': 'take_a_break',
            'minutes_left': 30 - int(self._time_passed.seconds / 60)
        }]
        return bits
