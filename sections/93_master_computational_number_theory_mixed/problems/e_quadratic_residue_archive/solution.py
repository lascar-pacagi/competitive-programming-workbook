import sys, math, random
MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
_rng = random.Random(712367821)

def rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = _rng.randrange(1, n)
        x = _rng.randrange(0, n)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d

def factor(n):
    out = []
    stack = [n]
    while stack:
        x = stack.pop()
        if x == 1:
            continue
        if is_prime(x):
            out.append(x)
        else:
            d = rho(x)
            stack.extend((d, x // d))
    out.sort()
    return out

def groups(n):
    result = []
    for p in factor(n):
        if result and result[-1][0] == p:
            result[-1] = (p, result[-1][1] + 1)
        else:
            result.append((p, 1))
    return result

def phi(n):
    answer = n
    for p, _ in groups(n):
        answer = answer // p * (p - 1)
    return answer

def lcm(a, b):
    return a // math.gcd(a, b) * b

def carmichael(n):
    answer = 1
    for p, e in groups(n):
        part = 1 << e - 2 if p == 2 and e >= 3 else (p - 1) * p ** (e - 1)
        answer = lcm(answer, part)
    return answer

def primitive_root(p):
    if p == 2:
        return 1
    primes = [q for q, _ in groups(p - 1)]
    g = 2
    while any((pow(g, (p - 1) // q, p) == 1 for q in primes)):
        g += 1
    return g

def bsgs(a, b, m):
    a %= m
    b %= m
    if m == 1:
        return 0
    size = math.isqrt(m) + 1
    baby = {}
    value = 1
    for j in range(size):
        baby.setdefault(value, j)
        value = value * a % m
    step = pow(pow(a, size, m), -1, m)
    value = b
    best = None
    for i in range(size + 1):
        if value in baby:
            candidate = i * size + baby[value]
            if best is None or candidate < best:
                best = candidate
        value = value * step % m
    return best

def discrete_log(a, b, m):
    a %= m
    b %= m
    if b == 1 % m:
        return 0
    added = 0
    scale = 1
    while True:
        g = math.gcd(a, m)
        if g == 1:
            break
        if b % g:
            return None
        m //= g
        b //= g
        scale = scale * (a // g) % m
        added += 1
        if scale == b:
            return added
        if m == 1:
            return added
    target = b * pow(scale, -1, m) % m
    tail = bsgs(a % m, target, m)
    return None if tail is None else added + tail

def tonelli(a, p):
    a %= p
    if a == 0:
        return 0
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    c = pow(z, q, p)
    x = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        i = 1
        value = t * t % p
        while value != 1:
            value = value * value % p
            i += 1
        b = pow(c, 1 << m - i - 1, p)
        x = x * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
    return x

def order(a, n):
    value = carmichael(n)
    for p, _ in groups(value):
        while value % p == 0 and pow(a, value // p, n) == 1:
            value //= p
    return value

def linear_smallest(a, b, m):
    g = math.gcd(a, m)
    if b % g:
        return None
    mod = m // g
    return b // g * pow(a // g, -1, mod) % mod if mod > 1 else 0

def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    p, q = d[:2]
    out = []
    for a in d[2:]:
        x = tonelli(a, p)
        out.append(str(-1 if x is None else min(x, p - x)))
    print('\n'.join(out))
if __name__ == '__main__':
    main()
