from pddl.benchmark import PlanningBenchmark, InstanceStats


class Heuristic:

    def __init__(self, is_safe=False, is_goal_aware=True, is_consistent=False, stats=None):
        self.stats = stats
        # Ensure that you document heuristics properties correctly
        self.is_safe = is_safe
        self.is_goal_aware = is_goal_aware
        self.is_consistent = is_consistent

    def __call__(self, actions, initial_state, goals):
        if self.stats: self.stats.h_calls += 1
        return self.h(actions, initial_state, goals)

    def h(self, domain, initial_state, goals):
        """A heuristic estimate of the cost to solve the planning problem defined by the following parameters:
        :param domain(list[Action]): A list of grounded actions for the problem to be solved, this is the action space.
        :param initial_state(frozenset[tuple]): A set of grounded predicates defining the initial state of the problem
        :param goals(tuple[frozenset[tuple],frozenset[tuple]]): a tuple with two sets of tuples representing positive and negative goals
        :return:
        :rtype float: an estimate (usually an integer unless it is infinity) of the cost to reach 'goals' from 'state' computed using the max heuristic.
        """
        raise NotImplementedError("Unimplemented")
