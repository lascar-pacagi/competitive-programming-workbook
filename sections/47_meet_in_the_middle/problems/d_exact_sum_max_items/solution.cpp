#include <bits/stdc++.h>
using namespace std;

using State = pair<long long, int>;

vector<State> enumerate_states(const vector<long long>& values) {
    vector<State> states{{0, 0}};
    states.reserve(1ULL << values.size());
    for (long long value : values) {
        int old_size = (int)states.size();
        for (int i = 0; i < old_size; i++) {
            states.push_back({states[i].first + value, states[i].second + 1});
        }
    }
    return states;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;
    vector<long long> values(n);
    for (long long& value : values) cin >> value;

    vector<long long> left_values(values.begin(), values.begin() + n / 2);
    vector<long long> right_values(values.begin() + n / 2, values.end());
    vector<State> left_states = enumerate_states(left_values);
    vector<State> right_states = enumerate_states(right_values);

    unordered_map<long long, int> best_right_count;
    best_right_count.reserve(right_states.size() * 2);
    for (const State& state : right_states) {
        best_right_count[state.first] = max(best_right_count[state.first], state.second);
    }

    int answer = -1;
    for (const State& state : left_states) {
        auto it = best_right_count.find(target - state.first);
        if (it != best_right_count.end()) answer = max(answer, state.second + it->second);
    }
    cout << answer << '\n';
    return 0;
}
