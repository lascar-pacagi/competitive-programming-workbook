import sys

MOD = 1_000_000_007
BITS = 30


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    a = data[2:2 + n]
    queries = []
    pos = 2 + n
    for i in range(q):
        l = int(data[pos])
        r = int(data[pos + 1])
        x = int(data[pos + 2])
        pos += 3
        queries.append((r, l, x, i))
    queries.sort()
    pow2 = [1] * (n + 1)
    for i in range(n):
        pow2[i + 1] = pow2[i] * 2 % MOD
    # basis[b]: vector with leading bit b; where[b]: its (latest) position.
    # Inserting a newer element swaps it into the basis, so the vectors with
    # position >= l always span exactly a[l..r].
    basis = [0] * BITS
    where = [0] * BITS
    answer = [0] * q
    done = 0
    for r, l, x, idx in queries:
        while done < r:
            done += 1
            v = int(a[done - 1])
            p = done
            for b in range(BITS - 1, -1, -1):
                if not v >> b & 1:
                    continue
                if not basis[b]:
                    basis[b] = v
                    where[b] = p
                    break
                if where[b] < p:
                    basis[b], v = v, basis[b]
                    where[b], p = p, where[b]
                v ^= basis[b]
        rank = 0
        for b in range(BITS - 1, -1, -1):
            if basis[b] and where[b] >= l:
                rank += 1
                if x >> b & 1:
                    x ^= basis[b]
        answer[idx] = 0 if x else pow2[r - l + 1 - rank]
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
