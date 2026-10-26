#include <bits/stdc++.h>
using namespace std;

class Trie {
    struct Node {
        array<int, 26> next{};
        int pass = 0;
    };
    vector<Node> nodes{Node{}};

public:
    void insert(const string& word) {
        int v = 0;
        nodes[v].pass++;
        for (char ch : word) {
            int c = ch - 'a';
            if (nodes[v].next[c] == 0) {
                int child = nodes.size();
                nodes[v].next[c] = child;
                nodes.push_back(Node{});
            }
            v = nodes[v].next[c];
            nodes[v].pass++;
        }
    }

    int count_prefix(const string& prefix) const {
        int v = 0;
        for (char ch : prefix) {
            int child = nodes[v].next[ch - 'a'];
            if (child == 0) {
                return 0;
            }
            v = child;
        }
        return nodes[v].pass;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) {
        return 0;
    }
    Trie trie;
    for (int i = 0; i < n; i++) {
        string word;
        cin >> word;
        trie.insert(word);
    }
    while (q--) {
        string prefix;
        cin >> prefix;
        cout << trie.count_prefix(prefix) << '\n';
    }
}
