import sys


def minimum_cost(positions, groups):
    n = len(positions)
    prefix = [0]
    for x in positions:
        prefix.append(prefix[-1] + x)

    def cost(left, right):
        # Half-open block [left, right), using its lower median.
        median = (left + right - 1) // 2
        x = positions[median]
        return (x * (median - left) - (prefix[median] - prefix[left])
                + prefix[right] - prefix[median + 1]
                - x * (right - median - 1))

    infinity = 10**30
    previous = [0] + [infinity] * n
    for group in range(1, groups + 1):
        current = [infinity] * (n + 1)

        def compute(low, high, opt_low, opt_high):
            if low > high:
                return
            middle = (low + high) // 2
            best_value = infinity
            best_split = opt_low
            for split in range(opt_low, min(opt_high, middle - 1) + 1):
                candidate = previous[split] + cost(split, middle)
                if candidate < best_value:
                    best_value = candidate
                    best_split = split
            current[middle] = best_value
            compute(low, middle - 1, opt_low, best_split)
            compute(middle + 1, high, best_split, opt_high)

        compute(group, n, group - 1, n - 1)
        previous = current
    return previous[n]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    print(minimum_cost(data[2:2 + n], k))


if __name__ == '__main__':
    main()
