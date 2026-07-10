import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    teammates, cards, edges = data[:3]
    graph = [[] for _ in range(teammates + 1)]
    index = 3
    for _ in range(edges):
        teammate, card = data[index], data[index + 1]
        index += 2
        graph[teammate].append(card)

    match_card = [0] * (cards + 1)

    def augment(teammate: int) -> bool:
        for card in graph[teammate]:
            if seen[card]:
                continue
            seen[card] = True
            if match_card[card] == 0 or augment(match_card[card]):
                match_card[card] = teammate
                return True
        return False

    answer = 0
    for teammate in range(1, teammates + 1):
        seen = [False] * (cards + 1)
        answer += augment(teammate)
    print(answer)


if __name__ == "__main__":
    main()
