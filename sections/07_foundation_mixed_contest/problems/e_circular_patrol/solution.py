import sys


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    tests = int(tokens[0])
    index = 1
    answers = []
    for _ in range(tests):
        n = int(tokens[index])
        position = int(tokens[index + 1]) - 1
        commands = tokens[index + 2].decode()
        index += 3
        seen = {position}
        for command in commands:
            position = (position + (1 if command == "R" else -1)) % n
            seen.add(position)
        answers.append(f"{position + 1} {len(seen)}")
    print("\n".join(answers))


if __name__ == "__main__":
    main()
