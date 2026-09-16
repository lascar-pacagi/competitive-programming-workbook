import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, wanted = data[:2]
    at = 2
    machines = []
    base_cost = 0
    minimum_total = maximum_total = 0
    for _ in range(n):
        a, b, low, high = data[at:at + 4]
        at += 4
        base_cost += a * low * low + b * low
        minimum_total += low
        maximum_total += high
        capacity = high - low
        if capacity:
            start = a * (2 * low + 1) + b
            last = start + 2 * a * (capacity - 1)
            machines.append((a, start, capacity, last))

    if not minimum_total <= wanted <= maximum_total:
        print("IMPOSSIBLE")
        return
    need = wanted - minimum_total
    if need == 0:
        print(base_cost)
        return

    def count_at_most(threshold):
        count = 0
        for a, start, capacity, _ in machines:
            if threshold >= start:
                count += min(capacity, (threshold - start) // (2 * a) + 1)
                if count >= need:
                    return need
        return count

    left = min(start for _, start, _, _ in machines)
    right = max(last for _, _, _, last in machines)
    while left < right:
        middle = (left + right) // 2
        if count_at_most(middle) >= need:
            right = middle
        else:
            left = middle + 1
    threshold = left

    answer = base_cost
    selected = 0
    for a, start, capacity, _ in machines:
        if threshold <= start:
            continue
        take = min(capacity, (threshold - 1 - start) // (2 * a) + 1)
        selected += take
        answer += take * start + a * take * (take - 1)
    answer += (need - selected) * threshold
    print(answer)


if __name__ == '__main__':
    main()
