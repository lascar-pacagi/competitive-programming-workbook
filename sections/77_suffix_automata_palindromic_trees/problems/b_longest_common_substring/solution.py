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

    a, b = (part.decode() for part in sys.stdin.buffer.read().split())
    automaton = SAM(a)
    state = length = answer = 0
    for char in b:
        while state and char not in automaton.next[state]:
            state = automaton.link[state]
            length = min(length, automaton.length[state])
        if char in automaton.next[state]:
            state = automaton.next[state][char]
            length += 1
        else:
            state = length = 0
        answer = max(answer, length)
    print(answer)


if __name__ == "__main__":
    main()
