#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s, answer;
    int k, r;
    char required;
    cin >> s >> k >> required >> r;
    int remaining_required = count(s.begin(), s.end(), required);
    int chosen_required = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
        char c = s[i];
        while (!answer.empty() && answer.back() > c
               && (int)answer.size() - 1 + (int)s.size() - i >= k
               && (answer.back() != required
                   || chosen_required - 1 + remaining_required >= r)) {
            if (answer.back() == required) --chosen_required;
            answer.pop_back();
        }
        if ((int)answer.size() < k) {
            if (c == required) {
                answer.push_back(c);
                ++chosen_required;
            } else if (k - (int)answer.size() - 1 >= r - chosen_required) {
                answer.push_back(c);
            }
        }
        if (c == required) --remaining_required;
    }
    cout << answer << '\n';
}
