#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> values(n);
    for (long long& value : values)
        cin >> value;

    // Only new prefix minima can be useful left endpoints.
    vector<int> candidates;
    for (int i = 0; i < n; ++i)
        if (candidates.empty() || values[i] < values[candidates.back()])
            candidates.push_back(i);

    int answer = 0;
    for (int j = n - 1; j >= 0; --j) {
        while (!candidates.empty() &&
               values[candidates.back()] <= values[j]) {
            answer = max(answer, j - candidates.back());
            candidates.pop_back();
        }
    }

    cout << answer << '\n';
}
