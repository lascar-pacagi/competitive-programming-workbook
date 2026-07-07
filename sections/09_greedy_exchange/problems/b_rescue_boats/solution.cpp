#include <bits/stdc++.h>
using namespace std;

int solve_case(vector<int> weights, int limit) {
    sort(weights.begin(), weights.end());
    int left = 0;
    int right = (int)weights.size() - 1;
    int boats = 0;
    while (left <= right) {
        if (weights[left] + weights[right] <= limit) {
            ++left;
        }
        --right;
        ++boats;
    }
    return boats;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, limit;
        cin >> n >> limit;
        vector<int> weights(n);
        for (int &w : weights) cin >> w;
        cout << solve_case(weights, limit) << '\n';
    }

    return 0;
}

