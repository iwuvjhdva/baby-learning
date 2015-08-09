import random

import cherrypy

from backend.exercises.base import BaseExercise

# TODO: daily limit
# TODO: tests
# TODO: quanitities 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10000


class MathStates:
    none = None
    quantity_1_5 = '1-5'
    quantity_1_10 = '1-10'
    quantity_1_20 = '1-20'
    addition = 'addition'
    multiplication = 'multiplication'
    zero = 'zero'
    division = 'division'
    complex_equality_3 = 'complex-equations-3'
    complex_equality_4 = 'complex-equations-4'
    sequences = 'sequences'
    less_or_greater = 'less-or-greater'
    inequality = 'inequality '
    fractions = 'fractions'
    equations = 'equations'
    numbers = 'numbers'


class Math(BaseExercise):
    bit_type = 'math'

    def __init__(self):
        self._profile = cherrypy.request.profile['courses']['math']
        self._next_state = self._profile['state']

    def perform(self):
        super().perform()

        state = self._profile['state'].copy()
        state_name = self._profile['state']['name']

        if state_name == MathStates.none:
            bits = self._create_quantity_bits(range(1, 6), shuffle=False)
            state = dict(name=MathStates.quantity_1_5, counter=0)
        elif state_name == MathStates.quantity_1_5:
            bits = self._create_quantity_bits(range(1, 6))
            state['counter'] += 1

            if state['counter'] >= 2:
                state = dict(name=MathStates.quantity_1_10, counter=0)
            else:
                state['name'] = MathStates.quantity_1_5
        elif state_name == MathStates.quantity_1_10:
            if state['counter'] == 0:
                self._verify_day_passed()
                bits = self._create_quantity_bits(range(6, 11), shuffle=False)
            else:
                bits = self._create_quantity_bits(range(6, 11))
            state = dict(name=MathStates.quantity_1_10, counter=1)
        else:
            bits = None

        self._update_state(state)

        return bits

    def _create_quantity_bits(self, quantities, shuffle=True):
        bits = [{
            'type': 'math',
            'kind': 'quantity',
            'quantity': quantity,
            'label': str(quantity)
        } for quantity in quantities]

        if shuffle:
            random.shuffle(bits)

        return bits
