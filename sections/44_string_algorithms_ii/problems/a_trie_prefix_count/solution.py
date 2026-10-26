import sys


class Trie:
    def __init__(self):
        self.children = [{}]
        self.passed = [0]

    def insert(self, word):
        v = 0
        self.passed[v] += 1
        for ch in word:
            if ch not in self.children[v]:
                child = len(self.children)
                self.children[v][ch] = child
                self.children.append({})
                self.passed.append(0)
            v = self.children[v][ch]
            self.passed[v] += 1

    def count_prefix(self, prefix):
        v = 0
        for ch in prefix:
            if ch not in self.children[v]:
                return 0
            v = self.children[v][ch]
        return self.passed[v]


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    q = int(next(tokens))
    trie = Trie()
    for _ in range(n):
        trie.insert(next(tokens))

    answers = []
    for _ in range(q):
        prefix = next(tokens)
        answers.append(str(trie.count_prefix(prefix)))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
