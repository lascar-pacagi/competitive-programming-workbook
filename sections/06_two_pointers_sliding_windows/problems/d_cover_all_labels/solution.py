import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    tests = data[index]
    index += 1
    out: list[str] = []
    for _ in range(tests):
        n = data[index]
        labels = data[index + 1]
        index += 2
        values = data[index:index + n]
        index += n

        count = [0] * (labels + 1)
        missing = labels
        left = 0
        answer = n + 1
        for right, value in enumerate(values):
            if count[value] == 0:
                missing -= 1
            count[value] += 1
            while missing == 0:
                answer = min(answer, right - left + 1)
                count[values[left]] -= 1
                if count[values[left]] == 0:
                    missing += 1
                left += 1
        out.append(str(-1 if answer == n + 1 else answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
