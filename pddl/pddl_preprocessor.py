#
#  pddl_preprocessor.py
#  pddl
#
#  Created by Felipe Meneguzzi on 2021-04-20.
#  Copyright 2021 Felipe Meneguzzi. All rights reserved.
#
from typing import Set, Any

from pddl.state import apply, applicable, regress, regressable


class PDDLPreprocessor:
    """A class to preprocess PDDL domains"""

    def __init__(self):
        pass

    def preprocess_actions(self, actions, initial_state, goal):
        """Preprocess actions
        :param actions - Actions to be preprocessed
        :param initial_state - The initial state of a PDDL problem
        :param goal - The goal state """
        raise NotImplementedError("Unimplemented")

    def preprocess_states(self, states, initial_state, goal):
        """"Somehow preprocess states for some purpose"""
        raise NotImplementedError("Unimplemented")


class RPGReachabilityPreprocessor(PDDLPreprocessor):

    def __init__(self):
        super().__init__()

    def preprocess_actions(self, actions, initial_state, goal):
        """Uses the RPG to eliminate unreachable actions"""
        positive_g, negative_g = goal
        reachable_literals = initial_state
        positive_literals = None
        reachable_actions: Set[Any] = set()
        while positive_literals != reachable_literals:
            if positive_g.issubset(reachable_literals):
                return reachable_actions
            positive_literals = reachable_literals
            for a in actions:
                if applicable(positive_literals, a.positive_preconditions, frozenset([])): # TODO: This does not handle negative preconditions correctly
                    reachable_actions.add(a)
                    reachable_literals = reachable_literals.union(a.add_effects)

        return reachable_actions

    def preprocess_states(self, states, initial_state, goal):
        return states
