#include <bits/stdc++.h>
using namespace std;

// Min_25 sieve.  Phase one (Lucy DP) finds, for every value v = N / i, the
// number and the sum of primes up to v; since f(p) = p xor 1 equals p - 1 for
// odd p and 3 for p = 2, these give the prime part of the answer.  Phase two
// adds composites by their least prime factor, recursing only while p^2 <= v.

typedef long long ll;
const ll MOD = 1000000007;

ll N, sq;
vector<ll> primes, vals, gCount, gSum;
vector<int> idxSmall, idxLarge;

int index(ll v) { return v <= sq ? idxSmall[v] : idxLarge[N / v]; }

ll primeF(ll v) {  // sum of f(p) over primes p <= v, modulo MOD
    if (v < 2) return 0;
    int i = index(v);
    return ((gSum[i] - gCount[i] + 2) % MOD + MOD) % MOD;
}

ll S(ll v, int j) {  // sum of f(i), 2 <= i <= v, least prime factor > primes[j-1]
    ll pj = j ? primes[j - 1] : 1;
    if (v < 2 || pj >= v) return 0;
    ll result = (primeF(v) - primeF(pj) + MOD) % MOD;
    for (int k = j; k < (int)primes.size() && primes[k] * primes[k] <= v; k++) {
        ll p = primes[k];
        ll pe = p;
        for (int e = 1; pe * p <= v; e++, pe *= p) {
            ll fe = (p ^ e) % MOD, fe1 = (p ^ (e + 1)) % MOD;
            result = (result + fe * S(v / pe, k + 1) + fe1) % MOD;
        }
    }
    return result;
}

int main() {
    cin >> N;
    sq = sqrtl((long double)N);
    while (sq * sq > N) sq--;
    while ((sq + 1) * (sq + 1) <= N) sq++;
    vector<char> composite(sq + 1, 0);
    for (ll i = 2; i <= sq; i++) {
        if (composite[i]) continue;
        primes.push_back(i);
        for (ll j = i * i; j <= sq; j += i) composite[j] = 1;
    }
    idxSmall.assign(sq + 2, 0);
    idxLarge.assign(sq + 2, 0);
    for (ll i = 1; i <= N; i = N / (N / i) + 1) {
        ll v = N / i;
        int id = vals.size();
        vals.push_back(v);
        if (v <= sq) idxSmall[v] = id;
        else idxLarge[N / v] = id;
        gCount.push_back((v - 1) % MOD);
        // 2 + 3 + ... + v = v(v+1)/2 - 1
        __int128 t = (__int128)v * (v + 1) / 2 - 1;
        gSum.push_back((ll)(t % MOD));
    }
    for (ll p : primes) {
        ll pc = gCount[index(p - 1)], ps = gSum[index(p - 1)];
        for (size_t i = 0; i < vals.size() && vals[i] >= p * p; i++) {
            int k = index(vals[i] / p);
            gCount[i] = ((gCount[i] - (gCount[k] - pc)) % MOD + MOD) % MOD;
            gSum[i] = ((gSum[i] - p % MOD * ((gSum[k] - ps + MOD) % MOD)) % MOD + MOD) % MOD;
        }
    }
    cout << (S(N, 0) + 1) % MOD << '\n';
}
