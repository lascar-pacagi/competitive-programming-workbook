#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using int128 = __int128_t;

string to_string128(int128 value) {
    if (value == 0) return "0";
    bool negative = value < 0;
    if (negative) value = -value;
    string result;
    while (value) {
        result.push_back(char('0' + value % 10));
        value /= 10;
    }
    if (negative) result.push_back('-');
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int64 low, high;
    cin >> n >> low >> high;

    // Each pair is (breakpoint, multiplicity) in the derivative summary.
    priority_queue<pair<int64, int64>> breakpoints;
    int128 answer = 0;

    for (int i = 0; i < n; ++i) {
        int64 target, weight;
        cin >> target >> weight;

        int64 x = clamp(target, low, high);
        answer += int128(weight) * llabs(target - x);

        breakpoints.push({x, 2 * weight});
        int64 remove = weight;
        while (remove > 0) {
            auto [position, mass] = breakpoints.top();
            breakpoints.pop();
            int64 take = min(remove, mass);
            answer += int128(position - x) * take;
            remove -= take;
            mass -= take;
            if (mass) breakpoints.push({position, mass});
        }
    }

    cout << to_string128(answer) << '\n';
}
