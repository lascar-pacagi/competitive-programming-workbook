#include <bits/stdc++.h>
using namespace std;

// A plane tree is a root with s ordered subtrees, weighted by c_s, so its
// generating function satisfies T = x * phi(T) with phi(z) = sum c_s z^s.
// Newton's method doubles the number of correct coefficients each round:
// T <- T - (T - x phi(T)) / (1 - x phi'(T)), with phi(T), phi'(T) by Horner.

const long long MOD = 998244353, G = 3;

long long power(long long b, long long e) {
    long long r = 1;
    b %= MOD;
    if (b < 0) b += MOD;
    for (; e; e >>= 1, b = b * b % MOD)
        if (e & 1) r = r * b % MOD;
    return r;
}

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long w = power(G, (MOD - 1) / len);
        if (invert) w = power(w, MOD - 2);
        vector<long long> ws(len / 2, 1);
        for (int k = 1; k < len / 2; k++) ws[k] = ws[k - 1] * w % MOD;
        for (int i = 0; i < n; i += len)
            for (int k = 0; k < len / 2; k++) {
                long long u = a[i + k], v = a[i + k + len / 2] * ws[k] % MOD;
                a[i + k] = u + v < MOD ? u + v : u + v - MOD;
                a[i + k + len / 2] = u - v >= 0 ? u - v : u - v + MOD;
            }
    }
    if (invert) {
        long long inv = power(n, MOD - 2);
        for (auto& x : a) x = x * inv % MOD;
    }
}

// Product truncated to `limit` terms (limit < 0: full product).
vector<long long> multiply(vector<long long> a, vector<long long> b, int limit = -1) {
    if (a.empty() || b.empty()) return {};
    if (limit >= 0) {
        if ((int)a.size() > limit) a.resize(limit);
        if ((int)b.size() > limit) b.resize(limit);
    }
    int need = a.size() + b.size() - 1, n = 1;
    while (n < need) n <<= 1;
    a.resize(n);
    b.resize(n);
    ntt(a, false);
    ntt(b, false);
    for (int i = 0; i < n; i++) a[i] = a[i] * b[i] % MOD;
    ntt(a, true);
    a.resize(limit >= 0 ? min(need, limit) : need);
    return a;
}

vector<long long> inverse(const vector<long long>& a, int n) {
    vector<long long> g = {power(a[0], MOD - 2)};
    for (int m = 1; m < n;) {
        m *= 2;
        vector<long long> t = multiply(vector<long long>(a.begin(), a.begin() + min<int>(m, a.size())), g, m);
        for (auto& x : t) x = (MOD - x) % MOD;
        t[0] = (t[0] + 2) % MOD;
        g = multiply(g, t, m);
    }
    g.resize(n);
    return g;
}

vector<long long> logarithm(const vector<long long>& a, int n) {
    vector<long long> da;
    for (int i = 1; i < min<int>(a.size(), n); i++) da.push_back(a[i] * i % MOD);
    vector<long long> q = multiply(da, inverse(a, n), n - 1), out(n, 0);
    q.resize(max(n - 1, 0));
    vector<long long> inv(n + 1, 1);
    for (int i = 2; i <= n; i++) inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD;
    for (int i = 1; i < n; i++) out[i] = q[i - 1] * inv[i] % MOD;
    return out;
}

vector<long long> exponential(const vector<long long>& a, int n) {
    vector<long long> g = {1};
    for (int m = 1; m < n;) {
        m *= 2;
        vector<long long> gm = g;
        gm.resize(m, 0);
        vector<long long> lg = logarithm(gm, m), t(m);
        for (int i = 0; i < m; i++) t[i] = ((i < (int)a.size() ? a[i] : 0) - lg[i] + MOD) % MOD;
        t[0] = (t[0] + 1) % MOD;
        g = multiply(g, t, m);
    }
    g.resize(n);
    return g;
}

vector<long long> horner(const vector<long long>& coef, const vector<long long>& T, int m) {
    vector<long long> acc = {coef.back()};
    for (int s = (int)coef.size() - 2; s >= 0; s--) {
        acc = multiply(acc, T, m);
        if (acc.empty()) acc = {0};
        acc[0] = (acc[0] + coef[s]) % MOD;
    }
    acc.resize(m, 0);
    return acc;
}

int main() {
    int N, D;
    cin >> N >> D;
    vector<long long> c(D + 1), dc;
    for (auto& x : c) cin >> x, x %= MOD;
    for (int s = 1; s <= D; s++) dc.push_back(s * c[s] % MOD);
    int total = N + 1;
    vector<long long> T = {0, c[0]};
    for (int m = 2; m < total;) {
        m = min(2 * m, total);
        T.resize(m, 0);
        vector<long long> P = horner(c, T, m), Q = dc.empty() ? vector<long long>(m, 0) : horner(dc, T, m);
        vector<long long> F(m), Fp(m);
        for (int i = 0; i < m; i++) {
            F[i] = (T[i] - (i ? P[i - 1] : 0) + MOD) % MOD;
            Fp[i] = ((i == 0 ? 1 : 0) - (i ? Q[i - 1] : 0) + MOD) % MOD;
        }
        vector<long long> step = multiply(F, inverse(Fp, m), m);
        step.resize(m, 0);
        for (int i = 0; i < m; i++) T[i] = (T[i] - step[i] + MOD) % MOD;
    }
    T.resize(total, 0);
    string out;
    for (int n = 1; n <= N; n++) {
        out += to_string(T[n]);
        out += n < N ? ' ' : '\n';
    }
    cout << out;
}
