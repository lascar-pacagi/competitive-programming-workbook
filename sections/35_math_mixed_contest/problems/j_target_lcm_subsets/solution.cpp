#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    cin >> n >> target;
    vector<int> values(n);
    for (int& value : values)
        cin >> value;

    vector<pair<int, int>> factors;
    int remaining = target;
    for (int prime = 2; 1LL * prime * prime <= remaining; ++prime) {
        if (remaining % prime)
            continue;
        int exponent = 0;
        while (remaining % prime == 0) {
            remaining /= prime;
            ++exponent;
        }
        factors.push_back({prime, exponent});
    }
    if (remaining > 1)
        factors.push_back({remaining, 1});

    int mask_count = 1 << factors.size();
    vector<int> frequency(mask_count);
    for (int value : values) {
        if (target % value)
            continue;
        int mask = 0;
        int copy = value;
        for (int bit = 0; bit < static_cast<int>(factors.size()); ++bit) {
            auto [prime, target_exponent] = factors[bit];
            int exponent = 0;
            while (copy % prime == 0) {
                copy /= prime;
                ++exponent;
            }
            if (exponent == target_exponent)
                mask |= 1 << bit;
        }
        ++frequency[mask];
    }

    vector<int> dp(mask_count);
    dp[0] = 1;
    for (int type = 0; type < mask_count; ++type) {
        if (!frequency[type])
            continue;
        int nonempty_ways = 1;
        for (int i = 0; i < frequency[type]; ++i)
            nonempty_ways = 2LL * nonempty_ways % MOD;
        nonempty_ways = (nonempty_ways - 1 + MOD) % MOD;

        vector<int> next = dp;
        for (int mask = 0; mask < mask_count; ++mask) {
            int combined = mask | type;
            next[combined] = (
                next[combined] + 1LL * dp[mask] * nonempty_ways
            ) % MOD;
        }
        dp.swap(next);
    }

    int full_mask = mask_count - 1;
    int answer = dp[full_mask];
    if (full_mask == 0)
        answer = (answer - 1 + MOD) % MOD;
    cout << answer << '\n';
}
