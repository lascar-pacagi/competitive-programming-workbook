#pragma once

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
