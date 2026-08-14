#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, minimum_length, maximum_length;
    if (!(cin >> n >> minimum_length >> maximum_length)) return 0;
    vector<long long> prefix(n + 1);
    for (int index = 1; index <= n; ++index) {
        long long value;
        cin >> value;
        prefix[index] = prefix[index - 1] + value;
    }

    deque<int> candidates;
    long long answer = numeric_limits<long long>::lowest();
    for (int right = 1; right <= n; ++right) {
        int entering = right - minimum_length;
        if (entering >= 0) {
            while (!candidates.empty() && prefix[candidates.back()] >= prefix[entering]) {
                candidates.pop_back();
            }
            candidates.push_back(entering);
        }
        while (!candidates.empty() && candidates.front() < right - maximum_length) {
            candidates.pop_front();
        }
        if (!candidates.empty()) {
            answer = max(answer, prefix[right] - prefix[candidates.front()]);
        }
    }
    cout << answer << '\n';
}
