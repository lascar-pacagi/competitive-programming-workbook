import sys


def main() -> None:
    s = sys.stdin.buffer.readline().strip().decode()
    count = [0] * 26
    for char in s:
        count[ord(char) - ord("a")] += 1
    answer = []
    previous = -1
    for position in range(len(s)):
        prefix = [0] * 27
        suffix = [0] * 27
        for char in range(26):
            prefix[char + 1] = max(prefix[char], count[char])
        for char in range(25, -1, -1):
            suffix[char] = max(suffix[char + 1], count[char])
        remaining = len(s) - position - 1
        chosen = -1
        for char in range(26):
            if char == previous or count[char] == 0:
                continue
            same = count[char] - 1
            other = max(prefix[char], suffix[char + 1])
            if same <= remaining // 2 and other <= (remaining + 1) // 2:
                chosen = char
                break
        if chosen == -1:
            print("IMPOSSIBLE")
            return
        answer.append(chr(ord("a") + chosen))
        count[chosen] -= 1
        previous = chosen
    print("".join(answer))


if __name__ == "__main__":
    main()
