import sys


def main() -> None:
    # TODO: topologically process jobs and compute earliest finish times.
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    raise NotImplementedError("solve.py is for your solution")


if __name__ == "__main__":
    main()

