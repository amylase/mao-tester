from abc import abstractmethod

from mao.models import Rules


class Optimizer(object):
    @abstractmethod
    def optimize(self, rules: Rules) -> Rules:
        raise NotImplementedError()


class Tweaker(object):
    @abstractmethod
    def tweak(self, rules: Rules) -> Rules:
        raise NotImplementedError()