import argparse
import functools
import random
from pathlib import Path


def oracle(s):
    alphabet = sorted(set(s))
    initial = tuple(s.count(char) for char in alphabet)

    @functools.lru_cache(None)
    def search(counts, previous):
        if sum(counts) == 0:
            return ""
        for i, char in enumerate(alphabet):
            if i == previous or counts[i] == 0:
                continue
            after = list(counts)
            after[i] -= 1
            suffix = search(tuple(after), i)
            if suffix is not None:
                return char + suffix
        return None

    answer = search(initial, -1)
    return "IMPOSSIBLE" if answer is None else answer


def greedy(s):
    count = [0] * 26
    for char in s:
        count[ord(char) - 97] += 1
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
        for char in range(26):
            if char == previous or count[char] == 0:
                continue
            same = count[char] - 1
            other = max(prefix[char], suffix[char + 1])
            if same <= remaining // 2 and other <= (remaining + 1) // 2:
                answer.append(chr(97 + char))
                count[char] -= 1
                previous = char
                break
        else:
            return "IMPOSSIBLE"
    return "".join(answer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = ["a", "aa", "aab", "aaab", "aaabb", "aabbcc", "zzzzaaaa"]
    for case in range(args.count):
        if case < len(fixed):
            s = fixed[case]
        elif case == len(fixed):
            s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz")
                        for _ in range(200000))
        else:
            s = "".join(rng.choice("abcde")
                        for _ in range(rng.randint(1, 10)))
        answer = greedy(s) if len(s) > 12 else oracle(s)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(s + "\n")
        stem.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
