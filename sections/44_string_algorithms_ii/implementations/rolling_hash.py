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
