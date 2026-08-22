import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[:2]
    machines = [tuple(data[i : i + 3]) for i in range(2, 3 * n + 2, 3)]
    if sum(cap for _, _, cap in machines) < k:
        print("IMPOSSIBLE")
        return

    def count(threshold):
        result = 0
        for a, b, cap in machines:
            if threshold >= a + b:
                result += min(cap, (threshold - b + a) // (2 * a))
            if result >= k:
                return k
        return result

    lo, hi = -4 * 10**18, 4 * 10**18
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    threshold = lo
    used = answer = 0
    for a, b, cap in machines:
        x = 0
        if threshold - 1 >= a + b:
            x = min(cap, (threshold - 1 - b + a) // (2 * a))
        used += x
        answer += a * x * x + b * x
    print(answer + (k - used) * threshold)


if __name__ == "__main__":
    main()
