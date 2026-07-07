import math
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    log = [0] * (n + 1)
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1
    st = [a]
    k = 1
    while (1 << k) <= n:
        prev = st[-1]
        length = 1 << (k - 1)
        st.append([math.gcd(prev[i], prev[i + length]) for i in range(n - (1 << k) + 1)])
        k += 1
    idx = 2 + n
    out = []
    for _ in range(q):
        l, r = data[idx] - 1, data[idx + 1] - 1
        idx += 2
        k = log[r - l + 1]
        out.append(str(math.gcd(st[k][l], st[k][r - (1 << k) + 1])))
    print("\n".join(out))

if __name__ == "__main__":
    main()
