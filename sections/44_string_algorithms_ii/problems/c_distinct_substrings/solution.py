import sys


class SuffixAutomaton:
    def __init__(self):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.last = 0

    def extend(self, ch):
        # 1. Make a state for the new whole text and its new suffixes.
        cur = len(self.next)
        self.next.append({})
        self.length.append(self.length[self.last] + 1)
        self.link.append(0)
        p = self.last

        # 2. Visit old suffix groups that have no ch continuation.
        while p != -1 and ch not in self.next[p]:
            self.next[p][ch] = cur
            p = self.link[p]

        # 3. Find the next shorter group for cur.
        if p == -1:
            # Case 1: ch is new; only the empty suffix was known.
            self.link[cur] = 0
        else:
            q = self.next[p][ch]
            if self.length[p] + 1 == self.length[q]:
                # Case 2: all of q is the next suffix group.
                self.link[cur] = q
            else:
                # Case 3: split q; clone keeps its shorter strings.
                # Copy the dictionary so the two states are independent.
                clone = len(self.next)
                self.next.append(self.next[q].copy())
                self.length.append(self.length[p] + 1)
                self.link.append(self.link[q])

                # Redirect only the shorter incoming contexts.
                while p != -1:
                    # Every shorter suffix also has a ch transition.
                    assert ch in self.next[p]
                    if self.next[p][ch] != q:
                        break
                    self.next[p][ch] = clone
                    p = self.link[p]
                # Both longer groups now have clone as suffix parent.
                self.link[q] = clone
                self.link[cur] = clone

        self.last = cur

    def count_distinct(self):
        return sum(
            self.length[v] - self.length[self.link[v]]
            for v in range(1, len(self.next))
        )


def main():
    s = sys.stdin.readline().strip()
    sam = SuffixAutomaton()
    for ch in s:
        sam.extend(ch)
    print(sam.count_distinct())


if __name__ == "__main__":
    main()
