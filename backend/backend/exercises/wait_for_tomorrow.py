from backend.exercises.base import BaseExercise


class WaitForTomorrow(BaseExercise):
    def perform(self):
        exercise = {
            'type': 'message',
            'bits': [{
                'message': "Wait for tomorrow"
            }]
        }
        return exercise
