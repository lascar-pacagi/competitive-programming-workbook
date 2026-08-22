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
  int m, k;
  cin >> m >> k;
  vector<string> a(m);
  for (auto &x : a)
    cin >> x;
  SAM s(a[0]);
  int z = s.st.size();
  vector<vector<int>> seen(z, vector<int>(m));
  for (int v = 0; v < z; ++v)
    seen[v][0] = s.st[v].len;
  auto order = s.order();
  for (int id = 1; id < m; ++id) {
    vector<int> best(z);
    int v = 0, len = 0;
    for (char ch : a[id]) {
      int c = ch - 'a';
      while (v && s.st[v].next[c] == -1)
        v = s.st[v].link, len = min(len, s.st[v].len);
      if (s.st[v].next[c] != -1)
        v = s.st[v].next[c], ++len;
      else
        v = 0, len = 0;
      best[v] = max(best[v], len);
    }
    for (int j = z - 1; j; j--) {
      int x = order[j], p = s.st[x].link;
      best[p] = max(best[p], min(best[x], s.st[p].len));
    }
    for (int x = 0; x < z; ++x)
      seen[x][id] = min(best[x], s.st[x].len);
  }
  int ans = 0;
  for (int x = 1; x < z; ++x) {
    nth_element(seen[x].begin(), seen[x].begin() + m - k, seen[x].end());
    ans = max(ans, seen[x][m - k]);
  }
  cout << ans << '\n';
}
