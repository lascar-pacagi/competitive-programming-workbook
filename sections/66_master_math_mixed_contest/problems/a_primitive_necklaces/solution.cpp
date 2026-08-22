#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int64 MOD = 1'000'000'007;

int64 power(int64 base, int64 exponent) {
    int64 result = 1;
    while (exponent) {
        if (exponent & 1) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    vector<pair<int, int64>> queries(q);
    int maximum = 1;
    for (auto &[n, colors] : queries) {
        cin >> n >> colors;
        maximum = max(maximum, n);
    }

    vector<int> mu(maximum + 1), primes;
    vector<bool> composite(maximum + 1);
    mu[1] = 1;
    for (int value = 2; value <= maximum; ++value) {
        if (!composite[value]) primes.push_back(value), mu[value] = -1;
        for (int prime : primes) {
            if (1LL * value * prime > maximum) break;
            composite[value * prime] = true;
            if (value % prime == 0) {
                mu[value * prime] = 0;
                break;
            }
            mu[value * prime] = -mu[value];
        }
    }

    for (auto [n, colors] : queries) {
        int64 primitive_words = 0;
        for (int divisor = 1; 1LL * divisor * divisor <= n; ++divisor) {
            if (n % divisor) continue;
            primitive_words += mu[divisor] * power(colors, n / divisor);
            int other = n / divisor;
            if (other != divisor)
                primitive_words += mu[other] * power(colors, n / other);
            primitive_words %= MOD;
        }
        if (primitive_words < 0) primitive_words += MOD;
        cout << primitive_words * power(n, MOD - 2) % MOD << '\n';
    }
}
