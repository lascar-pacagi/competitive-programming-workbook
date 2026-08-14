#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tests;
    cin >> tests;
    while (tests--) {
        string s, answer;
        cin >> s;
        array<int, 26> remaining{}, used{};
        for (char c : s) ++remaining[c - 'a'];
        for (char c : s) {
            int x = c - 'a';
            --remaining[x];
            if (used[x]) continue;
            while (!answer.empty() && answer.back() > c &&
                   remaining[answer.back() - 'a'] > 0) {
                used[answer.back() - 'a'] = false;
                answer.pop_back();
            }
            answer.push_back(c);
            used[x] = true;
        }
        cout << answer << '\n';
    }
}
