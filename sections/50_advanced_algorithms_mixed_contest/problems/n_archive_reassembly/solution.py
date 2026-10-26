import sys


class SuffixAutomaton:
    def __init__(self, text):
        self.next = [{}]
        self.length = [0]
        self.link = [-1]
        last = 0
        for ch in text:
            cur = len(self.next)
            self.next.append({})
            self.length.append(self.length[last] + 1)
            self.link.append(0)
            p = last
            while p != -1 and ch not in self.next[p]:
                self.next[p][ch] = cur
                p = self.link[p]
            if p != -1:
                q = self.next[p][ch]
                if self.length[p] + 1 == self.length[q]:
                    self.link[cur] = q
                else:
                    clone = len(self.next)
                    self.next.append(self.next[q].copy())
                    self.length.append(self.length[p] + 1)
                    self.link.append(self.link[q])
                    while p != -1 and self.next[p].get(ch) == q:
                        self.next[p][ch] = clone
                        p = self.link[p]
                    self.link[q] = self.link[cur] = clone
            last = cur


def minimum_pieces(source, target):
    automaton = SuffixAutomaton(source)
    state = 0
    pieces = 1
    for ch in target:
        to = automaton.next[state].get(ch)
        if to is None:
            # Commit the longest possible piece, then retry from the root.
            pieces += 1
            to = automaton.next[0].get(ch)
            if to is None:
                return -1
        state = to
    return pieces


def main():
    source, target = sys.stdin.read().split()
    print(minimum_pieces(source, target))


if __name__ == '__main__':
    main()
