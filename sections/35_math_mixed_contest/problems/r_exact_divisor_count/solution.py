import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = [tuple(data[1 + 2 * i:3 + 2 * i]) + (i,)
               for i in range(q)]
    maximum = max((n for n, _, _ in queries), default=1)

    divisor_count = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        for multiple in range(divisor, maximum + 1, divisor):
            divisor_count[multiple] += 1

    needed = {k for _, k, _ in queries}
    seen = {k: 0 for k in needed}
    answers = [0] * q
    pointer = 0
    for n, k, index in sorted(queries):
        while pointer < n:
            pointer += 1
            count = divisor_count[pointer]
            if count in seen:
                seen[count] += 1
        answers[index] = seen.get(k, 0)

    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
