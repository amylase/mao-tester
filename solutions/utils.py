import mao.interp
import mao.tester
from mao.models import Problem, Rules
from optimize.bruteforce import BruteforceOptimizer
from optimize.pipeline import iterate


def binary(x: int):
    return bin(x)[2:]


def pad_binary(x: int, l: int):
    b = binary(x)
    if len(b) < l:
        b = '0' * (l - len(b)) + b
    return b


def simple_optimizer(problem: Problem):
    return iterate(BruteforceOptimizer(problem))


def serialize_rules(rules: Rules) -> str:
    rule_strs = []
    for fr, to, is_terminal in rules:
        tokens = [fr.strip(), '::' if is_terminal else ':', to.strip()]
        rule_strs.append(''.join(tokens))
    return '\n'.join(rule_strs)


def run(problem, solution, optimize=True, verbose=True) -> bool:
    rules = mao.interp.parse_source(solution)
    interp = mao.interp.Interpreter(rules, max_iter=problem.step_limit())

    success = mao.tester.stress_test(interp, problem, verbose=verbose)
    if not success:
        return False

    if optimize:
        optimizer = simple_optimizer(problem)
        optimized_rules = optimizer.optimize(rules)
        print(f"optimized. {len(rules)} rules -> {len(optimized_rules)} rules.")
    else:
        optimized_rules = rules
        print("optimization skipped")
    optimized_solution = serialize_rules(optimized_rules)
    with open("output.txt", "w") as f:
        f.write(optimized_solution)
    print(f"wrote a solution. size: {len(optimized_solution)} bytes")
    return True