"""Generate the original advanced suffix-structure packages, Sections 76--78."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CPP_STUB = """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
"""

PY_STUB = """import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
"""

SECTIONS = {
    76: ("suffix_arrays_lcp", "Suffix Arrays And LCP Structure"),
    77: ("suffix_automata_palindromic_trees", "Suffix Automata And Palindromic Trees"),
    78: ("master_suffix_structures_mixed", "Master Suffix Structures Mixed Contest"),
}

PROBLEMS = {
    76: [
        ("a_suffix_order_lcp", "Suffix Order And LCP", "suffix_dump"),
        ("b_repeated_at_least_k", "Repeated At Least K Times", "repeat_k"),
        ("c_pattern_occurrence_queries", "Pattern Occurrence Queries", "pattern_queries"),
        ("d_disjoint_repeated_substring", "Disjoint Repeated Substring", "disjoint_repeat"),
    ],
    77: [
        ("a_kth_distinct_substring", "K-th Distinct Substring", "kth_distinct"),
        ("b_longest_common_substring", "Longest Common Substring", "lcs"),
        ("c_palindrome_prefix_profile", "Palindrome Prefix Profile", "pal_profile"),
        ("d_shortest_absent_word", "Shortest Absent Word", "absent_word"),
    ],
    78: [
        ("a_minimum_rotation", "Minimum Rotation", "rotation"),
        ("b_repetition_spectrum", "Repetition Spectrum", "spectrum"),
        ("c_kth_substring_with_multiplicity", "K-th Substring With Multiplicity", "kth_multi"),
        ("d_common_distinct_substrings", "Common Distinct Substrings", "common_count"),
        ("e_palindrome_frequency_value", "Palindrome Frequency Value", "pal_value"),
        ("f_multi_archive_commonality", "Multi-Archive Commonality", "multi_lcs"),
    ],
}

STATEMENTS = {
    "suffix_dump": """A nonempty lowercase string `s` is given. Print the starting positions of all suffixes in lexicographic order, using 1-based positions. On the next line print the LCP lengths of every adjacent pair in that order.

Input: one string `s`, with `1 <= |s| <= 200000`.

Output: the suffix positions, then `|s|-1` LCP values (an empty second line when `|s|=1`).

Sample input
```text
banana
```
Sample output
```text
6 4 2 1 5 3
1 3 0 0 2
```""",
    "repeat_k": """Given a lowercase string `s` and an integer `k`, find the maximum length of a substring that occurs at least `k` times. Occurrences may overlap.

Input: `s` and `k` on one line, with `1 <= |s| <= 200000` and `1 <= k <= |s|`.

Output: one integer.

Sample input
```text
banana 2
```
Sample output
```text
3
```""",
    "pattern_queries": """Store a lowercase text `s`. For each query pattern, report how many starting positions of `s` contain that pattern.

Input: `s`, then `q`, then `q` nonempty lowercase patterns. The total pattern length is at most `200000`; `|s| <= 200000`.

Output: one count per query.

Sample input
```text
banana
3
ana
na
x
```
Sample output
```text
2
2
0
```""",
    "disjoint_repeat": """Find the greatest `L` for which a lowercase string contains two equal length-`L` substrings with disjoint index intervals. The occurrences may touch but may not overlap.

Input: one string `s`, `1 <= |s| <= 200000`.

Output: the maximum `L`.

Sample input
```text
aaaaa
```
Sample output
```text
2
```""",
    "kth_distinct": """List all distinct nonempty substrings of `s` in lexicographic order. Print the `k`-th one, or `IMPOSSIBLE` when fewer than `k` exist.

Input: lowercase `s` and `k`, with `|s| <= 200000` and `1 <= k <= 10^18`.

Sample input
```text
aba 4
```
Sample output
```text
b
```""",
    "lcs": """Given two nonempty lowercase strings, print the length of their longest common substring. A substring must be contiguous.

Input: strings `a` and `b`; their total length is at most `400000`.

Sample input
```text
abacaba bac
```
Sample output
```text
3
```""",
    "pal_profile": """For every nonempty prefix of a lowercase string, print two values: the number of distinct palindromic substrings in that prefix, and the length of its longest palindromic suffix.

Input: one string `s`, `1 <= |s| <= 200000`.

Output: `|s|` lines.

Sample input
```text
ababa
```
Sample output
```text
1 1
2 1
3 3
4 3
5 5
```""",
    "absent_word": """Find a nonempty lowercase word that is not a substring of `s`. Minimize its length; among equally short answers, choose the lexicographically smallest.

Input: one lowercase string `s`, `1 <= |s| <= 200000`.

Output: the required word.

Sample input
```text
abc
```
Sample output
```text
d
```""",
    "rotation": """Among all cyclic rotations of a lowercase string, print the lexicographically smallest rotation and its smallest 1-based starting position.

Input: one nonempty string `s`, `|s| <= 1000000`.

Sample input
```text
baca
```
Sample output
```text
abac
4
```""",
    "spectrum": """For every `k` from `1` through `n`, find the maximum length of a substring occurring at least `k` times in `s`. Occurrences may overlap.

Input: one lowercase string `s`, `1 <= n <= 200000`.

Output: `n` integers.

Sample input
```text
banana
```
Sample output
```text
6 3 1 0 0 0
```""",
    "kth_multi": """Form a multiset containing one copy of `s[l..r]` for every index pair `l <= r`. Sort it lexicographically, retaining duplicates. Print its `k`-th element or `IMPOSSIBLE`.

Input: lowercase `s` and `k`, with `|s| <= 200000`, `1 <= k <= 10^18`.

Sample input
```text
aba 3
```
Sample output
```text
ab
```""",
    "common_count": """Count the distinct nonempty strings that are substrings of both given lowercase strings.

Input: `a` and `b`, whose total length is at most `400000`.

Output: one 64-bit integer.

Sample input
```text
aba bab
```
Sample output
```text
4
```""",
    "pal_value": """For each distinct palindromic substring `p` of `s`, define its value as `|p|` times its number of occurrences. Print the maximum value.

Input: one lowercase string `s`, `1 <= |s| <= 200000`.

Sample input
```text
ababa
```
Sample output
```text
6
```""",
    "multi_lcs": """Given `m` lowercase archives and `k`, find the maximum length of a string that occurs as a substring in at least `k` different archives.

Input: `m k`, followed by `m` strings. `1 <= k <= m <= 20`; total length is at most `200000`.

Output: one integer.

Sample input
```text
3 2
ababc
babca
zzabaz
```
Sample output
```text
4
```""",
}

CPP = {}
PY = {}

SA_CPP = r'''#include <bits/stdc++.h>
using namespace std;
vector<int> suffix_array(const string& s) {
    int n=s.size(); vector<int> sa(n),r(n),nr(n); iota(sa.begin(),sa.end(),0);
    for(int i=0;i<n;++i)r[i]=(unsigned char)s[i];
    for(int k=1;;k*=2){
        sort(sa.begin(),sa.end(),[&](int a,int b){return pair{r[a],a+k<n?r[a+k]:-1}<pair{r[b],b+k<n?r[b+k]:-1};});
        nr[sa[0]]=0; for(int i=1;i<n;++i){int a=sa[i-1],b=sa[i];nr[b]=nr[a]+(pair{r[a],a+k<n?r[a+k]:-1}<pair{r[b],b+k<n?r[b+k]:-1});}
        r=nr;if(r[sa.back()]==n-1)break;
    } return sa;
}
vector<int> lcp_array(const string&s,const vector<int>&sa){
    int n=s.size(),h=0;vector<int>rank(n),lcp(max(0,n-1));for(int i=0;i<n;++i)rank[sa[i]]=i;
    for(int i=0;i<n;++i){int q=rank[i];if(!q)continue;int j=sa[q-1];while(i+h<n&&j+h<n&&s[i+h]==s[j+h])++h;lcp[q-1]=h;if(h)--h;}return lcp;
}
'''

SA_PY = r'''def suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = list(map(ord, s))
    step = 1
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + step] if i + step < n else -1))
        new_rank = [0] * n
        for j in range(1, n):
            a, b = sa[j - 1], sa[j]
            left = (rank[a], rank[a + step] if a + step < n else -1)
            right = (rank[b], rank[b + step] if b + step < n else -1)
            new_rank[b] = new_rank[a] + (left < right)
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            return sa
        step *= 2


def lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, start in enumerate(sa):
        rank[start] = i
    lcp = [0] * (n - 1)
    height = 0
    for i in range(n):
        place = rank[i]
        if place == 0:
            continue
        j = sa[place - 1]
        while i + height < n and j + height < n and s[i + height] == s[j + height]:
            height += 1
        lcp[place - 1] = height
        height = max(0, height - 1)
    return lcp
'''

SAM_CPP = r'''#include <bits/stdc++.h>
using namespace std;
struct SAM{
    struct Node{array<int,26>next;int link=-1,len=0;long long occ=0;Node(){next.fill(-1);}};
    vector<Node>st;int last=0;SAM(){st.emplace_back();}
    void add(int c){int cur=st.size();st.emplace_back();st[cur].len=st[last].len+1;st[cur].occ=1;int p=last;
        while(p!=-1&&st[p].next[c]==-1)st[p].next[c]=cur,p=st[p].link;
        if(p==-1)st[cur].link=0;else{int q=st[p].next[c];if(st[p].len+1==st[q].len)st[cur].link=q;else{int clone=st.size();st.push_back(st[q]);st[clone].len=st[p].len+1;st[clone].occ=0;while(p!=-1&&st[p].next[c]==q)st[p].next[c]=clone,p=st[p].link;st[q].link=st[cur].link=clone;}}last=cur;}
    SAM(const string&s):SAM(){for(char c:s)add(c-'a');}
    vector<int> order()const{vector<int>o(st.size());iota(o.begin(),o.end(),0);sort(o.begin(),o.end(),[&](int a,int b){return st[a].len<st[b].len;});return o;}
    void occurrences(){auto o=order();for(int i=(int)o.size()-1;i;--i)st[st[o[i]].link].occ+=st[o[i]].occ;}
};
'''

SAM_PY = r'''class SAM:
    def __init__(self, s):
        self.next = [{}]
        self.link = [-1]
        self.length = [0]
        self.occ = [0]
        last = 0
        for char in s:
            current = len(self.next)
            self.next.append({})
            self.link.append(0)
            self.length.append(self.length[last] + 1)
            self.occ.append(1)
            parent = last
            while parent != -1 and char not in self.next[parent]:
                self.next[parent][char] = current
                parent = self.link[parent]
            if parent == -1:
                self.link[current] = 0
            else:
                target = self.next[parent][char]
                if self.length[parent] + 1 == self.length[target]:
                    self.link[current] = target
                else:
                    clone = len(self.next)
                    self.next.append(self.next[target].copy())
                    self.link.append(self.link[target])
                    self.length.append(self.length[parent] + 1)
                    self.occ.append(0)
                    while parent != -1 and self.next[parent].get(char) == target:
                        self.next[parent][char] = clone
                        parent = self.link[parent]
                    self.link[target] = self.link[current] = clone
            last = current

    def order(self):
        return sorted(range(len(self.next)), key=self.length.__getitem__)

    def occurrences(self):
        order = self.order()
        for state in reversed(order[1:]):
            self.occ[self.link[state]] += self.occ[state]
'''

EERTREE_CPP = r'''#include <bits/stdc++.h>
using namespace std;
struct Eertree{struct N{array<int,26>to;int len=0,link=0;long long occ=0;N(){to.fill(0);}};vector<N>t;string s;int last=1;
    Eertree(){t.resize(2);t[0].len=-1;t[0].link=0;t[1].len=0;t[1].link=0;}
    bool add(char ch){int c=ch-'a',pos=s.size();s+=ch;int p=last;while(pos-1-t[p].len<0||s[pos-1-t[p].len]!=ch)p=t[p].link;
        if(t[p].to[c]){last=t[p].to[c];++t[last].occ;return false;}int v=t.size();t.emplace_back();t[v].len=t[p].len+2;t[p].to[c]=v;
        if(t[v].len==1)t[v].link=1;else{int q=t[p].link;while(pos-1-t[q].len<0||s[pos-1-t[q].len]!=ch)q=t[q].link;t[v].link=t[q].to[c];}last=v;t[v].occ=1;return true;}
};
'''

EERTREE_PY = r'''class Eertree:
    def __init__(self):
        self.next = [{}, {}]
        self.length = [-1, 0]
        self.link = [0, 0]
        self.occ = [0, 0]
        self.text = []
        self.last = 1

    def add(self, char):
        position = len(self.text)
        self.text.append(char)
        node = self.last
        while position - 1 - self.length[node] < 0 or self.text[position - 1 - self.length[node]] != char:
            node = self.link[node]
        if char in self.next[node]:
            self.last = self.next[node][char]
            self.occ[self.last] += 1
            return False
        created = len(self.next)
        self.next.append({})
        self.length.append(self.length[node] + 2)
        self.link.append(1)
        self.occ.append(1)
        self.next[node][char] = created
        if self.length[created] > 1:
            suffix = self.link[node]
            while position - 1 - self.length[suffix] < 0 or self.text[position - 1 - self.length[suffix]] != char:
                suffix = self.link[suffix]
            self.link[created] = self.next[suffix][char]
        self.last = created
        return True
'''

CPP["suffix_dump"] = SA_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;auto sa=suffix_array(s),lcp=lcp_array(s,sa);for(int i=0;i<(int)sa.size();++i)cout<<sa[i]+1<<" \n"[i+1==(int)sa.size()];for(int i=0;i<(int)lcp.size();++i)cout<<lcp[i]<<" \n"[i+1==(int)lcp.size()];if(lcp.empty())cout<<'\n';}
'''
PY["suffix_dump"] = SA_PY + r'''

def main():
    import sys
    s = sys.stdin.buffer.readline().decode().strip()
    sa = suffix_array(s)
    print(*(start + 1 for start in sa))
    print(*lcp_array(s, sa))


if __name__ == "__main__":
    main()
'''

CPP["repeat_k"] = SA_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;int k;cin>>s>>k;int n=s.size();if(k==1){cout<<n<<'\n';return 0;}auto sa=suffix_array(s),lcp=lcp_array(s,sa);deque<int>q;int ans=0,w=k-1;for(int i=0;i<n-1;++i){while(!q.empty()&&lcp[q.back()]>=lcp[i])q.pop_back();q.push_back(i);while(q.front()<=i-w)q.pop_front();if(i+1>=w)ans=max(ans,lcp[q.front()]);}cout<<ans<<'\n';}
'''
PY["repeat_k"] = SA_PY + r'''

def main():
    import collections
    import sys
    s, raw_k = sys.stdin.buffer.read().split()
    s, k = s.decode(), int(raw_k)
    if k == 1:
        print(len(s))
        return
    lcp = lcp_array(s, suffix_array(s))
    window = k - 1
    queue = collections.deque()
    answer = 0
    for i, value in enumerate(lcp):
        while queue and lcp[queue[-1]] >= value:
            queue.pop()
        queue.append(i)
        while queue[0] <= i - window:
            queue.popleft()
        if i + 1 >= window:
            answer = max(answer, lcp[queue[0]])
    print(answer)


if __name__ == "__main__":
    main()
'''

CPP["pattern_queries"] = SA_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;int q;cin>>s>>q;auto sa=suffix_array(s);while(q--){string p;cin>>p;auto cmp=[&](int at){int z=s.compare(at,p.size(),p);return z<0?-1:z>0?1:0;};int l=0,r=sa.size();while(l<r){int m=(l+r)/2;if(cmp(sa[m])<0)l=m+1;else r=m;}int first=l;l=0;r=sa.size();while(l<r){int m=(l+r)/2;if(cmp(sa[m])<=0)l=m+1;else r=m;}cout<<l-first<<'\n';}}
'''
PY["pattern_queries"] = SA_PY + r'''

def main():
    import sys
    data = sys.stdin.buffer.read().split()
    s = data[0].decode()
    sa = suffix_array(s)
    output = []
    for raw in data[2:]:
        pattern = raw.decode()
        def compare(start):
            piece = s[start:start + len(pattern)]
            return (piece > pattern) - (piece < pattern)
        left, right = 0, len(sa)
        while left < right:
            middle = (left + right) // 2
            if compare(sa[middle]) < 0:
                left = middle + 1
            else:
                right = middle
        first = left
        left, right = 0, len(sa)
        while left < right:
            middle = (left + right) // 2
            if compare(sa[middle]) <= 0:
                left = middle + 1
            else:
                right = middle
        output.append(str(left - first))
    print("\n".join(output))


if __name__ == "__main__":
    main()
'''

CPP["disjoint_repeat"] = SA_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;int n=s.size();auto sa=suffix_array(s),lcp=lcp_array(s,sa);auto ok=[&](int need){int lo=sa[0],hi=sa[0];for(int i=0;i<n-1;++i){if(lcp[i]<need)lo=hi=sa[i+1];else{lo=min(lo,sa[i+1]);hi=max(hi,sa[i+1]);if(hi-lo>=need)return true;}}return false;};int l=0,r=n/2+1;while(r-l>1){int m=(l+r)/2;(ok(m)?l:r)=m;}cout<<l<<'\n';}
'''
PY["disjoint_repeat"] = SA_PY + r'''

def main():
    import sys
    s = sys.stdin.buffer.readline().decode().strip()
    sa = suffix_array(s)
    lcp = lcp_array(s, sa)

    def possible(length):
        low = high = sa[0]
        for i, common in enumerate(lcp):
            if common < length:
                low = high = sa[i + 1]
            else:
                low = min(low, sa[i + 1])
                high = max(high, sa[i + 1])
                if high - low >= length:
                    return True
        return False

    low, high = 0, len(s) // 2 + 1
    while high - low > 1:
        middle = (low + high) // 2
        if possible(middle):
            low = middle
        else:
            high = middle
    print(low)


if __name__ == "__main__":
    main()
'''

CPP["rotation"] = r'''#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;int n=s.size(),i=0,j=1,k=0;while(i<n&&j<n&&k<n){char a=s[(i+k)%n],b=s[(j+k)%n];if(a==b){++k;continue;}if(a>b){i=i+k+1;if(i==j)++i;}else{j=j+k+1;if(i==j)++j;}k=0;}int at=min(i,j);cout<<s.substr(at)+s.substr(0,at)<<'\n'<<at+1<<'\n';}
'''
PY["rotation"] = r'''import sys


def main():
    s = sys.stdin.buffer.readline().decode().strip()
    n = len(s)
    first, second, offset = 0, 1, 0
    while first < n and second < n and offset < n:
        a, b = s[(first + offset) % n], s[(second + offset) % n]
        if a == b:
            offset += 1
            continue
        if a > b:
            first += offset + 1
            if first == second:
                first += 1
        else:
            second += offset + 1
            if first == second:
                second += 1
        offset = 0
    start = min(first, second)
    print(s[start:] + s[:start])
    print(start + 1)


if __name__ == "__main__":
    main()
'''

CPP["spectrum"] = SA_CPP + r'''
struct DSU{vector<int>p,z;DSU(int n):p(n),z(n,1){iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}int unite(int a,int b){a=f(a);b=f(b);if(a==b)return z[a];if(z[a]<z[b])swap(a,b);p[b]=a;return z[a]+=z[b];}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;int n=s.size();auto sa=suffix_array(s),lcp=lcp_array(s,sa);vector<array<int,3>>e;for(int i=0;i<n-1;++i)e.push_back({lcp[i],i,i+1});sort(e.rbegin(),e.rend());DSU d(n);vector<int>ans(n+1);ans[1]=n;for(auto [w,a,b]:e){int size=d.unite(a,b);ans[size]=max(ans[size],w);}for(int k=n-1;k;--k)ans[k]=max(ans[k],ans[k+1]);for(int k=1;k<=n;++k)cout<<ans[k]<<" \n"[k==n];}
'''
PY["spectrum"] = SA_PY + r'''

def main():
    import sys
    s = sys.stdin.buffer.readline().decode().strip()
    n = len(s)
    sa = suffix_array(s)
    edges = sorted(((w, i, i + 1) for i, w in enumerate(lcp_array(s, sa))), reverse=True)
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = [0] * (n + 1)
    answer[1] = n
    for weight, a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
        answer[size[a]] = max(answer[size[a]], weight)
    for k in range(n - 1, 0, -1):
        answer[k] = max(answer[k], answer[k + 1])
    print(*answer[1:])


if __name__ == "__main__":
    main()
'''

CPP["kth_distinct"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;long long k;cin>>s>>k;SAM a(s);const long long CAP=4000000000000000000LL;auto o=a.order();vector<long long>dp(a.st.size());for(int z=(int)o.size()-1;z>=0;--z){int v=o[z];for(int u:a.st[v].next)if(u!=-1){long long add=min(CAP,1+dp[u]);dp[v]=dp[v]>=CAP-add?CAP:dp[v]+add;}}if(k>dp[0]){cout<<"IMPOSSIBLE\n";return 0;}string ans;int v=0;while(k){for(int c=0;c<26;++c){int u=a.st[v].next[c];if(u==-1)continue;long long block=1+dp[u];if(k>block)k-=block;else{ans+=char('a'+c);--k;v=u;break;}}}cout<<ans<<'\n';}
'''
PY["kth_distinct"] = SAM_PY + r'''

def main():
    import sys
    raw_s, raw_k = sys.stdin.buffer.read().split()
    automaton = SAM(raw_s.decode())
    k = int(raw_k)
    paths = [0] * len(automaton.next)
    for state in reversed(automaton.order()):
        paths[state] = sum(1 + paths[target] for target in automaton.next[state].values())
    if k > paths[0]:
        print("IMPOSSIBLE")
        return
    answer = []
    state = 0
    while k:
        for char, target in sorted(automaton.next[state].items()):
            block = 1 + paths[target]
            if k > block:
                k -= block
            else:
                answer.append(char)
                k -= 1
                state = target
                break
    print("".join(answer))


if __name__ == "__main__":
    main()
'''

CPP["lcs"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string a,b;cin>>a>>b;SAM s(a);int v=0,len=0,ans=0;for(char ch:b){int c=ch-'a';while(v&&s.st[v].next[c]==-1)v=s.st[v].link,len=min(len,s.st[v].len);if(s.st[v].next[c]!=-1)v=s.st[v].next[c],++len;else v=0,len=0;ans=max(ans,len);}cout<<ans<<'\n';}
'''
PY["lcs"] = SAM_PY + r'''

def main():
    import sys
    a, b = (part.decode() for part in sys.stdin.buffer.read().split())
    automaton = SAM(a)
    state = length = answer = 0
    for char in b:
        while state and char not in automaton.next[state]:
            state = automaton.link[state]
            length = min(length, automaton.length[state])
        if char in automaton.next[state]:
            state = automaton.next[state][char]
            length += 1
        else:
            state = length = 0
        answer = max(answer, length)
    print(answer)


if __name__ == "__main__":
    main()
'''

CPP["pal_profile"] = EERTREE_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;Eertree e;for(char c:s){e.add(c);cout<<e.t.size()-2<<' '<<e.t[e.last].len<<'\n';}}
'''
PY["pal_profile"] = EERTREE_PY + r'''

def main():
    import sys
    tree = Eertree()
    output = []
    for char in sys.stdin.buffer.readline().decode().strip():
        tree.add(char)
        output.append(f"{len(tree.next) - 2} {tree.length[tree.last]}")
    print("\n".join(output))


if __name__ == "__main__":
    main()
'''

CPP["absent_word"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;SAM a(s);int n=a.st.size();vector<int>par(n,-2),letter(n);queue<int>q;par[0]=-1;q.push(0);while(!q.empty()){int v=q.front();q.pop();for(int c=0;c<26;++c){int u=a.st[v].next[c];if(u==-1){string ans(1,char('a'+c));for(int x=v;x;x=par[x])ans+=char('a'+letter[x]);reverse(ans.begin(),ans.end());cout<<ans<<'\n';return 0;}if(par[u]==-2){par[u]=v;letter[u]=c;q.push(u);}}}}
'''
PY["absent_word"] = SAM_PY + r'''

def main():
    import collections
    import sys
    automaton = SAM(sys.stdin.buffer.readline().decode().strip())
    parent = [None] * len(automaton.next)
    letter = [""] * len(automaton.next)
    parent[0] = -1
    queue = collections.deque([0])
    while queue:
        state = queue.popleft()
        for code in range(26):
            char = chr(ord("a") + code)
            if char not in automaton.next[state]:
                answer = [char]
                while state:
                    answer.append(letter[state])
                    state = parent[state]
                print("".join(reversed(answer)))
                return
            target = automaton.next[state][char]
            if parent[target] is None:
                parent[target] = state
                letter[target] = char
                queue.append(target)


if __name__ == "__main__":
    main()
'''

CPP["kth_multi"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;long long k;cin>>s>>k;SAM a(s);a.occurrences();const long long CAP=4000000000000000000LL;auto o=a.order();vector<long long>dp(a.st.size());for(int z=(int)o.size()-1;z>=0;--z){int v=o[z];for(int u:a.st[v].next)if(u!=-1){long long add=min(CAP,a.st[u].occ+dp[u]);dp[v]=dp[v]>=CAP-add?CAP:dp[v]+add;}}if(k>dp[0]){cout<<"IMPOSSIBLE\n";return 0;}string ans;int v=0;while(true){for(int c=0;c<26;++c){int u=a.st[v].next[c];if(u==-1)continue;long long block=min(CAP,a.st[u].occ+dp[u]);if(k>block){k-=block;continue;}ans+=char('a'+c);if(k<=a.st[u].occ){cout<<ans<<'\n';return 0;}k-=a.st[u].occ;v=u;break;}}}
'''
PY["kth_multi"] = SAM_PY + r'''

def main():
    import sys
    raw_s, raw_k = sys.stdin.buffer.read().split()
    automaton = SAM(raw_s.decode())
    automaton.occurrences()
    k = int(raw_k)
    paths = [0] * len(automaton.next)
    for state in reversed(automaton.order()):
        paths[state] = sum(automaton.occ[target] + paths[target] for target in automaton.next[state].values())
    if k > paths[0]:
        print("IMPOSSIBLE")
        return
    answer = []
    state = 0
    while True:
        for char, target in sorted(automaton.next[state].items()):
            block = automaton.occ[target] + paths[target]
            if k > block:
                k -= block
                continue
            answer.append(char)
            if k <= automaton.occ[target]:
                print("".join(answer))
                return
            k -= automaton.occ[target]
            state = target
            break


if __name__ == "__main__":
    main()
'''

CPP["common_count"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string a,b;cin>>a>>b;SAM s(a);vector<int>best(s.st.size());int v=0,len=0;for(char ch:b){int c=ch-'a';while(v&&s.st[v].next[c]==-1)v=s.st[v].link,len=min(len,s.st[v].len);if(s.st[v].next[c]!=-1)v=s.st[v].next[c],++len;else v=0,len=0;best[v]=max(best[v],len);}auto o=s.order();for(int i=(int)o.size()-1;i;--i){int x=o[i],p=s.st[x].link;best[p]=max(best[p],min(best[x],s.st[p].len));}long long ans=0;for(int x=1;x<(int)s.st.size();++x)ans+=max(0,min(s.st[x].len,best[x])-s.st[s.st[x].link].len);cout<<ans<<'\n';}
'''
PY["common_count"] = SAM_PY + r'''

def main():
    import sys
    a, b = (part.decode() for part in sys.stdin.buffer.read().split())
    automaton = SAM(a)
    best = [0] * len(automaton.next)
    state = length = 0
    for char in b:
        while state and char not in automaton.next[state]:
            state = automaton.link[state]
            length = min(length, automaton.length[state])
        if char in automaton.next[state]:
            state = automaton.next[state][char]
            length += 1
        else:
            state = length = 0
        best[state] = max(best[state], length)
    for state in reversed(automaton.order()[1:]):
        parent = automaton.link[state]
        best[parent] = max(best[parent], min(best[state], automaton.length[parent]))
    answer = 0
    for state in range(1, len(automaton.next)):
        low = automaton.length[automaton.link[state]]
        answer += max(0, min(automaton.length[state], best[state]) - low)
    print(answer)


if __name__ == "__main__":
    main()
'''

CPP["pal_value"] = EERTREE_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;Eertree e;for(char c:s)e.add(c);vector<int>o(e.t.size());iota(o.begin(),o.end(),0);sort(o.begin(),o.end(),[&](int a,int b){return e.t[a].len<e.t[b].len;});long long ans=0;for(int i=(int)o.size()-1;i>=2;--i){int v=o[i];ans=max(ans,e.t[v].occ*e.t[v].len);e.t[e.t[v].link].occ+=e.t[v].occ;}cout<<ans<<'\n';}
'''
PY["pal_value"] = EERTREE_PY + r'''

def main():
    import sys
    tree = Eertree()
    for char in sys.stdin.buffer.readline().decode().strip():
        tree.add(char)
    order = sorted(range(2, len(tree.next)), key=tree.length.__getitem__, reverse=True)
    answer = 0
    for node in order:
        answer = max(answer, tree.length[node] * tree.occ[node])
        tree.occ[tree.link[node]] += tree.occ[node]
    print(answer)


if __name__ == "__main__":
    main()
'''

CPP["multi_lcs"] = SAM_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int m,k;cin>>m>>k;vector<string>a(m);for(auto&x:a)cin>>x;SAM s(a[0]);int z=s.st.size();vector<vector<int>>seen(z,vector<int>(m));for(int v=0;v<z;++v)seen[v][0]=s.st[v].len;auto order=s.order();for(int id=1;id<m;++id){vector<int>best(z);int v=0,len=0;for(char ch:a[id]){int c=ch-'a';while(v&&s.st[v].next[c]==-1)v=s.st[v].link,len=min(len,s.st[v].len);if(s.st[v].next[c]!=-1)v=s.st[v].next[c],++len;else v=0,len=0;best[v]=max(best[v],len);}for(int j=z-1;j;j--){int x=order[j],p=s.st[x].link;best[p]=max(best[p],min(best[x],s.st[p].len));}for(int x=0;x<z;++x)seen[x][id]=min(best[x],s.st[x].len);}int ans=0;for(int x=1;x<z;++x){nth_element(seen[x].begin(),seen[x].begin()+m-k,seen[x].end());ans=max(ans,seen[x][m-k]);}cout<<ans<<'\n';}
'''
PY["multi_lcs"] = SAM_PY + r'''

def main():
    import sys
    data = sys.stdin.buffer.read().split()
    m, k = map(int, data[:2])
    archives = [part.decode() for part in data[2:]]
    automaton = SAM(archives[0])
    states = len(automaton.next)
    seen = [[0] * m for _ in range(states)]
    for state in range(states):
        seen[state][0] = automaton.length[state]
    order = automaton.order()
    for archive_id, archive in enumerate(archives[1:], 1):
        best = [0] * states
        state = length = 0
        for char in archive:
            while state and char not in automaton.next[state]:
                state = automaton.link[state]
                length = min(length, automaton.length[state])
            if char in automaton.next[state]:
                state = automaton.next[state][char]
                length += 1
            else:
                state = length = 0
            best[state] = max(best[state], length)
        for state in reversed(order[1:]):
            parent = automaton.link[state]
            best[parent] = max(best[parent], min(best[state], automaton.length[parent]))
        for state in range(states):
            seen[state][archive_id] = min(best[state], automaton.length[state])
    print(max(sorted(values)[-k] for values in seen[1:]))


if __name__ == "__main__":
    main()
'''

TESTS = {
    "suffix_dump": [("banana\n", "6 4 2 1 5 3\n1 3 0 0 2\n"), ("a\n", "1\n\n")],
    "repeat_k": [("banana 2\n", "3\n"), ("abc 3\n", "0\n")],
    "pattern_queries": [("banana\n3\nana\nna\nx\n", "2\n2\n0\n")],
    "disjoint_repeat": [("aaaaa\n", "2\n"), ("abc\n", "0\n")],
    "kth_distinct": [("aba 4\n", "b\n"), ("a 2\n", "IMPOSSIBLE\n")],
    "lcs": [("abacaba bac\n", "3\n"), ("a z\n", "0\n")],
    "pal_profile": [("ababa\n", "1 1\n2 1\n3 3\n4 3\n5 5\n")],
    "absent_word": [("abc\n", "d\n"), ("abcdefghijklmnopqrstuvwxyz\n", "aa\n")],
    "rotation": [("baca\n", "abac\n4\n"), ("aaaa\n", "aaaa\n1\n")],
    "spectrum": [("banana\n", "6 3 1 0 0 0\n")],
    "kth_multi": [("aba 3\n", "ab\n"), ("a 2\n", "IMPOSSIBLE\n")],
    "common_count": [("aba bab\n", "4\n"), ("a z\n", "0\n")],
    "pal_value": [("ababa\n", "6\n"), ("a\n", "1\n")],
    "multi_lcs": [("3 2\nababc\nbabca\nzzabaz\n", "4\n"), ("2 2\na\nz\n", "0\n")],
}

LESSON_76 = r'''---
title: "Section 76 — Suffix Arrays And LCP Structure"
format: pdf
geometry: margin=1.8cm
fontsize: 10pt
---

## 1. Why sort suffixes?

A substring is a prefix of some suffix. After suffixes are sorted, all suffixes beginning with the same pattern form one contiguous interval. This single geometric fact turns substring questions into interval questions.

This lesson develops Problems A--C. Problem D is deliberately reserved for independent discovery and the editorial.

## 2. Problem A: build the order

A direct comparison of suffixes repeats work. Prefix doubling instead stores a rank for every block of length `2^h`. To rank length `2^(h+1)`, sort the pair

```text
(rank[i], rank[i + 2^h]).
```

The pair is a compressed model of the whole longer block: everything relevant to lexicographic comparison crosses the round boundary through two integer ranks.

After the suffix array, Kasai's algorithm computes adjacent LCP values. When moving from suffix `i` to suffix `i+1`, an already-known common prefix can shrink by at most one. Reusing that prefix makes the total number of successful character comparisons linear.

**Invariant.** At the start of doubling round `h`, equal ranks mean equal length-`2^h` prefixes, and rank order equals their lexicographic order.

Complexity here is `O(n log^2 n)` with comparison sorting and `O(n)` for Kasai. Counting/radix sorting reduces construction to `O(n log n)`.

## 3. Problem B: repeated at least k times

If a substring occurs in `k` suffixes, those suffixes occupy a contiguous suffix-array block. Their common prefix length is the minimum of the `k-1` adjacent LCP values inside the block. Therefore:

1. slide a window of `k-1` over the LCP array;
2. maintain its minimum with a monotone deque;
3. maximize that minimum.

The hard step is recognizing that a global collection of occurrences becomes a local contiguous block after sorting.

## 4. Problem C: pattern occurrence queries

For a pattern `p`, suffixes smaller than `p` come first, suffixes beginning with `p` form the answer interval, and greater suffixes follow. Two binary searches find the interval boundaries.

Do not compare `p` with an entire copied suffix. Compare characters in the original text, and treat “the pattern ended” as equality even if the suffix continues.

With ordinary comparisons, a query costs `O(|p| log n)`. More advanced LCP-aware searches can reduce repeated comparisons.

## 5. A reusable discovery checklist

- Is every candidate a prefix of some suffix?
- Does sorting make all witnesses contiguous?
- Is the answer over a suffix-array interval a minimum of adjacent LCPs?
- Are many neighboring interval minima required? Try a deque, RMQ, or offline DSU.
- Is feasibility monotone in a candidate length? Try binary search.

# Exercises

- A — construct suffix order and LCP.
- B — turn repeated occurrences into a sliding LCP minimum.
- C — turn a pattern into a suffix-array interval.
- D — new transfer problem; no lesson derivation is given.
'''

LESSON_77 = r'''---
title: "Section 77 — Suffix Automata And Palindromic Trees"
format: pdf
geometry: margin=1.8cm
fontsize: 10pt
---

## 1. Two compressed substring graphs

A suffix automaton (SAM) merges substrings having the same set of ending positions. Its transitions form a DAG because transition lengths strictly increase. A palindromic tree keeps one node per distinct palindrome and links it to its longest proper palindromic suffix.

This lesson develops Problems A--C. Problem D is intentionally explained only in the editorial.

## 2. Problem A: k-th distinct substring

Every nonempty path from the SAM root spells one distinct substring. Let `dp[v]` be the number of nonempty paths starting at state `v`:

```text
dp[v] = sum over transitions v -> u of (1 + dp[u]).
```

Process states by decreasing maximum length. For reconstruction, inspect outgoing letters in sorted order. A transition owns one substring ending immediately there, followed by all extensions below it. Subtract whole blocks until the block containing `k` is found.

The state is a compressed model: exponentially many substring occurrences collapse to at most `2n-1` end-position classes.

## 3. Problem B: longest common substring

Build the SAM of `a`, then scan `b`. Maintain a state and the length of the longest suffix of the scanned prefix that occurs in `a`. On a missing transition, follow suffix links until the character fits, shortening the current match to the new state's maximum length.

**Invariant.** After each scanned character, `length` is the longest suffix of the processed prefix of `b` represented by `state`.

Each suffix-link retreat can be amortized against progress, so the scan is linear.

## 4. Problem C: palindrome prefix profile

When one character is appended, at most one new distinct palindrome appears: every new palindrome must end at the new position, and only the longest new palindromic suffix can be new.

To add a character:

1. follow suffix links from the previous longest palindromic suffix until the new character also matches on its left;
2. reuse its transition if present;
3. otherwise create one node and compute its suffix link similarly.

The two roots of lengths `-1` and `0` remove parity special cases. The current node directly gives the longest palindromic suffix; nodes minus two gives the distinct count.

## 5. Choosing the structure

- Need lexicographic enumeration, suffix intervals, or LCP geometry: suffix array.
- Need online extension, occurrence classes, or path DP over all substrings: suffix automaton.
- Need one node per distinct palindrome and palindromic suffix links: palindromic tree.

# Exercises

- A — path counting and lexicographic reconstruction.
- B — streaming matches through suffix links.
- C — online palindromic suffix maintenance.
- D — a fresh automaton-graph problem reserved for the editorial.
'''

LESSON_78 = r'''---
title: "Section 78 — Master Suffix Structures Mixed Contest"
format: pdf
geometry: margin=1.8cm
fontsize: 10pt
---

## Contest contract

Six new problems mix suffix ordering, LCP connectivity, suffix-automaton path weights, cross-string propagation, and palindromic occurrence aggregation. They are not restatements of Sections 76--77.

Suggested order: A, D, E, B, C, F. Budget about five hours, then write a proof before reading the editorial.

## Coverage map

| Problem | Main pressure point |
|---|---|
| A | eliminate cyclic-rotation candidates in linear time |
| B | process every occurrence threshold through LCP edges and DSU |
| C | distinguish a substring from its many occurrences in SAM path DP |
| D | propagate the best match through suffix links |
| E | propagate palindrome occurrence counts |
| F | combine per-string SAM evidence with an order statistic |

## Post-contest questions

For each problem, identify the exact object represented by one state, the direction in which information must flow, why every candidate is counted, and why no candidate is counted twice.

# Exercises

Problems A--F in this section form the complete mixed contest.
'''

NOTES = {
    "suffix_dump": ("Replace suffix strings by ranks of power-of-two prefixes. Kasai then reuses all but the first character of the previous comparison.", "The doubling invariant proves the final ranks are the exact suffix order. Kasai compares the suffix preceding each suffix in that order, so every requested adjacent LCP is produced.", "`O(n log^2 n)` time and `O(n)` memory with comparison sorting."),
    "repeat_k": ("Sort the occurrence starts indirectly as suffixes. A length shared by `k` consecutive suffixes is exactly the minimum of the intervening LCP values.", "Every substring with `k` occurrences yields a block whose LCP minimum is at least its length. Conversely, a block minimum `L` makes the first `L` characters equal in all suffixes of that block.", "`O(n log^2 n)` construction and `O(n)` deque processing."),
    "pattern_queries": ("All suffixes prefixed by a fixed pattern are consecutive. Binary-search the first suffix not smaller than the pattern and the first suffix strictly greater under prefix comparison.", "The comparator partitions the sorted suffixes into smaller, matching, and greater groups. Their middle interval contains exactly all occurrence starts.", "`O(n log^2 n + sum |p| log n)` time and `O(n)` memory."),
    "disjoint_repeat": ("Binary-search the length. LCP values at least that length join maximal groups of suffixes sharing the candidate prefix; track the minimum and maximum starting positions in each group.", "Two equal occurrences are disjoint exactly when their starts differ by at least the tested length. The scan examines precisely every maximal equal-prefix group, so feasibility is exact and monotone.", "`O(n log^2 n + n log n)` time and `O(n)` memory."),
    "kth_distinct": ("View distinct substrings as nonempty paths from the SAM root. Count paths in reverse length order, then skip lexicographic transition blocks.", "Each distinct substring spells exactly one root path. Each outgoing transition partitions paths by their first next character, so block subtraction selects exactly the k-th path.", "`O(n log alphabet)` time and `O(n alphabet)` memory in the fixed-array implementation."),
    "lcs": ("Build a SAM for the first string and maintain the longest suffix of each scanned prefix of the second string that the automaton accepts.", "The scan invariant gives the longest common substring ending at every position of the second string. Taking the maximum therefore considers every possible endpoint.", "`O(|a|+|b|)` time and `O(|a| alphabet)` memory."),
    "pal_profile": ("A newly appended character can introduce only one new distinct palindrome: the longest palindromic suffix. Maintain it with palindromic suffix links.", "Every new occurrence ends at the appended position. Shorter palindromic suffixes already occurred as suffixes of the previous longest one; creation of exactly the missing longest node is therefore necessary and sufficient.", "`O(n alphabet)` stored transitions and amortized `O(n)` traversal."),
    "absent_word": ("A word is a substring exactly when it labels a SAM root path. Breadth-first search those paths in letter order and stop at the first missing transition.", "BFS processes path labels by increasing length and, within a level, lexicographic order. A missing next edge certifies absence, so the first such label meets both tie-breaks.", "`O(n alphabet)` time and memory."),
    "rotation": ("Compare two candidate starts and skip every start inside the losing matched block; none can beat the winner. This is Booth's elimination argument.", "After a mismatch at offset `k`, the losing candidate and the next `k` starts have the same obstructing prefix relation and cannot be minimal. Thus discarded starts are safe, and one survivor is globally minimal.", "`O(n)` time and `O(1)` auxiliary memory."),
    "spectrum": ("Treat adjacent suffix-array positions as edges weighted by LCP. Add edges from high to low; a DSU component of size `k` certifies a prefix occurring in those `k` suffixes.", "At threshold `L`, components are exactly maximal groups connected by LCP values at least `L`, hence exactly groups sharing a length-`L` prefix. Recording merge sizes and suffix-maximizing over `k` gives every at-least threshold.", "`O(n log n)` after suffix-array construction and `O(n)` memory."),
    "kth_multi": ("A SAM path still identifies a distinct substring, but its terminal state's occurrence count is the multiplicity of that path label. Weight each path endpoint by this count.", "Transition blocks partition the sorted multiset by next letter. Within a block, the immediate label contributes `occ[target]` copies before all longer extensions, exactly matching lexicographic multiset order.", "`O(n alphabet)` time and memory, with saturated 64-bit counts."),
    "common_count": ("While scanning the second string, record the best accepted match ending in each SAM state, then propagate capped values down suffix links.", "A state represents all lengths from `len(link)+1` through `len(state)`. After propagation, precisely the lengths up to `best[state]` occur in both strings, giving the stated interval contribution without duplication.", "`O(|a|+|b|)` time apart from fixed transition initialization."),
    "pal_value": ("Create one node per palindrome, count visits to the current longest suffix, then propagate counts from longer nodes to their palindromic suffix links.", "Every occurrence is first credited to the longest palindromic suffix at its endpoint. Suffix-link propagation credits that endpoint to every shorter palindromic suffix exactly once.", "`O(n alphabet)` memory and amortized `O(n)` traversal."),
    "multi_lcs": ("Use the first archive's SAM as the candidate universe. For every other archive, scan matches and suffix-link-propagate the maximum supported length per state. The k-th largest archive support is that state's feasible length.", "Every common candidate occurs in the first archive and belongs to one state. Per-archive propagation computes its maximum valid length; requiring at least `k` archives is exactly taking the k-th largest support.", "`O(total length + m n + m n log m)` with `m <= 20`, and `O(mn)` memory."),
}


def checker(section: int, slugs: list[str]) -> str:
    quoted = ",\n        ".join(f'"{slug}"' for slug in slugs)
    return f'''"""Friendly checker for Section {section}."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        {quoted},
    )
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks({section}, PROBLEMS, ROOT))
'''


def editorial(section: int) -> str:
    title = SECTIONS[section][1]
    chunks = [f'''---
title: "Section {section} Editorial — {title}"
format: pdf
geometry: margin=1.65cm
fontsize: 9pt
---

Each solution starts from the uncompressed object, identifies the bottleneck, and states the invariant that justifies the compressed structure.
''']
    for number, (slug, name, kind) in enumerate(PROBLEMS[section], 1):
        find, proof, complexity = NOTES[kind]
        letter = chr(64 + number)
        chunks.append(f'''# {letter}. {name}

### How to find it

{find}

### Correctness

{proof}

### Complexity

{complexity}

### Reference C++

```cpp
{{{{< include problems/{slug}/solution.cpp >}}}}
```

### Reference Python

```python
{{{{< include problems/{slug}/solution.py >}}}}
```
''')
    return "\n".join(chunks)


def section_readme(section: int) -> str:
    slug, title = SECTIONS[section]
    listing = "\n".join(
        f"{chr(65+i)}. [{name}](problems/{problem}/README.md)"
        for i, (problem, name, _) in enumerate(PROBLEMS[section])
    )
    special = (
        "The lesson explicitly teaches A--C; D is a transfer exercise whose derivation appears only in the editorial."
        if section in (76, 77)
        else "This mixed contest contains exactly six new problems."
    )
    return f'''# Section {section}: {title}

{special}

## Material

- [Lesson](lesson.qmd)
- [Editorial](editorial.qmd)
- [Practice checklist](PRACTICE.md)

## Problems

{listing}

Run `python3 check.py --keep-going` to test every attempted solution, or add a problem letter/slug to select one exercise.
'''


def practice(section: int) -> str:
    lines = [f"# Section {section} Practice", ""]
    for slug, name, _ in PROBLEMS[section]:
        lines.append(f"- [ ] [{name}](problems/{slug}/README.md)")
    lines += ["", "After solving, write the state meaning, transition invariant, proof, and complexity before opening the editorial.", ""]
    return "\n".join(lines)


def manifest(section: int, title: str) -> dict:
    return {
        "section": section,
        "title": title,
        "checker": "tokens",
        "time_limit_seconds": 7,
    }


def generate() -> None:
    lesson = {76: LESSON_76, 77: LESSON_77, 78: LESSON_78}
    for section, (directory, _) in SECTIONS.items():
        base = ROOT / "sections" / f"{section:02d}_{directory}"
        base.mkdir(parents=True, exist_ok=True)
        (base / "lesson.qmd").write_text(lesson[section], encoding="utf-8")
        (base / "editorial.qmd").write_text(editorial(section), encoding="utf-8")
        (base / "README.md").write_text(section_readme(section), encoding="utf-8")
        (base / "PRACTICE.md").write_text(practice(section), encoding="utf-8")
        slugs = [slug for slug, _, _ in PROBLEMS[section]]
        (base / "check.py").write_text(checker(section, slugs), encoding="utf-8")
        for slug, name, kind in PROBLEMS[section]:
            problem = base / "problems" / slug
            problem.mkdir(parents=True, exist_ok=True)
            (problem / "README.md").write_text(f"# {name}\n\n{STATEMENTS[kind]}\n", encoding="utf-8")
            (problem / "solve.cpp").write_text(CPP_STUB, encoding="utf-8")
            (problem / "solve.py").write_text(PY_STUB, encoding="utf-8")
            (problem / "solution.cpp").write_text(CPP[kind], encoding="utf-8")
            (problem / "solution.py").write_text(PY[kind], encoding="utf-8")
            (problem / "manifest.json").write_text(json.dumps(manifest(section, name), indent=2) + "\n", encoding="utf-8")
            tests = problem / "tests"
            tests.mkdir(exist_ok=True)
            for number, (input_text, output_text) in enumerate(TESTS[kind], 1):
                (tests / f"sample{number}.in").write_text(input_text, encoding="utf-8")
                (tests / f"sample{number}.out").write_text(output_text, encoding="utf-8")
            wrapper = f'''import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(
    subprocess.call(
        [sys.executable, str(ROOT / "tools" / "suffix_structures_random.py"), "{kind}", *sys.argv[1:]]
    )
)
'''
            (tests / "random_cases.py").write_text(wrapper, encoding="utf-8")


if __name__ == "__main__":
    generate()
