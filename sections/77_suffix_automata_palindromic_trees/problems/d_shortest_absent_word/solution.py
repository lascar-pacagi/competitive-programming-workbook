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
    import collections
    import sys

    automaton = SAM(sys.stdin.buffer.readline().decode().strip())
    parent = [None] * len(automaton.next)
    letter = [""] * len(automaton.next)
    parent[0] = -1
    queue = collections.deque([0])
    while queue:
        state = queue.popleft()
        for code in range(26):
            char = chr(ord("a") + code)
            if char not in automaton.next[state]:
                answer = [char]
                while state:
                    answer.append(letter[state])
                    state = parent[state]
                print("".join(reversed(answer)))
                return
            target = automaton.next[state][char]
            if parent[target] is None:
                parent[target] = state
                letter[target] = char
                queue.append(target)


if __name__ == "__main__":
    main()
