#include <bits/stdc++.h>
using namespace std;
struct Node { array<int,26> next{}; int pass = 0; };
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0; vector<string> words(n); vector<Node> trie(1);
    for (string &word : words) { cin >> word; int node = 0; for (char ch : word) { int c=ch-'a'; if (!trie[node].next[c]) { trie[node].next[c]=trie.size(); trie.push_back(Node{}); } node=trie[node].next[c]; ++trie[node].pass; } }
    for (const string &word : words) { int node=0, answer=-1; for (int i=0;i<(int)word.size();++i) { node=trie[node].next[word[i]-'a']; if (trie[node].pass==1) { answer=i+1; break; } } cout << answer << '\n'; }
}
