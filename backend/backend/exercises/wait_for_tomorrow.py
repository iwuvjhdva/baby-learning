from backend.exercises.base import BaseExercise


class WaitForTomorrow(BaseExercise):
    def perform(self):
        bits = [{
            'type': 'wait_for_tomorrow',
        }]
        return bits
