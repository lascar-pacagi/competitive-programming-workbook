#include <bits/stdc++.h>
using namespace std;
struct SAM {
  struct Node {
    array<int, 26> next;
    int link = -1, len = 0;
    long long occ = 0;
    Node() { next.fill(-1); }
  };
  vector<Node> st;
  int last = 0;
  SAM() { st.emplace_back(); }
  void add(int c) {
    int cur = st.size();
    st.emplace_back();
    st[cur].len = st[last].len + 1;
    st[cur].occ = 1;
    int p = last;
    while (p != -1 && st[p].next[c] == -1)
      st[p].next[c] = cur, p = st[p].link;
    if (p == -1)
      st[cur].link = 0;
    else {
      int q = st[p].next[c];
      if (st[p].len + 1 == st[q].len)
        st[cur].link = q;
      else {
        int clone = st.size();
        st.push_back(st[q]);
        st[clone].len = st[p].len + 1;
        st[clone].occ = 0;
        while (p != -1 && st[p].next[c] == q)
          st[p].next[c] = clone, p = st[p].link;
        st[q].link = st[cur].link = clone;
      }
    }
    last = cur;
  }
  SAM(const string &s) : SAM() {
    for (char c : s)
      add(c - 'a');
  }
  vector<int> order() const {
    vector<int> o(st.size());
    iota(o.begin(), o.end(), 0);
    sort(o.begin(), o.end(),
         [&](int a, int b) { return st[a].len < st[b].len; });
    return o;
  }
  void occurrences() {
    auto o = order();
    for (int i = (int)o.size() - 1; i; --i)
      st[st[o[i]].link].occ += st[o[i]].occ;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  SAM a(s);
  int n = a.st.size();
  vector<int> par(n, -2), letter(n);
  queue<int> q;
  par[0] = -1;
  q.push(0);
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int c = 0; c < 26; ++c) {
      int u = a.st[v].next[c];
      if (u == -1) {
        string ans(1, char('a' + c));
        for (int x = v; x; x = par[x])
          ans += char('a' + letter[x]);
        reverse(ans.begin(), ans.end());
        cout << ans << '\n';
        return 0;
      }
      if (par[u] == -2) {
        par[u] = v;
        letter[u] = c;
        q.push(u);
      }
    }
  }
}
