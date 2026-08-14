"""Reference solution for D. Equal Index Pairs."""

import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    index = 1
    out: list[str] = []
    for _ in range(t):
        n = data[index]
        index += 1
        freq: dict[int, int] = {}
        answer = 0
        for value in data[index:index + n]:
            answer += freq.get(value, 0)
            freq[value] = freq.get(value, 0) + 1
        index += n
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
