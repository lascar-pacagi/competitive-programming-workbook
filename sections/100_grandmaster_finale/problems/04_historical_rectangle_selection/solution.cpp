#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

constexpr int MOD = 1'000'000'007;

struct State {
    int64 score = 0;
    int ways = 0;
};

State combine(State a, State b) {
    if (a.score != b.score) return a.score > b.score ? a : b;
    if (a.score == 0) return {0, 0};
    return {a.score, static_cast<int>((a.ways + static_cast<long long>(b.ways)) % MOD)};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> x(n), y(n), compressed_y;
    vector<int64> reward(n), dp(n);
    vector<int> ways(n, 1);
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i] >> reward[i];
        compressed_y.push_back(y[i]);
        dp[i] = reward[i];
    }
    sort(compressed_y.begin(), compressed_y.end());
    compressed_y.erase(unique(compressed_y.begin(), compressed_y.end()),
                       compressed_y.end());
    vector<int> rank_y(n);
    for (int i = 0; i < n; ++i)
        rank_y[i] = lower_bound(compressed_y.begin(), compressed_y.end(), y[i])
                  - compressed_y.begin() + 1;

    vector<State> bit(compressed_y.size() + 1);
    vector<int> touched;
    auto update = [&](int position, State state) {
        for (int i = position; i < static_cast<int>(bit.size()); i += i & -i) {
            bit[i] = combine(bit[i], state);
            touched.push_back(i);
        }
    };
    auto query = [&](int position) {
        State result;
        for (int i = position; i > 0; i -= i & -i)
            result = combine(result, bit[i]);
        return result;
    };

    auto cdq = [&](auto &&self, int left, int right) -> void {
        if (right - left == 1) return;
        int middle = (left + right) / 2;
        self(self, left, middle);
        vector<int> first, second;
        first.reserve(middle - left);
        second.reserve(right - middle);
        for (int i = left; i < middle; ++i) first.push_back(i);
        for (int i = middle; i < right; ++i) second.push_back(i);
        sort(first.begin(), first.end(), [&](int a, int b) {
            return pair{x[a], y[a]} < pair{x[b], y[b]};
        });
        sort(second.begin(), second.end(), [&](int a, int b) {
            return pair{x[a], y[a]} < pair{x[b], y[b]};
        });
        size_t pointer = 0;
        for (int j : second) {
            while (pointer < first.size() && x[first[pointer]] < x[j]) {
                int i = first[pointer++];
                update(rank_y[i], {dp[i], ways[i]});
            }
            State predecessor = query(rank_y[j] - 1);
            if (predecessor.score == 0) continue;
            int64 candidate = predecessor.score + reward[j];
            if (candidate > dp[j]) {
                dp[j] = candidate;
                ways[j] = predecessor.ways;
            } else if (candidate == dp[j]) {
                ways[j] = (ways[j] + static_cast<long long>(predecessor.ways)) % MOD;
            }
        }
        for (int position : touched) bit[position] = {};
        touched.clear();
        self(self, middle, right);
    };
    cdq(cdq, 0, n);

    State answer;
    for (int i = 0; i < n; ++i)
        answer = combine(answer, {dp[i], ways[i]});
    cout << answer.score << ' ' << answer.ways << '\n';
}
