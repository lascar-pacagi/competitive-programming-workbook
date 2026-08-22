#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int64 MOD = 1'000'000'007;

int64 mod_pow(int64 base, long long exponent) {
    int64 result = 1;
    while (exponent > 0) {
        if (exponent & 1) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<int> frequency(1, 0);
    int maximum = 0;
    vector<int> values(n);
    for (int &value : values) {
        cin >> value;
        maximum = max(maximum, value);
    }
    frequency.resize(maximum + 1);
    for (int value : values) ++frequency[value];

    vector<int> divisible(maximum + 1);
    for (int d = 1; d <= maximum; ++d)
        for (int multiple = d; multiple <= maximum; multiple += d)
            divisible[d] += frequency[multiple];

    // jordan[d] is defined by x^k = sum_{d|x} jordan[d].
    vector<int64> jordan(maximum + 1);
    for (int d = 1; d <= maximum; ++d) jordan[d] = mod_pow(d, k);
    for (int d = 1; d <= maximum; ++d)
        for (int multiple = 2 * d; multiple <= maximum; multiple += d) {
            jordan[multiple] -= jordan[d];
            if (jordan[multiple] < 0) jordan[multiple] += MOD;
        }

    int64 answer = 0;
    for (int d = 1; d <= maximum; ++d) {
        int64 pairs = 1LL * divisible[d] * (divisible[d] - 1) / 2 % MOD;
        answer = (answer + jordan[d] * pairs) % MOD;
    }
    cout << answer << '\n';
}
