#include <bits/stdc++.h>
using namespace std;

// C(n, k) mod p^e: write n! = p^{v_p(n!)} * u(n), where u(n) (the factorial
// with every factor p removed) satisfies the generalized Lucas recursion
// u(n) = full^{floor(n/p^e)} * pre[n mod p^e] * u(floor(n/p)), with pre[j] the
// product of integers <= j coprime to p.  Combine the prime powers by CRT.

typedef long long ll;

ll egcdInverse(ll a, ll m) {  // inverse of a modulo m, gcd(a, m) = 1
    ll old_r = a % m, r = m, old_s = 1, s = 0;
    while (r) {
        ll q = old_r / r;
        tie(old_r, r) = make_pair(r, old_r - q * r);
        tie(old_s, s) = make_pair(s, old_s - q * s);
    }
    return (old_s % m + m) % m;
}

struct PrimePower {
    ll p, e, pe, full;
    vector<ll> pre;
    PrimePower(ll p, ll e) : p(p), e(e) {
        pe = 1;
        for (int i = 0; i < e; i++) pe *= p;
        pre.assign(pe + 1, 1);
        for (ll i = 1; i <= pe; i++) pre[i] = i % p ? pre[i - 1] * i % pe : pre[i - 1];
        full = pre[pe];
    }
    ll unitFactorial(ll x) const {
        ll result = 1;
        while (x) {
            ll qq = x / pe, r = x % pe;
            if (full != 1 && (qq & 1)) result = result * full % pe;
            result = result * pre[r] % pe;
            x /= p;
        }
        return result;
    }
    ll legendre(ll x) const {
        ll v = 0;
        while (x) x /= p, v += x;
        return v;
    }
    ll binom(ll n, ll k) const {
        ll v = legendre(n) - legendre(k) - legendre(n - k);
        if (v >= e) return 0;
        ll top = unitFactorial(n), bottom = unitFactorial(k) * unitFactorial(n - k) % pe;
        ll r = top * egcdInverse(bottom, pe) % pe;
        for (int i = 0; i < v; i++) r = r * p % pe;
        return r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll m;
    int q;
    cin >> m >> q;
    vector<PrimePower> parts;
    {
        ll x = m;
        for (ll p = 2; p * p <= x; p++)
            if (x % p == 0) {
                int e = 0;
                while (x % p == 0) x /= p, e++;
                parts.emplace_back(p, e);
            }
        if (x > 1) parts.emplace_back(x, 1);
    }
    vector<ll> coef;
    for (auto& part : parts) {
        ll Mi = m / part.pe;
        coef.push_back(part.pe > 1 ? Mi * egcdInverse(Mi % part.pe, part.pe) % m : 0);
    }
    string out;
    while (q--) {
        ll n, k;
        cin >> n >> k;
        ll total = 0;
        if (k <= n && m > 1)
            for (size_t i = 0; i < parts.size(); i++)
                total = (total + (__int128)parts[i].binom(n, k) * coef[i]) % m;
        out += to_string(total) + '\n';
    }
    cout << out;
}
