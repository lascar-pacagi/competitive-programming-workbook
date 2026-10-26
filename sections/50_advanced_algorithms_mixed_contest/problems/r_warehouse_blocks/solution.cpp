#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<ll> positions(n), prefix(n + 1);
    for (int i = 0; i < n; ++i) {
        cin >> positions[i];
        prefix[i + 1] = prefix[i] + positions[i];
    }
    auto cost = [&](int left, int right) {
        int median = (left + right - 1) / 2;
        ll x = positions[median];
        return x * (median - left) - (prefix[median] - prefix[left])
             + prefix[right] - prefix[median + 1] - x * (right - median - 1);
    };
    const ll INF = 1LL << 62;
    vector<ll> previous(n + 1, INF);
    previous[0] = 0;
    for (int group = 1; group <= k; ++group) {
        vector<ll> current(n + 1, INF);
        function<void(int, int, int, int)> compute =
            [&](int low, int high, int opt_low, int opt_high) {
                if (low > high) return;
                int middle = (low + high) / 2;
                ll best_value = INF;
                int best_split = opt_low;
                int last_split = min(opt_high, middle - 1);
                for (int split = opt_low; split <= last_split; ++split) {
                    if (previous[split] == INF) continue;
                    ll candidate = previous[split] + cost(split, middle);
                    if (candidate < best_value) {
                        best_value = candidate;
                        best_split = split;
                    }
                }
                current[middle] = best_value;
                compute(low, middle - 1, opt_low, best_split);
                compute(middle + 1, high, best_split, opt_high);
            };
        compute(group, n, group - 1, n - 1);
        previous.swap(current);
    }
    cout << previous[n] << '\n';
}
