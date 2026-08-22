import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    events = []
    ys = []
    at = 1
    for _ in range(n):
        x1, y1, x2, y2 = data[at : at + 4]
        at += 4
        events.append((x1, -1, y1, y2))  # additions sort first
        events.append((x2, +1, y1, y2))
        ys.extend((y1, y2))
    ys = sorted(set(ys))
    position = {value: index for index, value in enumerate(ys)}
    events.sort()

    size = 4 * (len(ys) - 1)
    cover = [0] * size
    length = [0] * size
    components = [0] * size
    left_covered = [False] * size
    right_covered = [False] * size

    def pull(node: int, low: int, high: int) -> None:
        if cover[node] > 0:
            length[node] = ys[high] - ys[low]
            components[node] = 1
            left_covered[node] = right_covered[node] = True
        elif high - low == 1:
            length[node] = components[node] = 0
            left_covered[node] = right_covered[node] = False
        else:
            left = 2 * node
            right = left + 1
            length[node] = length[left] + length[right]
            components[node] = (
                components[left] + components[right]
                - (right_covered[left] and left_covered[right])
            )
            left_covered[node] = left_covered[left]
            right_covered[node] = right_covered[right]

    def update(start: int, end: int, delta: int, node=1, low=0, high=None) -> None:
        if high is None:
            high = len(ys) - 1
        if end <= low or high <= start:
            return
        if start <= low and high <= end:
            cover[node] += delta
            pull(node, low, high)
            return
        middle = (low + high) // 2
        update(start, end, delta, 2 * node, low, middle)
        update(start, end, delta, 2 * node + 1, middle, high)
        pull(node, low, high)

    area = perimeter = 0
    previous_x = events[0][0]
    index = 0
    while index < len(events):
        x = events[index][0]
        width = x - previous_x
        area += length[1] * width
        perimeter += 2 * components[1] * width
        while index < len(events) and events[index][0] == x:
            _, encoded_delta, y1, y2 = events[index]
            before = length[1]
            update(position[y1], position[y2], -encoded_delta)
            perimeter += abs(length[1] - before)
            index += 1
        previous_x = x

    print(area, perimeter)


if __name__ == "__main__":
    main()
