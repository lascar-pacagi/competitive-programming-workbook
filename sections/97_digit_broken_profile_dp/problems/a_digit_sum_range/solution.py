import sys
MAX_SUM = 171
WAYS = [[0] * (MAX_SUM + 1) for _ in range(20)]
WAYS[0][0] = 1
for length in range(1, 20):
    for total in range(MAX_SUM + 1):
        WAYS[length][total] = sum((WAYS[length - 1][total - digit] for digit in range(10) if digit <= total))

def count(n, target):
    if n < 0:
        return 0
    digits = list(map(int, str(n)))
    answer = 0
    prefix = 0
    for pos, limit in enumerate(digits):
        remaining = len(digits) - pos - 1
        for digit in range(limit):
            needed = target - prefix - digit
            if 0 <= needed <= MAX_SUM:
                answer += WAYS[remaining][needed]
        prefix += limit
    return answer + int(prefix == target)

def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    print('\n'.join((str(count(d[i + 1], d[i + 2]) - count(d[i] - 1, d[i + 2])) for i in range(1, len(d), 3))))
if __name__ == '__main__':
    main()
