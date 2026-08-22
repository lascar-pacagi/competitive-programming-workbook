import sys
from functools import lru_cache

def count(n, pattern):
    digits = list(map(int, str(n)))
    p = list(map(int, pattern))
    fail = [0] * len(p)
    for i in range(1, len(p)):
        j = fail[i - 1]
        while j and p[i] != p[j]:
            j = fail[j - 1]
        if p[i] == p[j]:
            j += 1
        fail[i] = j

    def step(j, d):
        while j and p[j] != d:
            j = fail[j - 1]
        if p[j] == d:
            j += 1
        return j

    @lru_cache(None)
    def dp(pos, j, tight, started):
        if pos == len(digits):
            return int(started or pattern != '0')
        limit = digits[pos] if tight else 9
        answer = 0
        for d in range(limit + 1):
            nt = tight and d == limit
            if not started and d == 0:
                answer += dp(pos + 1, 0, nt, False)
            else:
                nj = step(j, d)
                if nj < len(p):
                    answer += dp(pos + 1, nj, nt, True)
        return answer
    return dp(0, 0, True, False)

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    for i in range(1, len(data), 2):
        out.append(str(count(int(data[i]), data[i + 1].decode())))
    print('\n'.join(out))
if __name__ == '__main__':
    main()
