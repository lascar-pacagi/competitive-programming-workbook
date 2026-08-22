import sys
MAX_SUM = 171

def suffix_ways(mod):
    ways = [[[0] * mod for _ in range(MAX_SUM + 1)] for _ in range(20)]
    ways[0][0][0] = 1
    for length in range(1, 20):
        previous = ways[length - 1]
        current = ways[length]
        for total in range(MAX_SUM + 1):
            row = current[total]
            for digit in range(min(9, total) + 1):
                for remainder, value in enumerate(previous[total - digit]):
                    if value:
                        row[(remainder * 10 + digit) % mod] += value
    return ways

def count(n, target, mod, ways):
    if n < 0:
        return 0
    digits = list(map(int, str(n)))
    answer = 0
    prefix_sum = 0
    prefix_rem = 0
    powers = [pow(10, length, mod) for length in range(20)]
    for pos, limit in enumerate(digits):
        remaining = len(digits) - pos - 1
        for digit in range(limit):
            needed_sum = target - prefix_sum - digit
            if 0 <= needed_sum <= MAX_SUM:
                next_rem = (prefix_rem * 10 + digit) % mod
                needed_rem = -next_rem * powers[remaining] % mod
                answer += ways[remaining][needed_sum][needed_rem]
        prefix_sum += limit
        prefix_rem = (prefix_rem * 10 + limit) % mod
    return answer + int(prefix_sum == target and prefix_rem == 0)

def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    queries = [tuple(d[i:i + 4]) for i in range(1, len(d), 4)]
    out = [0] * len(queries)
    groups = {}
    for index, query in enumerate(queries):
        groups.setdefault(query[3], []).append(index)
    for mod, indices in groups.items():
        ways = suffix_ways(mod)
        for index in indices:
            left, right, target, _ = queries[index]
            out[index] = count(right, target, mod, ways) - count(left - 1, target, mod, ways)
    print('\n'.join(map(str, out)))
if __name__ == '__main__':
    main()
