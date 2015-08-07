from backend.exercises.base import BaseExercise


class TakeABreak(BaseExercise):
    def __init__(self, minutes):
        self._minutes = minutes

    def get_bits(self):
        bits = [{
            'type': 'take_a_break',
            'minutes_left': self._minutes
        }]
        return bits
