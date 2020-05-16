from typing import Iterable
from mao.interp import Interpreter
from mao.models import Judge, Problem


def _test(interp: Interpreter, judge: Judge, s: str, verbose=False):
    actual = interp.apply(s)
    expected = judge(s)
    success = actual == expected
    if not success and verbose:
        print(f"Wrong Answer. Input: {s}, Actual: {actual}, Expected: {expected}")
        verbose_interpreter = Interpreter(interp.rules, True, interp.max_iter)
        verbose_interpreter.apply(s)
    return success


def _stress_test(interp: Interpreter, judge: Judge, gen: Iterable[str], verbose=False):
    success_count = 0
    for s in gen:
        if not _test(interp, judge, s, verbose):
            if verbose:
                print(f"Wrong Answer after {success_count} successful tests.")
            return False
        success_count += 1
    if verbose:
        print(f"Passed all {success_count} tests. {len(interp.rules)} rules.")
    return True


def stress_test(interp: Interpreter, problem: Problem, verbose):
    return _stress_test(interp, problem.judge, problem.test_cases(), verbose)

