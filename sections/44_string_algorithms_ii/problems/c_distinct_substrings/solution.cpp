#include <bits/stdc++.h>
using namespace std;

class SuffixAutomaton {
    struct State {
        map<char, int> next;  // Character transitions: extend to the right.
        int link = -1;        // Next group of shorter suffixes.
        int len = 0;          // Longest string in this group.
    };
    vector<State> states{State{}};
    int last = 0;

public:
    void extend(char ch) {
        // 1. Make a state for the new whole text and its new suffixes.
        int cur = states.size();
        states.push_back(State{});
        states[cur].len = states[last].len + 1;
        int p = last;

        // 2. Visit old suffix groups that have no ch continuation.
        while (p != -1 && !states[p].next.count(ch)) {
            states[p].next[ch] = cur;
            p = states[p].link;
        }

        // 3. Find the next shorter group for cur.
        if (p == -1) {
            // Case 1: ch is new; only the empty suffix was known.
            states[cur].link = 0;
        } else {
            int q = states[p].next.at(ch);
            if (states[p].len + 1 == states[q].len) {
                // Case 2: all of q is the next suffix group.
                states[cur].link = q;
            } else {
                // Case 3: split q; clone keeps its shorter strings.
                int clone = states.size();
                State copied = states[q];
                copied.len = states[p].len + 1;
                states.push_back(copied);

                // Redirect only the shorter incoming contexts.
                while (p != -1) {
                    auto it = states[p].next.find(ch);
                    // Every shorter suffix also has a ch transition.
                    assert(it != states[p].next.end());
                    if (it->second != q) {
                        break;
                    }
                    it->second = clone;
                    p = states[p].link;
                }
                // Both longer groups now have clone as suffix parent.
                states[q].link = clone;
                states[cur].link = clone;
            }
        }
        last = cur;
    }

    long long count_distinct() const {
        long long answer = 0;
        for (int v = 1; v < (int)states.size(); v++) {
            int parent = states[v].link;
            answer += states[v].len - states[parent].len;
        }
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) {
        return 0;
    }
    SuffixAutomaton sam;
    for (char ch : s) {
        sam.extend(ch);
    }
    cout << sam.count_distinct() << '\n';
}
