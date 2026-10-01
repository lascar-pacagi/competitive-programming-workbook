#include <bits/stdc++.h>
using namespace std;

// Give an edge of weight w the formal weight x^w.  By the matrix-tree theorem
// any cofactor of the Laplacian is F(x) = sum_T x^{weight(T)}, a polynomial of
// degree at most D = (n-1)K.  Evaluate F at x = 0..D by Gaussian elimination
// modulo the prime, then recover its coefficients by Lagrange interpolation.

const long long MOD = 998244353;

long long power(long long b, long long e) {
    long long r = 1;
    b %= MOD;
    if (b < 0) b += MOD;
    while (e) {
        if (e & 1) r = r * b % MOD;
        b = b * b % MOD;
        e >>= 1;
    }
    return r;
}

long long determinant(vector<vector<long long>> a) {
    int n = a.size();
    long long det = 1;
    for (int c = 0; c < n; c++) {
        int pivot = -1;
        for (int r = c; r < n; r++)
            if (a[r][c]) {
                pivot = r;
                break;
            }
        if (pivot < 0) return 0;
        if (pivot != c) {
            swap(a[pivot], a[c]);
            det = (MOD - det) % MOD;
        }
        det = det * a[c][c] % MOD;
        long long inv = power(a[c][c], MOD - 2);
        for (int r = c + 1; r < n; r++) {
            if (!a[r][c]) continue;
            long long f = a[r][c] * inv % MOD;
            for (int k = c; k < n; k++) a[r][k] = (a[r][k] - f * a[c][k]) % MOD;
            for (int k = c; k < n; k++)
                if (a[r][k] < 0) a[r][k] += MOD;
        }
    }
    return det;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, K;
    cin >> n >> m >> K;
    vector<array<int, 3>> edges(m);
    for (auto& [u, v, w] : edges) {
        cin >> u >> v >> w;
        --u;
        --v;
    }
    int D = (n - 1) * K;
    vector<long long> values(D + 1);
    for (int x = 0; x <= D; x++) {
        vector<long long> pw(K + 1, 1);
        for (int i = 1; i <= K; i++) pw[i] = pw[i - 1] * x % MOD;
        vector<vector<long long>> lap(n - 1, vector<long long>(n - 1, 0));
        for (auto [u, v, w] : edges) {
            if (u == v) continue;
            long long t = pw[w];
            if (u < n - 1) lap[u][u] = (lap[u][u] + t) % MOD;
            if (v < n - 1) lap[v][v] = (lap[v][v] + t) % MOD;
            if (u < n - 1 && v < n - 1) {
                lap[u][v] = (lap[u][v] - t + MOD) % MOD;
                lap[v][u] = (lap[v][u] - t + MOD) % MOD;
            }
        }
        values[x] = determinant(lap);
    }

    // Interpolate through (i, values[i]), i = 0..D.
    vector<long long> master(D + 2, 0);  // prod (x - i)
    master[0] = 1;
    for (int i = 0; i <= D; i++) {
        for (int k = i + 1; k >= 1; k--) master[k] = (master[k - 1] - master[k] * i) % MOD;
        master[0] = master[0] * (MOD - i) % MOD;
    }
    for (auto& c : master) c = (c % MOD + MOD) % MOD;
    vector<long long> fact(D + 1, 1);
    for (int i = 1; i <= D; i++) fact[i] = fact[i - 1] * i % MOD;
    vector<long long> coef(D + 1, 0), quotient(D + 1);
    for (int i = 0; i <= D; i++) {
        if (!values[i]) continue;
        long long denom = fact[i] * fact[D - i] % MOD;
        if ((D - i) % 2) denom = (MOD - denom) % MOD;
        long long scale = values[i] * power(denom, MOD - 2) % MOD;
        // quotient = master / (x - i), synthetic division from the top.
        long long carry = 0;
        for (int k = D + 1; k >= 1; k--) {
            carry = (master[k] + carry * i) % MOD;
            quotient[k - 1] = carry;
        }
        for (int k = 0; k <= D; k++) coef[k] = (coef[k] + scale * quotient[k]) % MOD;
    }
    string out;
    for (int k = 0; k <= D; k++) {
        out += to_string(coef[k]);
        out += k < D ? ' ' : '\n';
    }
    cout << out;
}
