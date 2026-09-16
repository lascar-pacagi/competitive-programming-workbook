import heapq
import sys


def main():
    lines = sys.stdin.buffer.readlines()
    current = {}
    heap = []
    output = []

    for line in lines[1:]:
        fields = line.split()
        operation = fields[0]

        if operation in (b'A', b'U'):
            identifier = int(fields[1])
            priority = int(fields[2])
            current[identifier] = priority
            heapq.heappush(heap, (-priority, identifier))
            continue

        while heap:
            negative_priority, identifier = heap[0]
            priority = -negative_priority
            if current.get(identifier) == priority:
                break
            heapq.heappop(heap)

        if not heap:
            output.append("-1")
        else:
            _, identifier = heapq.heappop(heap)
            del current[identifier]
            output.append(str(identifier))

    sys.stdout.write('\n'.join(output))


if __name__ == '__main__':
    main()
