import argparse
import heapq
import random
from pathlib import Path


def oracle(s):
    best = None
    endings = []
    labels = []

    def search(position):
        nonlocal best
        if position == len(s):
            candidate = (len(endings), tuple(labels))
            if best is None or candidate < best:
                best = candidate
            return
        if best is not None and len(endings) > best[0]:
            return

        for group, ending in enumerate(endings):
            if ending == s[position]:
                continue
            endings[group] = s[position]
            labels.append(group + 1)
            search(position + 1)
            labels.pop()
            endings[group] = ending

        endings.append(s[position])
        labels.append(len(endings))
        search(position + 1)
        labels.pop()
        endings.pop()

    search(0)
    return best


def greedy(s):
    ending = [[], []]
    labels = []
    groups = 0
    for character in s:
        bit = int(character)
        opposite = 1 - bit
        if ending[opposite]:
            group = heapq.heappop(ending[opposite])
        else:
            groups += 1
            group = groups
        heapq.heappush(ending[bit], group)
        labels.append(group)
    return groups, tuple(labels)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = ["0", "1", "0000", "010101", "011", "00110100"]

    for case in range(args.count):
        if case < len(fixed):
            s = fixed[case]
        elif case == len(fixed):
            s = "".join(rng.choice("01") for _ in range(200000))
        else:
            s = "".join(rng.choice("01")
                        for _ in range(rng.randint(1, 10)))
        groups, labels = greedy(s) if len(s) > 11 else oracle(s)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(s + "\n")
        stem.with_suffix(".out").write_text(
            f"{groups}\n" + " ".join(map(str, labels)) + "\n")


if __name__ == "__main__":
    main()
