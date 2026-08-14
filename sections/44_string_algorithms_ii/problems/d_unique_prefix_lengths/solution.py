import sys


def main() -> None:
    words = sys.stdin.buffer.read().split()
    if not words: return
    n = int(words[0]); words = [word.decode() for word in words[1:n + 1]]
    children = [{}]; passed = [0]
    for word in words:
        node = 0
        for char in word:
            if char not in children[node]:
                children[node][char] = len(children); children.append({}); passed.append(0)
            node = children[node][char]; passed[node] += 1
    output = []
    for word in words:
        node = 0; answer = -1
        for length, char in enumerate(word, 1):
            node = children[node][char]
            if passed[node] == 1: answer = length; break
        output.append(str(answer))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__": main()
