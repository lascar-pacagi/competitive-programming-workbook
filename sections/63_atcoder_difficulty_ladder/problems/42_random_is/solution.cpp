#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int move_count, pile_count;
    if (!(cin >> move_count >> pile_count)) return 0;
    vector<int> moves(move_count), piles(pile_count);
    for (int& move : moves) cin >> move;
    int maximum = 0;
    for (int& pile : piles) {
        cin >> pile;
        maximum = max(maximum, pile);
    }

    vector<int> grundy(maximum + 1);
    for (int stones = 1; stones <= maximum; ++stones) {
        bool seen[32]{};
        for (int move : moves) {
            if (move <= stones) seen[grundy[stones - move]] = true;
        }
        while (seen[grundy[stones]]) ++grundy[stones];
    }
    int total = 0;
    for (int pile : piles) total ^= grundy[pile];
    cout << (total ? "WIN" : "LOSE") << '\n';
}
