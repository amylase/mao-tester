from mao.interp import Interpreter
from mao.models import Rules, Problem
from mao.tester import stress_test
from . import Optimizer, Tweaker


class Reverser(Tweaker):
    def tweak(self, rules: Rules) -> Rules:
        return list(reversed(rules))


class TweakAndDo(Optimizer):
    def __init__(self, problem: Problem, tweaker: Tweaker, optimizer: Optimizer):
        self.problem = problem
        self.tweaker = tweaker
        self.optimizer = optimizer

    def optimize(self, rules: Rules) -> Rules:
        tweaked_rules = self.tweaker.tweak(rules)
        optimized_interpreter = Interpreter(tweaked_rules, False, max_iter=self.problem.step_limit())
        success = stress_test(optimized_interpreter, self.problem, False)
        return tweaked_rules if success else rules

