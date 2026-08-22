import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = data[1:1 + q]
    maximum = max(queries, default=1)

    squarefree = [True] * (maximum + 1)
    squarefree[0] = False
    p = 2
    while p * p <= maximum:
        for multiple in range(p * p, maximum + 1, p * p):
            squarefree[multiple] = False
        p += 1

    prefix = [0] * (maximum + 1)
    for value in range(1, maximum + 1):
        prefix[value] = prefix[value - 1] + squarefree[value]

    print("\n".join(str(prefix[x]) for x in queries))


if __name__ == "__main__":
    main()
