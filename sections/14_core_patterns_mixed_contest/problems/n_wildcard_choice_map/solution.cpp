#include <bits/stdc++.h>
using namespace std;

bool intersects(int low1, int high1, int low2, int high2) {
    return max(low1, low2) <= min(high1, high2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    int n = s.size();
    vector<int> prefix_low(n + 1), prefix_high(n + 1);
    for (int i = 0; i < n; ++i) {
        if (prefix_low[i] > prefix_high[i]) {
            prefix_low[i + 1] = 1;
            prefix_high[i + 1] = 0;
            continue;
        }
        int low = prefix_low[i];
        int high = prefix_high[i];
        if (s[i] == '(') ++low, ++high;
        else if (s[i] == ')') --low, --high;
        else --low, ++high;
        int parity = (i + 1) & 1;
        if (low < 0) low = parity;
        prefix_low[i + 1] = low;
        prefix_high[i + 1] = high;
    }
    if (n % 2 || prefix_low[n] > 0 || prefix_high[n] < 0) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }

    vector<int> suffix_low(n + 1), suffix_high(n + 1);
    for (int i = n - 1; i >= 0; --i) {
        if (suffix_low[i + 1] > suffix_high[i + 1]) {
            suffix_low[i] = 1;
            suffix_high[i] = 0;
            continue;
        }
        int low = suffix_low[i + 1];
        int high = suffix_high[i + 1];
        if (s[i] == '(') {
            low = low == 0 ? 1 : low - 1;
            high -= 1;
        } else if (s[i] == ')') {
            ++low;
            ++high;
        } else {
            low = low == 0 ? 1 : low - 1;
            ++high;
        }
        suffix_low[i] = low;
        suffix_high[i] = high;
    }

    string answer = s;
    for (int i = 0; i < n; ++i) {
        if (s[i] != '?') continue;
        bool can_open = intersects(
            prefix_low[i] + 1, prefix_high[i] + 1,
            suffix_low[i + 1], suffix_high[i + 1]);
        int closing_low = max(prefix_low[i], 1) - 1;
        bool can_close = intersects(
            closing_low, prefix_high[i] - 1,
            suffix_low[i + 1], suffix_high[i + 1]);
        if (can_open && !can_close) answer[i] = '(';
        else if (!can_open && can_close) answer[i] = ')';
        else answer[i] = '?';
    }
    cout << answer << '\n';
}
