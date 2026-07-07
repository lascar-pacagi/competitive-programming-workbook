import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    idx = 2 + n
    block = max(1, int(n ** 0.5))
    queries = []
    for qi in range(q):
        l, r = data[idx] - 1, data[idx + 1] - 1
        idx += 2
        queries.append((l, r, qi))
    queries.sort(key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1]))
    freq = defaultdict(int)
    ans = [0] * q
    distinct = 0
    left, right = 0, -1
    for l, r, qi in queries:
        while right < r:
            right += 1
            freq[a[right]] += 1
            if freq[a[right]] == 1:
                distinct += 1
        while right > r:
            freq[a[right]] -= 1
            if freq[a[right]] == 0:
                distinct -= 1
            right -= 1
        while left < l:
            freq[a[left]] -= 1
            if freq[a[left]] == 0:
                distinct -= 1
            left += 1
        while left > l:
            left -= 1
            freq[a[left]] += 1
            if freq[a[left]] == 1:
                distinct += 1
        ans[qi] = distinct
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
