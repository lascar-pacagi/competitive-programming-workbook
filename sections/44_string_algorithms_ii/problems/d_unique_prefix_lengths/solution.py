import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    words = [word.decode() for word in tokens[1:n + 1]]
    children = [{}]
    passed = [0]

    for word in words:
        node = 0
        for ch in word:
            if ch not in children[node]:
                child = len(children)
                children[node][ch] = child
                children.append({})
                passed.append(0)
            node = children[node][ch]
            passed[node] += 1

    answers = []
    for word in words:
        node = 0
        answer = -1
        for length, ch in enumerate(word, 1):
            node = children[node][ch]
            if passed[node] == 1:
                answer = length
                break
        answers.append(str(answer))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
