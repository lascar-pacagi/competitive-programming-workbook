import heapq
import sys


def main() -> None:
    s = sys.stdin.buffer.readline().strip().decode()
    ending = [[], []]
    answer = []
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
        answer.append(group)

    print(groups)
    print(*answer)


if __name__ == "__main__":
    main()
