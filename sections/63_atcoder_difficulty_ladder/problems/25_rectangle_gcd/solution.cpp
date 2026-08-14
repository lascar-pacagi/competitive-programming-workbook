#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007LL;

long long mod_pow(long long base, long long exponent) {
    long long result = 1;
    while (exponent > 0) {
        if (exponent & 1LL) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1LL;
    }
    return result;
}

long long choose(int n, int r) {
    r = min(r, n - r);
    long long result = 1;
    for (int i = 1; i <= r; i++) result = result * (n - r + i) / i;
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int k;
    if (!(cin >> n >> k)) return 0;

    long long answer = 0;
    for (int missing = 0; missing <= k; missing++) {
        long long term = choose(k, missing) * mod_pow(k - missing, n) % MOD;
        if (missing % 2 == 0) answer += term;
        else answer -= term;
        answer %= MOD;
    }
    cout << (answer + MOD) % MOD << '\n';
    return 0;
}
