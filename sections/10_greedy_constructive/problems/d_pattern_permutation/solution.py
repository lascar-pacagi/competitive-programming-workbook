import sys


def construct(pattern: str) -> list[int]:
    pending: list[int] = []
    answer: list[int] = []
    n = len(pattern) + 1

    for value in range(1, n + 1):
        pending.append(value)
        if value == n or pattern[value - 1] == "<":
            answer.extend(reversed(pending))
            pending.clear()
    return answer


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    tests = int(next(it))
    out: list[str] = []
    for _ in range(tests):
        n = int(next(it))
        pattern = next(it)
        assert len(pattern) == n - 1
        out.append(" ".join(map(str, construct(pattern))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
