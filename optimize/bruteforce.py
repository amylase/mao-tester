from typing import List, Iterable

from mao.interp import Interpreter
from mao.models import Rule, Problem
from mao.tester import stress_test
from . import Optimizer


class BruteforceOptimizer(Optimizer):
    def __init__(self, problem: Problem):
        self.problem = problem

    def optimize(self, rules: [Iterable[Rule]]) -> List[Rule]:
        for i in range(len(rules)):
            sub_rules = rules[:i] + rules[i + 1:]
            interp = Interpreter(sub_rules, max_iter=self.problem.step_limit())
            success = stress_test(interp, self.problem, False)
            if success:
                return sub_rules
        return rules
