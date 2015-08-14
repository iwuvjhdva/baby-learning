import random

import cherrypy

from backend.exercises.base import BaseExercise


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
            bits = self._get_two_shuffled_sets_bits(range(1, 11), state)
            self._iterate_days_counter(state, 6)
            if state['days_counter'] >= 5:
                state = dict(
                    name=MathStates.quantity_11_20,
                    counter=0,
                    days_counter=0,
                    loop_days_counter=0
                )
        elif state_name == MathStates.quantity_11_20:
            bits = self._get_main_quantity_loop_bits(state)
            self._iterate_days_counter(state, 6)

            if state['days_counter'] >= 5:
                state = dict(
                    name=MathStates.addition,
                    counter=0,
                    days_counter=0,
                    loop_days_counter=state['loop_days_counter']
                )
        elif state_name == MathStates.addition:
            def _members():
                case_result = self._get_sample_case_member(state)
                first = random.randint(1, case_result - 1)
                return (first, case_result - first, case_result)

            bits = self._process_equation_state(state, '+', _members,
                                                MathStates.subtraction)
        elif state_name == MathStates.subtraction:
            def _members():
                # TODO: fix zero
                max_num = self._get_max_learned_number(state)
                first = random.randint(2, max_num - 1)
                second = random.randint(max_num - first)
                return (first, second, first - second)

            bits = self._process_equation_state(state, '-', _members,
                                                MathStates.multiplication)
        elif state_name == MathStates.multiplication:
            def _members():
                approx_result = self._get_sample_case_member(state)
                first = random.randint(1, approx_result)
                second = int(approx_result / first)
                return (first, second, first * second)

            bits = self._process_equation_state(state, '*', _members,
                                                MathStates.division)
        elif state_name == MathStates.division:
            def _members():
                first = self._get_sample_case_member(state)
                second = random.randint(1, first + 1)
                return (first, second, int(first / second))

            bits = self._process_equation_state(state, '*', _members,
                                                MathStates.complex_equality_3)
        else:
            bits = None

        self._update_state(state)

        return bits

    def _get_equation_bits(self, members_func, op):
        bits = []

        for case in range(3):
            first, second, result = members_func()
            label = lambda tpl: tpl.format(first, op, second, result)

            bits += [
                {
                    'type': 'math',
                    'kind': 'quantity',
                    'quantity': first,
                    'label': label("_{}_ {} {} = {}")
                },
                {
                    'type': 'math',
                    'kind': 'quantity',
                    'quantity': second,
                    'label': label("{} {} _{}_ = {}")
                },
                {
                    'type': 'math',
                    'kind': 'quantity',
                    'quantity': result,
                    'label': label("{} {} {} = _{}_")
                },
            ]

        return bits

    def _process_equation_state(self, state, op, members_func, next_state):
        if state['counter'] % 3 == 1:
            bits = self._get_equation_bits(members_func, op)
            state['counter'] += 1
        else:
            bits = self._get_main_quantity_loop_bits(state)

        self._iterate_days_counter(state, 9)

        if state['days_counter'] >= 14:
            state = dict(
                name=next_state,
                counter=0,
                days_counter=0,
                loop_days_counter=state['loop_days_counter']
            )

        return bits

    def _get_two_shuffled_sets_bits(self, bits_range, state):
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

        return bits

    def _get_main_quantity_loop_bits(self, state):
        number_offset = state['loop_days_counter'] * 2
        bits_range = range(3 + number_offset, 13 + number_offset)
        return self._get_two_shuffled_sets_bits(bits_range, state)

    def _get_sample_case_member(self, state):
        max_learned_number = self._get_max_learned_number(state)
        case_result = random.randint(2, max_learned_number)
        return case_result

    def _get_max_learned_number(self, state):
        return 3 + state['loop_days_counter'] * 2

    def _iterate_days_counter(self, state, exercises_per_day_num):
        if state['counter'] >= exercises_per_day_num:
            state['counter'] = 0
            state['days_counter'] += 1
            if 'loop_days_counter' in state:
                state['loop_days_counter'] += 1

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
