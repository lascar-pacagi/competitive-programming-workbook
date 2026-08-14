import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    events = sorted(zip(data[1::2], data[2::2]))
    finishes = []
    index = answer = 0
    day = 0
    while index < len(events) or finishes:
        if not finishes:
            day = max(day, events[index][0])
        while index < len(events) and events[index][0] <= day:
            heapq.heappush(finishes, events[index][1])
            index += 1
        while finishes and finishes[0] < day:
            heapq.heappop(finishes)
        if finishes:
            heapq.heappop(finishes)
            answer += 1
            day += 1
    print(answer)


if __name__ == "__main__":
    main()
