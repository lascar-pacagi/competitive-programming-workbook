import sys


class RollingHash:
    MOD1 = 1_000_000_007
    MOD2 = 1_000_000_009
    BASE = 911_382_323

    def __init__(self, s):
        n = len(s)
        self.h1 = [0] * (n + 1)
        self.h2 = [0] * (n + 1)
        self.p1 = [1] * (n + 1)
        self.p2 = [1] * (n + 1)
        for i, ch in enumerate(s):
            value = ord(ch) - ord("a") + 1
            self.h1[i + 1] = (
                self.h1[i] * self.BASE + value
            ) % self.MOD1
            self.h2[i + 1] = (
                self.h2[i] * self.BASE + value
            ) % self.MOD2
            self.p1[i + 1] = self.p1[i] * self.BASE % self.MOD1
            self.p2[i + 1] = self.p2[i] * self.BASE % self.MOD2

    def get(self, l, r):
        # Hash of s[l:r], with 0-based, half-open endpoints.
        a = (
            self.h1[r] - self.h1[l] * self.p1[r - l]
        ) % self.MOD1
        b = (
            self.h2[r] - self.h2[l] * self.p2[r - l]
        ) % self.MOD2
        return a, b


def main():
    s = sys.stdin.readline().strip()
    forward = RollingHash(s)
    backward = RollingHash(s[::-1])
    n = len(s)
    q = int(sys.stdin.readline())
    answers = []
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        l -= 1
        same = forward.get(l, r) == backward.get(n - r, n - l)
        answers.append("YES" if same else "NO")
    print("\n".join(answers))


if __name__ == "__main__":
    main()
