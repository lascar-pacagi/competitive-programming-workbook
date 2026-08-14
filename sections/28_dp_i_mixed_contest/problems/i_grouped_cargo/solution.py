import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    groups, capacity = data[index:index + 2]
    index += 2
    dp = [0] * (capacity + 1)

    for _ in range(groups):
        count = data[index]
        index += 1
        items = []
        for _ in range(count):
            weight, value = data[index:index + 2]
            index += 2
            items.append((weight, value))

        next_dp = dp.copy()
        for weight, value in items:
            for used in range(capacity - weight + 1):
                next_dp[used + weight] = max(
                    next_dp[used + weight], dp[used] + value)
        dp = next_dp

    print(max(dp))


if __name__ == "__main__":
    main()
