import random

import cherrypy

from backend.exercises.base import BaseExercise

# TODO: red screen last bit
# TODO: dots intersection
# TODO: dots overflow
# TODO: different exercises support on client

# TODO: tests
# TODO: quanitities 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10000
# TODO: at least equality
# TODO: deploy on AWS
# TODO: unit tests


class MathStates:
    none = None
    quantity_1_5 = '1-5'
    quantity_1_10 = '1-10'
    quantity_1_10_shuffle = '1-10-shuffle'
    quantity_11_20 = '11-20'
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
        elif state_name == MathStates.quantity_1_10:
            if state['counter'] == 0:
                self._verify_day_passed()
                bits = self._create_quantity_bits(range(6, 11), shuffle=False)
            else:
                if state['counter'] % 2:
                    bits_range = range(1, 6)
                else:
                    bits_range = range(6, 11)
                bits = self._create_quantity_bits(bits_range)

            state['counter'] += 1
            if state['counter'] >= 6:
                state = dict(
                    name=MathStates.quantity_1_10_shuffle,
                    counter=0,
                    days_counter=0
                )
        elif state_name == MathStates.quantity_1_10_shuffle:
            bits = self._perform_two_shuffled_sets(range(1, 11), state)
            if state['days_counter'] >= 5:
                state = dict(
                    name=MathStates.quantity_11_20,
                    counter=0,
                    days_counter=0
                )
        elif state_name == MathStates.quantity_11_20:
            bits_range = range(2 + state['days_counter'],
                               12 + state['days_counter'])

            bits = self._perform_two_shuffled_sets(bits_range, state)

            if state['days_counter'] >= 10:
                state = dict(name=MathStates.addition, counter=0)
        else:
            bits = None

        self._update_state(state)

        return bits

    def _perform_two_shuffled_sets(self, bits_range, state):
        if state['counter'] == 0:
            self._verify_day_passed()

            # Saving two sets from 1-10
            two_sets = random.shuffle(bits_range)
            state['set1'] = two_sets[:5]
            state['set2'] = two_sets[5:]

        if state['counter'] % 2:
            bits_range = state['set1']
        else:
            bits_range = state['set2']

        bits = self._create_quantity_bits(bits_range)

        state['counter'] += 1

        if state['counter'] >= 6:
            state['counter'] = 0
            state['days_counter'] += 1

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
