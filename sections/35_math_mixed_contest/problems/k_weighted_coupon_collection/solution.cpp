#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
const int64 MOD = 1'000'000'007;

int64 power(int64 base, int64 exponent) {
    int64 result = 1;
    while (exponent) {
        if (exponent & 1)
            result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int64> weight(n);
    int64 total = 0;
    for (int64& value : weight) {
        cin >> value;
        total += value;
    }

    int subset_count = 1 << n;
    vector<int64> subset_sum(subset_count);
    int64 answer = 0;
    for (int mask = 1; mask < subset_count; ++mask) {
        int bit = __builtin_ctz(mask);
        subset_sum[mask] = subset_sum[mask ^ (1 << bit)] + weight[bit];
        int64 term = total * power(subset_sum[mask], MOD - 2) % MOD;
        if (__builtin_popcount(static_cast<unsigned>(mask)) & 1)
            answer = (answer + term) % MOD;
        else
            answer = (answer - term + MOD) % MOD;
    }

    cout << answer << '\n';
}
