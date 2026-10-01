#include <bits/stdc++.h>
using namespace std;

// D(h)(n) = Omega(n) h(n) (prime factors counted with multiplicity) is a
// derivation of Dirichlet convolution: D(a*b) = D(a)*b + a*D(b).  For
// g = f^k this gives f * D(g) = k g * D(f), and comparing values at n:
//   Omega(n) g(n) = sum over d | n, d < n of g(d) f(n/d) (k Omega(n/d) - Omega(d)).
// Push each finished g(d) to its multiples: O(N log N), k only mod p.

typedef long long ll;
const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1;
    for (b %= MOD; e; e >>= 1, b = b * b % MOD)
        if (e & 1) r = r * b % MOD;
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    ll k;
    cin >> N >> k;
    k %= MOD;
    vector<ll> f(N + 1, 0);
    for (int i = 1; i <= N; i++) cin >> f[i], f[i] %= MOD;
    vector<int> omega(N + 1, 0);
    for (int p = 2; p <= N; p++)
        if (!omega[p])
            for (ll pk = p; pk <= N; pk *= p)
                for (ll m = pk; m <= N; m += pk) omega[m]++;
    vector<ll> inv(64, 1);
    for (int i = 1; i < 64; i++) inv[i] = power(i, MOD - 2);
    vector<ll> acc(N + 1, 0), g(N + 1, 0);
    g[1] = 1;
    for (int d = 1; d <= N; d++) {
        if (d > 1) g[d] = acc[d] % MOD * inv[omega[d]] % MOD;
        if (!g[d]) continue;
        for (ll n = 2LL * d, m = 2; n <= N; n += d, m++) {
            ll coef = (k * omega[m] - omega[d] + MOD) % MOD;
            acc[n] = (acc[n] + g[d] * f[m] % MOD * coef) % MOD;
        }
    }
    string out;
    for (int n = 1; n <= N; n++) {
        out += to_string(g[n]);
        out += n < N ? ' ' : '\n';
    }
    cout << out;
}
