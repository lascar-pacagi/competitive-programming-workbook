import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    move_count, pile_count = data[0], data[1]
    moves = data[2 : 2 + move_count]
    piles = data[2 + move_count : 2 + move_count + pile_count]
    maximum = max(piles)
    grundy = [0] * (maximum + 1)
    for stones in range(1, maximum + 1):
        reachable = {grundy[stones - move] for move in moves if move <= stones}
        while grundy[stones] in reachable:
            grundy[stones] += 1
    total = 0
    for stones in piles:
        total ^= grundy[stones]
    print("WIN" if total else "LOSE")


if __name__ == "__main__":
    main()
