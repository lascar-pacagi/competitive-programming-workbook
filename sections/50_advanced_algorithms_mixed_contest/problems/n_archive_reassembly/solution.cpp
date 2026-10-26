#include <bits/stdc++.h>
using namespace std;

struct SuffixAutomaton {
    struct State {
        array<int, 26> next;
        int length = 0, link = -1;
        State() { next.fill(-1); }
    };
    vector<State> states;
    int last = 0;

    explicit SuffixAutomaton(const string& text) {
        states.reserve(2 * text.size());
        states.emplace_back();
        for (char ch : text) extend(ch - 'a');
    }

    void extend(int ch) {
        int cur = states.size();
        states.emplace_back();
        states[cur].length = states[last].length + 1;
        int p = last;
        while (p != -1 && states[p].next[ch] == -1) {
            states[p].next[ch] = cur;
            p = states[p].link;
        }
        if (p == -1) {
            states[cur].link = 0;
        } else {
            int q = states[p].next[ch];
            if (states[p].length + 1 == states[q].length) {
                states[cur].link = q;
            } else {
                int clone = states.size();
                states.push_back(states[q]);
                states[clone].length = states[p].length + 1;
                while (p != -1 && states[p].next[ch] == q) {
                    states[p].next[ch] = clone;
                    p = states[p].link;
                }
                states[q].link = states[cur].link = clone;
            }
        }
        last = cur;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string source, target;
    cin >> source >> target;
    SuffixAutomaton automaton(source);
    int state = 0, pieces = 1;
    for (char letter : target) {
        int ch = letter - 'a';
        int to = automaton.states[state].next[ch];
        if (to == -1) {
            ++pieces;
            to = automaton.states[0].next[ch];
            if (to == -1) {
                cout << -1 << '\n';
                return 0;
            }
        }
        state = to;
    }
    cout << pieces << '\n';
}
