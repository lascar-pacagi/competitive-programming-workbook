#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
constexpr int64 MOD = 1'000'000'007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, maximum;
    if (!(cin >> n >> maximum)) return 0;
    vector<int> frequency(maximum + 1);
    for (int i = 0, value; i < n; ++i) {
        cin >> value;
        ++frequency[value];
    }

    vector<int> inside(maximum + 1);
    for (int divisor = 1; divisor <= maximum; ++divisor)
        for (int multiple = divisor; multiple <= maximum; multiple += divisor)
            inside[multiple] += frequency[divisor];

    vector<int64> exact(maximum + 1);
    for (int value = 1; value <= maximum; ++value)
        exact[value] = 1LL * inside[value] * (inside[value] - 1) / 2 % MOD;
    for (int divisor = 1; divisor <= maximum; ++divisor)
        for (int multiple = 2 * divisor; multiple <= maximum; multiple += divisor) {
            exact[multiple] -= exact[divisor];
            if (exact[multiple] < 0) exact[multiple] += MOD;
        }

    for (int value = 1; value <= maximum; ++value)
        cout << exact[value] << (value == maximum ? '\n' : ' ');
}
