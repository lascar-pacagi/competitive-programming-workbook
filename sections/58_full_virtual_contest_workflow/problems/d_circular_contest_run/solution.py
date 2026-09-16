import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, budget = data[0], data[1]
    times = data[2:]

    total = 0
    left = 0
    answer = 0
    for right in range(2 * n):
        total += times[right % n]
        while total > budget or right - left + 1 > n:
            total -= times[left % n]
            left += 1
        answer = max(answer, right - left + 1)

    print(answer)


if __name__ == '__main__':
    main()
