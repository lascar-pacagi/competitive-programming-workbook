#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int teammates, cards, edges;
    if (!(cin >> teammates >> cards >> edges)) return 0;
    vector<vector<int>> graph(teammates + 1);
    while (edges--) {
        int teammate, card;
        cin >> teammate >> card;
        graph[teammate].push_back(card);
    }

    vector<int> match_card(cards + 1);
    vector<char> seen(cards + 1);
    function<bool(int)> augment = [&](int teammate) {
        for (int card : graph[teammate]) {
            if (seen[card]) continue;
            seen[card] = true;
            if (match_card[card] == 0 || augment(match_card[card])) {
                match_card[card] = teammate;
                return true;
            }
        }
        return false;
    };

    int answer = 0;
    for (int teammate = 1; teammate <= teammates; ++teammate) {
        fill(seen.begin(), seen.end(), false);
        answer += augment(teammate);
    }
    cout << answer << '\n';
}
