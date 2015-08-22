from backend.exercises.base import BaseExercise


class WaitForTomorrow(BaseExercise):
    def perform(self):
        exercise = {
            'type': 'wait_for_tomorrow',
        }
        return exercise
