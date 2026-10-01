#include <bits/stdc++.h>
using namespace std;

// S(k) = sum_{i<k} r^i i^d.  For r = 1, S is a polynomial of degree d+1 in k.
// For r != 1, S(k) = r^k G(k) + c with deg G <= d (sum by parts).  Compute
// S(0..d+1) directly; the (d+1)-th finite difference of G vanishes, which
// determines c, and Lagrange interpolation evaluates G at n mod p.

typedef long long ll;
const ll MOD = 998244353;

ll power(ll b, ll e) {
    ll r = 1;
    b %= MOD;
    if (b < 0) b += MOD;
    for (; e; e >>= 1, b = b * b % MOD)
        if (e & 1) r = r * b % MOD;
    return r;
}

vector<ll> fact, invFact;

ll interpolate(const vector<ll>& values, ll x) {
    int k = values.size();
    x %= MOD;
    vector<ll> pre(k + 1, 1), suf(k + 1, 1);
    for (int i = 0; i < k; i++) pre[i + 1] = pre[i] * ((x - i) % MOD + MOD) % MOD;
    for (int i = k - 1; i >= 0; i--) suf[i] = suf[i + 1] * ((x - i) % MOD + MOD) % MOD;
    ll total = 0;
    for (int i = 0; i < k; i++) {
        ll term = values[i] * pre[i] % MOD * suf[i + 1] % MOD * invFact[i] % MOD * invFact[k - 1 - i] % MOD;
        total = ((k - 1 - i) & 1) ? (total - term + MOD) % MOD : (total + term) % MOD;
    }
    return total;
}

int main() {
    ll n, r;
    int d;
    cin >> n >> r >> d;
    r %= MOD;
    if (n == 0) {
        cout << 0 << '\n';
        return 0;
    }
    if (r == 0) {
        cout << (d == 0 ? 1 : 0) << '\n';  // only i = 0 survives, 0^0 = 1
        return 0;
    }
    int m = d + 2;
    vector<ll> pw(m + 1, 0);
    pw[0] = d == 0 ? 1 : 0;
    if (m >= 1) pw[1] = 1;
    vector<int> primes;
    vector<char> composite(m + 1, 0);
    for (int i = 2; i <= m; i++) {
        if (!composite[i]) {
            primes.push_back(i);
            pw[i] = power(i, d);
        }
        for (int p : primes) {
            if ((ll)i * p > m) break;
            composite[i * p] = 1;
            pw[i * p] = pw[i] * pw[p] % MOD;
            if (i % p == 0) break;
        }
    }
    vector<ll> S(m + 1, 0);
    ll rp = 1;
    for (int i = 0; i < m; i++) {
        S[i + 1] = (S[i] + rp * pw[i]) % MOD;
        rp = rp * r % MOD;
    }
    fact.assign(m + 2, 1);
    invFact.assign(m + 2, 1);
    for (int i = 1; i < m + 2; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[m + 1] = power(fact[m + 1], MOD - 2);
    for (int i = m + 1; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    if (r == 1) {
        cout << interpolate(vector<ll>(S.begin(), S.begin() + d + 2), n) << '\n';
        return 0;
    }
    ll rInv = power(r, MOD - 2);
    vector<ll> t(d + 2);
    ll rk = 1;
    for (int i = 0; i < d + 2; i++) {
        t[i] = S[i] * rk % MOD;
        rk = rk * rInv % MOD;
    }
    ll num = 0;
    for (int i = 0; i < d + 2; i++) {
        ll w = fact[d + 1] * invFact[i] % MOD * invFact[d + 1 - i] % MOD * t[i] % MOD;
        num = ((d + 1 - i) & 1) ? (num - w + MOD) % MOD : (num + w) % MOD;
    }
    ll c = num * power(power((rInv - 1 + MOD) % MOD, d + 1), MOD - 2) % MOD;
    vector<ll> G(d + 1);
    rk = 1;
    for (int i = 0; i <= d; i++) {
        G[i] = ((t[i] - c * rk) % MOD + MOD) % MOD;
        rk = rk * rInv % MOD;
    }
    cout << (power(r, n % (MOD - 1)) * interpolate(G, n) + c) % MOD << '\n';
}
