#include <bits/stdc++.h>
using namespace std;

// The Pisano period of m is the order of F = [[1,1],[1,0]] modulo m, and by
// CRT it is the lcm of the orders modulo each prime power p^e.  Over F_p the
// roots of x^2 - x - 1 lie in F_p (p = +-1 mod 5), in F_{p^2} with the
// Frobenius swapping them (p = +-2 mod 5), or coincide (p = 5); this makes
// p^(e-1) * (p-1), p^(e-1) * 2(p+1), or 5^(e-1) * 20 a multiple of the order.
// Factor that multiple with Pollard's rho and strip prime factors while F to
// the reduced power is still the identity.

typedef unsigned long long u64;
typedef __uint128_t u128;

u64 mulmod(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
u64 powmod(u64 b, u64 e, u64 m) {
    u64 r = 1 % m;
    for (b %= m; e; e >>= 1, b = mulmod(b, b, m))
        if (e & 1) r = mulmod(r, b, m);
    return r;
}

bool isPrime(u64 n) {
    if (n < 2) return false;
    for (u64 p : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37})
        if (n % p == 0) return n == p;
    u64 d = n - 1;
    int s = 0;
    while (d % 2 == 0) d /= 2, s++;
    for (u64 a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL, 9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        u64 x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int i = 1; i < s && composite; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) composite = false;
        }
        if (composite) return false;
    }
    return true;
}

mt19937_64 rng(20261001);

u64 rho(u64 n) {
    if (n % 2 == 0) return 2;
    while (true) {
        u64 c = rng() % (n - 1) + 1, y = rng() % n, g = 1, q = 1, x = y, ys = y;
        auto f = [&](u64 v) { return (mulmod(v, v, n) + c) % n; };
        for (u64 r = 1; g == 1; r <<= 1) {
            x = y;
            for (u64 i = 0; i < r; i++) y = f(y);
            for (u64 k = 0; k < r && g == 1; k += 128) {
                ys = y;
                for (u64 i = 0; i < min<u64>(128, r - k); i++) {
                    y = f(y);
                    q = mulmod(q, x > y ? x - y : y - x, n);
                }
                g = __gcd(q, n);
            }
        }
        if (g == n) {
            g = 1;
            while (g == 1) {
                ys = f(ys);
                g = __gcd(x > ys ? x - ys : ys - x, n);
            }
        }
        if (g != n) return g;
    }
}

void factor(u64 n, map<u64, int>& out) {
    if (n == 1) return;
    if (isPrime(n)) {
        out[n]++;
        return;
    }
    for (u64 p : {2, 3, 5, 7, 11, 13})
        if (n % p == 0) {
            out[p]++;
            factor(n / p, out);
            return;
        }
    u64 d = rho(n);
    factor(d, out);
    factor(n / d, out);
}

typedef array<u64, 4> Mat;
Mat matmul(const Mat& x, const Mat& y, u64 m) {
    return {(mulmod(x[0], y[0], m) + mulmod(x[1], y[2], m)) % m, (mulmod(x[0], y[1], m) + mulmod(x[1], y[3], m)) % m,
            (mulmod(x[2], y[0], m) + mulmod(x[3], y[2], m)) % m, (mulmod(x[2], y[1], m) + mulmod(x[3], y[3], m)) % m};
}
bool isIdentityPower(u64 e, u64 m) {
    Mat r = {1 % m, 0, 0, 1 % m}, b = {1 % m, 1 % m, 1 % m, 0};
    for (; e; e >>= 1, b = matmul(b, b, m))
        if (e & 1) r = matmul(r, b, m);
    return r == Mat{1 % m, 0, 0, 1 % m};
}

u64 periodPrimePower(u64 p, int e) {
    u64 mod = 1, pk = 1;
    for (int i = 0; i < e; i++) mod *= p;
    for (int i = 1; i < e; i++) pk *= p;
    u64 base = p == 5 ? 20 : (p % 5 == 1 || p % 5 == 4) ? p - 1 : 2 * (p + 1);
    map<u64, int> fac;
    factor(base, fac);
    if (e > 1) fac[p] += e - 1;
    u64 L = base * pk;
    for (auto& [r, cnt] : fac)
        while (L % r == 0 && isIdentityPower(L / r, mod)) L /= r;
    return L;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        u64 m;
        cin >> m;
        map<u64, int> fac;
        factor(m, fac);
        u64 answer = 1;
        for (auto& [p, e] : fac) {
            u64 L = periodPrimePower(p, e);
            answer = answer / __gcd(answer, L) * L;
        }
        cout << answer << '\n';
    }
}
