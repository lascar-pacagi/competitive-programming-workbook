#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> values(n);
    int maximum = 0;
    for (int& value : values) {
        cin >> value;
        maximum = max(maximum, value);
    }

    vector<int> frequency(maximum + 1);
    for (int value : values)
        ++frequency[value];

    vector<int> powers(n + 1, 1);
    for (int i = 1; i <= n; ++i)
        powers[i] = 2LL * powers[i - 1] % MOD;

    vector<int> exact(maximum + 1);
    for (int divisor = maximum; divisor >= 1; --divisor) {
        int divisible_count = 0;
        long long remove = 0;
        for (int multiple = divisor; multiple <= maximum; multiple += divisor) {
            divisible_count += frequency[multiple];
            if (multiple != divisor)
                remove += exact[multiple];
        }
        exact[divisor] = (powers[divisible_count] - 1 - remove) % MOD;
        if (exact[divisor] < 0)
            exact[divisor] += MOD;
    }

    cout << exact[1] << '\n';
}
