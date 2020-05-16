from typing import Tuple, List, Callable, Optional
from abc import abstractmethod


Rule = Tuple[str, str, bool]
Rules = List[Rule]


class Problem(object):
    @abstractmethod
    def test_cases(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def judge(self, s: str) -> str:
        raise NotImplementedError()

    def step_limit(self) -> Optional[int]:
        return None


Judge = Callable[[str], str]