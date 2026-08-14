import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, limit = data[0], data[1]
    durations = sorted(data[2 : 2 + n])
    elapsed = 0
    penalty = 0
    solved = 0
    for duration in durations:
        if elapsed + duration > limit:
            break
        elapsed += duration
        penalty += elapsed
        solved += 1
    print(solved, penalty)


if __name__ == "__main__":
    main()
