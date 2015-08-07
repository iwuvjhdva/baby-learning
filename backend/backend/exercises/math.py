from backend.exercises.base import BaseExercise


class Math(BaseExercise):
    def __init__(self, math_profile):
        self.profile = math_profile

    def get_bits(self):
        if self.profile['state'] is None:
            pass

    def get_state(self):
        pass
