#include <bits/stdc++.h>
using namespace std;
struct Eertree {
  struct N {
    array<int, 26> to;
    int len = 0, link = 0;
    long long occ = 0;
    N() { to.fill(0); }
  };
  vector<N> t;
  string s;
  int last = 1;
  Eertree() {
    t.resize(2);
    t[0].len = -1;
    t[0].link = 0;
    t[1].len = 0;
    t[1].link = 0;
  }
  bool add(char ch) {
    int c = ch - 'a', pos = s.size();
    s += ch;
    int p = last;
    while (pos - 1 - t[p].len < 0 || s[pos - 1 - t[p].len] != ch)
      p = t[p].link;
    if (t[p].to[c]) {
      last = t[p].to[c];
      ++t[last].occ;
      return false;
    }
    int v = t.size();
    t.emplace_back();
    t[v].len = t[p].len + 2;
    t[p].to[c] = v;
    if (t[v].len == 1)
      t[v].link = 1;
    else {
      int q = t[p].link;
      while (pos - 1 - t[q].len < 0 || s[pos - 1 - t[q].len] != ch)
        q = t[q].link;
      t[v].link = t[q].to[c];
    }
    last = v;
    t[v].occ = 1;
    return true;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  Eertree e;
  for (char c : s) {
    e.add(c);
    cout << e.t.size() - 2 << ' ' << e.t[e.last].len << '\n';
  }
}
