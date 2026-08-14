#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tests;
    cin >> tests;
    while (tests--) {
        int n;
        string pattern;
        cin >> n >> pattern;

        vector<int> pending, answer;
        pending.reserve(n);
        answer.reserve(n);

        for (int value = 1; value <= n; ++value) {
            pending.push_back(value);
            if (value == n || pattern[value - 1] == '<') {
                while (!pending.empty()) {
                    answer.push_back(pending.back());
                    pending.pop_back();
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << answer[i];
        }
        cout << '\n';
    }
}
