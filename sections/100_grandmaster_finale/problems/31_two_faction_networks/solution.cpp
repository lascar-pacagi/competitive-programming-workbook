#include <bits/stdc++.h>
using namespace std;

// A 2-coloured graph puts every vertex in one of two factions and only joins
// vertices of different factions: b_n = sum_k C(n,k) 2^{k(n-k)}.  Its
// exponential generating function B satisfies log B = EGF of connected
// 2-coloured graphs, and a connected bipartite graph has exactly two
// colourings.  With s = sqrt(2) (it exists modulo 998244353), the identity
// k(n-k) = (n^2 - k^2 - (n-k)^2)/2 turns all b_n into one convolution.

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

int main() {
    int N;
    cin >> N;
    long long zeta = power(G, (MOD - 1) / 8);  // primitive 8th root of unity
    long long s = (zeta + power(zeta, MOD - 2)) % MOD;  // s^2 = 2
    long long sInv = power(s, MOD - 2);
    vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[N] = power(fact[N], MOD - 2);
    for (int i = N; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    vector<long long> a(N + 1);
    for (long long k = 0; k <= N; k++) a[k] = power(sInv, k * k % (MOD - 1)) * invFact[k] % MOD;
    vector<long long> B = multiply(a, a, N + 1);
    for (long long n = 0; n <= N; n++) B[n] = B[n] * power(s, n * n % (MOD - 1)) % MOD;
    vector<long long> C = logarithm(B, N + 1);
    long long inv2 = (MOD + 1) / 2;
    string out;
    for (int n = 1; n <= N; n++) {
        out += to_string(C[n] * fact[n] % MOD * inv2 % MOD);
        out += n < N ? ' ' : '\n';
    }
    cout << out;
}
