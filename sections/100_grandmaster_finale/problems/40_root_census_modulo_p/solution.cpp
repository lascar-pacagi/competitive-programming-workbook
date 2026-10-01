#include <bits/stdc++.h>
using namespace std;

// x^p - x = prod over a in F_p of (x - a), so gcd(f, x^p - x) is the product
// of (x - a) over the distinct roots a of f, and its degree is the answer.
// Compute h = x^p mod f by square-and-multiply; polynomial remainders use a
// precomputed inverse of reversed f (Barrett), so every step is three
// polynomial products.  Products accumulate 128-bit sums lazily.

typedef unsigned long long u64;
typedef __uint128_t u128;
u64 P;

u64 mulmod(u64 a, u64 b) { return (u128)a * b % P; }
u64 powmod(u64 b, u64 e) {
    u64 r = 1;
    for (b %= P; e; e >>= 1, b = mulmod(b, b))
        if (e & 1) r = mulmod(r, b);
    return r;
}
u64 sub(u64 a, u64 b) { return a >= b ? a - b : a + P - b; }

typedef vector<u64> Poly;

// Each product is < 2^120, so 256 of them fit in an unsigned 128-bit sum.
Poly mul(const Poly& a, const Poly& b, size_t limit = SIZE_MAX) {
    if (a.empty() || b.empty()) return {};
    size_t n = min(limit, a.size() + b.size() - 1);
    Poly out(n);
    for (size_t k = 0; k < n; k++) {
        size_t lo = k >= b.size() ? k - b.size() + 1 : 0, hi = min(k, a.size() - 1);
        u128 acc = 0;
        u64 res = 0;
        int cnt = 0;
        for (size_t i = lo; i <= hi; i++) {
            acc += (u128)a[i] * b[k - i];
            if (++cnt == 256) {
                res = (res + (u64)(acc % P)) % P;
                acc = 0;
                cnt = 0;
            }
        }
        out[k] = (res + (u64)(acc % P)) % P;
    }
    return out;
}

Poly seriesInverse(const Poly& a, size_t n) {
    Poly g = {powmod(a[0], P - 2)};
    for (size_t k = 1; k < n;) {
        k *= 2;
        Poly t = mul(Poly(a.begin(), a.begin() + min(k, a.size())), g, k);
        for (auto& x : t) x = x ? P - x : 0;
        t[0] = (t[0] + 2) % P;
        g = mul(g, t, k);
    }
    g.resize(n);
    return g;
}

int main() {
    int d;
    cin >> P >> d;
    Poly f(d + 1);
    for (auto& c : f) cin >> c, c %= P;
    while (!f.empty() && f.back() == 0) f.pop_back();
    if (f.empty()) {
        cout << P << '\n';
        return 0;
    }
    if (f.size() == 1) {
        cout << 0 << '\n';
        return 0;
    }
    u64 leadInv = powmod(f.back(), P - 2);
    for (auto& c : f) c = mulmod(c, leadInv);
    size_t m = f.size() - 1;
    Poly revF(f.rbegin(), f.rend());
    Poly invRev = seriesInverse(revF, max<size_t>(1, m));

    auto reduce = [&](Poly A) {
        while (!A.empty() && A.back() == 0) A.pop_back();
        if (A.size() <= m) {
            A.resize(m, 0);
            return A;
        }
        size_t n = A.size() - 1, qlen = n - m + 1;
        Poly revA(A.rbegin(), A.rbegin() + qlen);
        Poly qRev = mul(revA, Poly(invRev.begin(), invRev.begin() + qlen), qlen);
        qRev.resize(qlen, 0);
        Poly Q(qRev.rbegin(), qRev.rend());
        Poly prod = mul(Q, f, m);
        Poly R(m);
        for (size_t i = 0; i < m; i++) R[i] = sub(A[i], i < prod.size() ? prod[i] : 0);
        return R;
    };

    Poly h(m, 0);
    h[0] = 1;
    for (int bit = 63 - __builtin_clzll(P); bit >= 0; bit--) {
        h = reduce(mul(h, h));
        if (P >> bit & 1) {
            Poly shifted(h.size() + 1, 0);
            copy(h.begin(), h.end(), shifted.begin() + 1);
            h = reduce(shifted);
        }
    }
    Poly g = h;
    if (g.size() < 2) g.resize(2, 0);
    g[1] = sub(g[1], 1);
    Poly a = f, b = g;
    while (!b.empty() && b.back() == 0) b.pop_back();
    while (!b.empty()) {
        u64 invLead = powmod(b.back(), P - 2);
        size_t db = b.size() - 1;
        for (size_t i = a.size(); i-- > db;) {
            u64 c = mulmod(a[i], invLead);
            if (!c) continue;
            size_t shift = i - db;
            for (size_t j = 0; j <= db; j++) a[shift + j] = sub(a[shift + j], mulmod(c, b[j]));
        }
        a.resize(min(a.size(), db));
        while (!a.empty() && a.back() == 0) a.pop_back();
        swap(a, b);
    }
    cout << a.size() - 1 << '\n';
}
