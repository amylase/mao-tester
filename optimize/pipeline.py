from typing import List

from mao.models import Rules
from . import Optimizer


class IterativeOptimizer(Optimizer):
    def __init__(self, delegate: Optimizer):
        self.delegate = delegate

    def optimize(self, rules: Rules) -> Rules:
        while True:
            new_rules = self.delegate.optimize(rules)
            if len(new_rules) >= len(rules):
                return rules
            rules = new_rules


class OptimizerChain(Optimizer):
    def __init__(self, optimizers: List[Optimizer]):
        self.optimizers = optimizers

    def optimize(self, rules: Rules) -> Rules:
        for optimizer in self.optimizers:
            rules = optimizer.optimize(rules)
        return rules


def iterate(optimizer: Optimizer) -> IterativeOptimizer:
    return IterativeOptimizer(optimizer)


def chain(optimizers: List[Optimizer]) -> OptimizerChain:
    return OptimizerChain(optimizers)
