#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, answer;
    cin >> s;
    array<int, 26> count{};
    for (char c : s) ++count[c - 'a'];
    int previous = -1;
    for (int position = 0; position < (int)s.size(); ++position) {
        array<int, 27> prefix{}, suffix{};
        for (int c = 0; c < 26; ++c) {
            prefix[c + 1] = max(prefix[c], count[c]);
        }
        for (int c = 25; c >= 0; --c) {
            suffix[c] = max(suffix[c + 1], count[c]);
        }
        int remaining = (int)s.size() - position - 1;
        int chosen = -1;
        for (int c = 0; c < 26; ++c) {
            if (c == previous || count[c] == 0) continue;
            int same = count[c] - 1;
            int other = max(prefix[c], suffix[c + 1]);
            if (same <= remaining / 2
                    && other <= (remaining + 1) / 2) {
                chosen = c;
                break;
            }
        }
        if (chosen == -1) {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
        answer.push_back(char('a' + chosen));
        --count[chosen];
        previous = chosen;
    }
    cout << answer << '\n';
}
