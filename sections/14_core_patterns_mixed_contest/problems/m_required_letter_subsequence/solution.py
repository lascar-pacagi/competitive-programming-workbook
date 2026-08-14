import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    s = data[0].decode()
    k = int(data[1])
    required = data[2].decode()
    r = int(data[3])
    remaining_required = s.count(required)
    chosen_required = 0
    answer = []
    for i, char in enumerate(s):
        while (answer and answer[-1] > char
               and len(answer) - 1 + len(s) - i >= k
               and (answer[-1] != required
                    or chosen_required - 1 + remaining_required >= r)):
            if answer[-1] == required:
                chosen_required -= 1
            answer.pop()
        if len(answer) < k:
            if char == required:
                answer.append(char)
                chosen_required += 1
            elif k - len(answer) - 1 >= r - chosen_required:
                answer.append(char)
        if char == required:
            remaining_required -= 1
    print("".join(answer))


if __name__ == "__main__":
    main()
