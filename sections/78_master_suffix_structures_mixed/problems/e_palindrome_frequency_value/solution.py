class Eertree:
    def __init__(self):
        self.next = [{}, {}]
        self.length = [-1, 0]
        self.link = [0, 0]
        self.occ = [0, 0]
        self.text = []
        self.last = 1

    def add(self, char):
        position = len(self.text)
        self.text.append(char)
        node = self.last
        while (
            position - 1 - self.length[node] < 0
            or self.text[position - 1 - self.length[node]] != char
        ):
            node = self.link[node]
        if char in self.next[node]:
            self.last = self.next[node][char]
            self.occ[self.last] += 1
            return False
        created = len(self.next)
        self.next.append({})
        self.length.append(self.length[node] + 2)
        self.link.append(1)
        self.occ.append(1)
        self.next[node][char] = created
        if self.length[created] > 1:
            suffix = self.link[node]
            while (
                position - 1 - self.length[suffix] < 0
                or self.text[position - 1 - self.length[suffix]] != char
            ):
                suffix = self.link[suffix]
            self.link[created] = self.next[suffix][char]
        self.last = created
        return True


def main():
    import sys

    tree = Eertree()
    for char in sys.stdin.buffer.readline().decode().strip():
        tree.add(char)
    order = sorted(
        range(2, len(tree.next)), key=tree.length.__getitem__, reverse=True
    )
    answer = 0
    for node in order:
        answer = max(answer, tree.length[node] * tree.occ[node])
        tree.occ[tree.link[node]] += tree.occ[node]
    print(answer)


if __name__ == "__main__":
    main()
