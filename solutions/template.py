from mao.models import Problem
from solutions.utils import run, binary
import random
import itertools

solution = """
BA:AB
CA:AC
CB:BC
"""


class Problem6(Problem):
    def judge(self, s: str) -> str:
        return ''.join(sorted(s))

    def test_cases(self) -> str:
        rng = random.Random(12345)
        for length in range(1, 6):
            for chars in itertools.product("ABC", repeat=length):
                yield ''.join(chars)
        for length in range(6, 16):
            for case in range(20):
                chars = rng.choices("ABC", k=length)
                yield ''.join(chars)


if __name__ == '__main__':
    run(Problem6(), solution)