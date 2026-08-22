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
  long long k;
  cin >> s >> k;
  SAM a(s);
  const long long CAP = 4000000000000000000LL;
  auto o = a.order();
  vector<long long> dp(a.st.size());
  for (int z = (int)o.size() - 1; z >= 0; --z) {
    int v = o[z];
    for (int u : a.st[v].next)
      if (u != -1) {
        long long add = min(CAP, 1 + dp[u]);
        dp[v] = dp[v] >= CAP - add ? CAP : dp[v] + add;
      }
  }
  if (k > dp[0]) {
    cout << "IMPOSSIBLE\n";
    return 0;
  }
  string ans;
  int v = 0;
  while (k) {
    for (int c = 0; c < 26; ++c) {
      int u = a.st[v].next[c];
      if (u == -1)
        continue;
      long long block = 1 + dp[u];
      if (k > block)
        k -= block;
      else {
        ans += char('a' + c);
        --k;
        v = u;
        break;
      }
    }
  }
  cout << ans << '\n';
}
