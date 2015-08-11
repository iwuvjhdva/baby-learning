import random

import cherrypy

from backend.exercises.base import BaseExercise

# TODO: dots intersection
# TODO: dots overflow
# TODO: different exercises support on client

# TODO: status save
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
    subtraction = 'subtraction'
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
            number_offset = state['days_counter'] * 2
            bits_range = range(3 + number_offset, 13 + number_offset)

            bits = self._perform_two_shuffled_sets(bits_range, state)

            if state['days_counter'] >= 5:
                state = dict(name=MathStates.addition, counter=0)
        elif state_name == MathStates.addition:
            if state['counter'] % 3 == 1:
                number_offset = state['days_counter'] * 2
                bits_range = range(13 + number_offset, 23 + number_offset)
                bits = self._perform_two_shuffled_sets(bits_range, state)
            else:
                case_result = random.randint(2, 23 + state['days_counter'] * 2)
                first_member = random.randint(1, case_result)
                second_member = case_result - first_member
                label = lambda tpl: tpl.format(first_member,
                                               second_member,
                                               case_result)
                bits = [
                    {
                        'type': 'math',
                        'kind': 'case',
                        'label': label("_{}_ + {} = {}")
                    },
                    {
                        'type': 'math',
                        'kind': 'case',
                        'label': label("{} + _{}_ = {}")
                    },
                    {
                        'type': 'math',
                        'kind': 'case',
                        'label': label("{} + {} = _{}_")
                    },
                ]

            if state['counter'] >= 9:
                state['days_counter'] += 1
        else:
            bits = None

        self._update_state(state)

        return bits

    def _perform_two_shuffled_sets(self, bits_range, state):
        if state['counter'] == 0:
            self._verify_day_passed()

            # Saving two sets from 1-10
            two_sets = list(bits_range)
            random.shuffle(two_sets)
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
