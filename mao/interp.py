from typing import Tuple, Optional
from mao.models import Rules

MAX_ITERATION = 50000
MAX_LENGTH = 500


class Interpreter(object):
    def __init__(self, rules: Rules, verbose: bool=False, max_iter: Optional[int]=None):
        self.rules = rules
        self.verbose = verbose
        self.max_iter = max_iter or MAX_ITERATION

    def print(self, *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)

    def apply_once(self, s: str) -> Tuple[str, bool]:
        for fr, to, is_terminal in self.rules:
            pos = s.find(fr)
            if pos >= 0:
                return s[:pos] + to + s[pos + len(fr):], is_terminal
        return s, True

    def apply(self, s: str) -> Optional[str]:
        visited = set()
        for i in range(self.max_iter):
            if len(s) > MAX_LENGTH:
                self.print("Length Limit Exceeded.")
                return None
            if s in visited:
                # infinite loop detected
                self.print("Detected Infinite Loop.")
                return None
            visited.add(s)
            s, is_terminal = self.apply_once(s)
            self.print(f"{i:05}:{s}")
            if is_terminal:
                return s
        self.print("Step Limit Exceeded.")
        return None


def parse_source(s: str) -> Rules:
    rules = []
    for l in s.splitlines():
        l = l
        terminal_pos = l.find('::')
        if terminal_pos >= 0:
            fr, to = [p.strip() for p in l.split('::')]
            rules.append((fr.strip(), to.strip(), True))
            continue
        nonterminal_pos = l.find(':')
        if nonterminal_pos >= 0:
            fr, to = [p.strip() for p in l.split(':')]
            rules.append((fr.strip(), to.strip(), False))
            continue
    return rules


if __name__ == '__main__':
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("-v", action='store_true')
    args = parser.parse_args()
    with open(args.source) as f:
        rules = parse_source(f.read())
    interp = Interpreter(rules, args.verbose)
    s = sys.stdin.read().strip()
    result = interp.apply(s)
    if result is None:
        print("Evaluation Error. Try -v option to debug")
        quit(1)
    else:
        print(result)

