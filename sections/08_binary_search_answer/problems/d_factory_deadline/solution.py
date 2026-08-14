import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 1
    out = []
    for _ in range(data[0]):
        n, goal = data[index], data[index + 1]
        index += 2
        times = data[index:index + n]
        index += n
        lo, hi = 0, min(times) * goal
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(mid // value for value in times) >= goal:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(lo))
    print("\n".join(out))


if __name__ == "__main__":
    main()
