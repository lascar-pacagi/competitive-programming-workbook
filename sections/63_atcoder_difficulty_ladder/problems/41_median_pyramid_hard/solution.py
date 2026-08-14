import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    start = data[1]
    target = data[2]

    previous_operation = 0
    answer = 0
    for index in range(n - 1):
        mismatch = start[index] != target[index]
        current_operation = int(mismatch) ^ previous_operation
        answer += current_operation
        previous_operation = current_operation

    if previous_operation != (start[-1] != target[-1]):
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
