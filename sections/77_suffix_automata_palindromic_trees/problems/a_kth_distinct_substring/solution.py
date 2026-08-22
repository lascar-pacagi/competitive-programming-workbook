class SAM:
    def __init__(self, s):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.occ = [0]
        last = 0
        for char in s:
            current = len(self.next)
            self.next.append({})
            self.link.append(0)
            self.length.append(self.length[last] + 1)
            self.occ.append(1)
            parent = last
            while parent != -1 and char not in self.next[parent]:
                self.next[parent][char] = current
                parent = self.link[parent]
            if parent == -1:
                self.link[current] = 0
            else:
                target = self.next[parent][char]
                if self.length[parent] + 1 == self.length[target]:
                    self.link[current] = target
                else:
                    clone = len(self.next)
                    self.next.append(self.next[target].copy())
                    self.link.append(self.link[target])
                    self.length.append(self.length[parent] + 1)
                    self.occ.append(0)
                    while (
                        parent != -1 and self.next[parent].get(char) == target
                    ):
                        self.next[parent][char] = clone
                        parent = self.link[parent]
                    self.link[target] = self.link[current] = clone
            last = current

    def order(self):
        return sorted(range(len(self.next)), key=self.length.__getitem__)

    def occurrences(self):
        order = self.order()
        for state in reversed(order[1:]):
            self.occ[self.link[state]] += self.occ[state]


def main():
    import sys

    raw_s, raw_k = sys.stdin.buffer.read().split()
    automaton = SAM(raw_s.decode())
    k = int(raw_k)
    paths = [0] * len(automaton.next)
    for state in reversed(automaton.order()):
        paths[state] = sum(
            1 + paths[target] for target in automaton.next[state].values()
        )
    if k > paths[0]:
        print("IMPOSSIBLE")
        return
    answer = []
    state = 0
    while k:
        for char, target in sorted(automaton.next[state].items()):
            block = 1 + paths[target]
            if k > block:
                k -= block
            else:
                answer.append(char)
                k -= 1
                state = target
                break
    print("".join(answer))


if __name__ == "__main__":
    main()
