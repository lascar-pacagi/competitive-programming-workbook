import sys


def count_alignments(source, target):
    n = len(target)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j and target[i] != target[j]:
            j = prefix[j - 1]
        if target[i] == target[j]:
            j += 1
        prefix[i] = j

    answer = matched = 0
    # Exactly n possible starting positions; omit the repeated last window.
    for ch in (source + source)[:-1]:
        while matched and ch != target[matched]:
            matched = prefix[matched - 1]
        if ch == target[matched]:
            matched += 1
        if matched == n:
            answer += 1
            matched = prefix[matched - 1]
    return answer


def main():
    source, target = sys.stdin.read().split()
    print(count_alignments(source, target))


if __name__ == '__main__':
    main()
