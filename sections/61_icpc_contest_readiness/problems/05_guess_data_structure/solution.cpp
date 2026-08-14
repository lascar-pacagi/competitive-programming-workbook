#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        long long limit;
        cin >> n >> limit;
        vector<long long> values(n);
        for (long long &value : values) cin >> value;

        deque<int> maximum, minimum;
        int left = 0;
        long long answer = 0;
        for (int right = 0; right < n; ++right) {
            while (!maximum.empty() && values[maximum.back()] <= values[right]) maximum.pop_back();
            maximum.push_back(right);
            while (!minimum.empty() && values[minimum.back()] >= values[right]) minimum.pop_back();
            minimum.push_back(right);

            while (values[maximum.front()] - values[minimum.front()] > limit) {
                if (maximum.front() == left) maximum.pop_front();
                if (minimum.front() == left) minimum.pop_front();
                ++left;
            }
            answer += right - left + 1;
        }
        cout << answer << '\n';
    }
    return 0;
}
