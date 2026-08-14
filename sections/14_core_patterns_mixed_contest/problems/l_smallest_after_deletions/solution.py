import sys


def main() -> None:
    s, raw_k = sys.stdin.buffer.read().split()
    k = int(raw_k)
    answer = []
    for digit in s.decode():
        while k and answer and answer[-1] > digit:
            answer.pop()
            k -= 1
        answer.append(digit)
    if k:
        del answer[-k:]
    print("".join(answer))


if __name__ == "__main__":
    main()
