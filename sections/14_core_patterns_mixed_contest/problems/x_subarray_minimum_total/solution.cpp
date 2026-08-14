#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    // (value, number of suffixes for which value is the minimum)
    vector<pair<long long, long long>> stack;
    long long ending_sum = 0;
    long long answer = 0;

    for (int i = 0; i < n; ++i) {
        long long value;
        cin >> value;
        long long ways = 1;

        while (!stack.empty() && stack.back().first >= value) {
            auto [old_value, old_ways] = stack.back();
            stack.pop_back();
            ending_sum -= old_value * old_ways;
            ways += old_ways;
        }

        stack.push_back({value, ways});
        ending_sum += value * ways;
        answer += ending_sum;
    }

    cout << answer << '\n';
}
