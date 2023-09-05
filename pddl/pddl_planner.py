from pddl.pddl_parser import PDDLParser
from pddl.state import applicable
from pddl.benchmark import PlanningBenchmark
import time


class PDDLPlanner:

    planner_version = 'v2121.1'  # TODO Change this every year

    def __init__(self, verbose=False, collect_stats=False):
        self.verbose = verbose
        self.collect_benchmark = collect_stats
        self.stats = None

    # -----------------------------------------------
    # Solve
    # -----------------------------------------------

    def solve_file(self, domainfile, problemfile, preprocessor=None):
        if self.collect_benchmark: self.stats = PlanningBenchmark().get_instance(domainfile, problemfile)

        # Parser
        start_time = time.time()
        parser = PDDLParser()
        parser.parse_domain(domainfile)
        parser.parse_problem(problemfile)
        # Test if first state is not the goal
        if applicable(parser.state, parser.positive_goals, parser.negative_goals):
            return [], 0
        # Grounding process
        ground_actions = self.grounding(parser)
        if preprocessor:
            print("%d unprocessed actions" % len(ground_actions))
            ground_actions = preprocessor.preprocess_actions(ground_actions, parser.state, (parser.positive_goals, parser.negative_goals))
            print("%d preprocessed actions" % len(ground_actions))
        if self.stats: self.stats.action_space = len(ground_actions)  # compute stats
        plan = self.solve(ground_actions, parser.state, (parser.positive_goals, parser.negative_goals))
        final_time = time.time() - start_time
        if self.verbose:
            print('Time: ' + str(final_time) + 's')
            if plan:
                print('plan:')
                for act in plan:
                    print('(' + act.name + ''.join(' ' + p for p in act.parameters) + ')')
            else:
                print('No plan was found')
        if self.stats: self.stats.time = final_time
        return plan, final_time

    def grounding(self, parser):
        ground_actions = []
        if self.verbose: start_time = time.time()
        for action in parser.actions:
            for act in action.groundify(parser.objects, parser.types):
                ground_actions.append(act)

        if self.verbose:
            final_time = time.time() - start_time
            print("Grounding time: %d s" % final_time)
            print("Number of actions: %d" % len(ground_actions))
        return ground_actions

    def solve(self, domain, initial_state, goals):
        """Solves a planning problem defined by 'actions', 'state', and 'goal', returning the plan if one exists or none otherwise.

        Args:
            actions (list[Action]): A list of grounded actions for the problem to be solved, this is the action space.
            state (frozenset[tuple]): A set of grounded predicates defining the initial state of the problem
            goals (tuple[frozenset[tuple],frozenset[tuple]]): a tuple with two sets of tuples representing positive and negative goals

        Returns:
            list[Action]: A plan comprising a (possibly empty) list of actions from 'actions', that transform the initial 'state' into one that is a model of 'goals'.
        """
        raise NotImplementedError("PDDL Planners need to implement solve")
