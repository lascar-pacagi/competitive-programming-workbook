"""Generate Sections 79--81: advanced graph decomposition."""

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
    79: ("directed_graph_decomposition", "Directed Graph Decomposition"),
    80: ("undirected_connectivity_decomposition", "Undirected Connectivity Decomposition"),
    81: ("master_graph_decomposition_mixed", "Master Graph Decomposition Mixed Contest"),
}

PROBLEMS = {
    79: [
        ("a_condensation_profile", "Condensation Profile", "condensation"),
        ("b_clause_satisfiability", "Clause Satisfiability", "twosat"),
        ("c_lexicographic_euler_trail", "Lexicographic Euler Trail", "euler"),
        ("d_unavoidable_checkpoints", "Unavoidable Checkpoints", "dominators"),
    ],
    80: [
        ("a_bridge_distance_queries", "Bridge Distance Queries", "bridge_distance"),
        ("b_articulation_pair_damage", "Articulation Pair Damage", "articulation_damage"),
        ("c_mandatory_station_queries", "Mandatory Station Queries", "mandatory"),
        ("d_two_edge_completion", "Two-Edge Connectivity Completion", "bridge_completion"),
    ],
    81: [
        ("a_unique_sink_population", "Unique Sink Population", "sink_size"),
        ("b_strong_connectivity_repairs", "Strong Connectivity Repairs", "strong_repairs"),
        ("c_eulerian_word_chain", "Eulerian Word Chain", "word_chain"),
        ("d_robbins_orientation", "Robbins Orientation", "robbins"),
        ("e_failed_vertex_routes", "Failed Vertex Routes", "failed_vertex"),
        ("f_dominator_subtree_queries", "Dominator Subtree Queries", "dominator_subtree"),
    ],
}

STATEMENTS = {
    "condensation": """Given a directed graph, contract every strongly connected component. Print the number of components, the number with indegree zero, and the number with outdegree zero in the resulting condensation DAG.

Input: `n m`, followed by `m` directed edges. `1 <= n <= 200000` and
`0 <= m <= 200000`.

Sample input
```text
4 4
1 2
2 1
2 3
3 4
```
Sample output
```text
3 1 1
```""",
    "twosat": """There are `n` Boolean variables and `m` clauses. A literal is a signed integer: `x` means variable `x` is true and `-x` means it is false. Decide whether all clauses `(a OR b)` can hold simultaneously.

Input: `n m`, then the two literals of each clause; `n,m <= 200000`.

Output: `YES` or `NO`.

Sample input
```text
2 3
1 2
-1 2
-2 1
```
Sample output
```text
YES
```""",
    "euler": """A directed multigraph is given. Find the lexicographically smallest vertex sequence of an Euler trail that starts at vertex `1` and uses every edge exactly once. Parallel edges and loops are allowed.

Input: `n m`, then `m` directed edges; `n,m <= 200000`.

Output the `m+1` vertices, or `IMPOSSIBLE`.

Sample input
```text
3 3
1 2
2 1
1 3
```
Sample output
```text
1 2 1 3
```""",
    "dominators": """In a directed graph, vertex `1` is the entrance and vertex `n` is reachable. Print all vertices other than `1` and `n` that occur on every directed path from `1` to `n`.

Input: `n m`, followed by directed edges. `2 <= n <= 1500`, `m <= 10000`.

Output the count and then the sorted vertices.

Sample input
```text
5 6
1 2
1 3
2 4
3 4
4 5
2 3
```
Sample output
```text
1
4
```""",
    "bridge_distance": """A connected undirected multigraph is given. For every query `(u,v)`, report how many bridges must be crossed by every path from `u` to `v`.

Input: `n m q`, `m` edges, then `q` queries. `n,m,q <= 200000`.

Sample input
```text
4 4 2
1 2
2 3
3 1
3 4
1 4
1 2
```
Sample output
```text
1
0
```""",
    "articulation_damage": """For every vertex `v` of a connected undirected graph, remove `v` and its incident edges. Count unordered pairs of remaining vertices that become disconnected. Print all `n` counts.

Input: `n m`, then `m` undirected edges; `n,m <= 200000`.

Sample input
```text
4 3
1 2
2 3
2 4
```
Sample output
```text
0 3 0 0
```""",
    "mandatory": """For each query `(u,v,c)` in a connected undirected graph, answer whether every path from `u` to `v` contains `c`. Endpoints count as contained.

Input: `n m q`, the edges, then the queries; all bounds are `200000`.

Output `YES` or `NO` per query.

Sample input
```text
4 3 2
1 2
2 3
2 4
1 3 2
3 4 1
```
Sample output
```text
YES
NO
```""",
    "bridge_completion": """A connected undirected multigraph is given. Add the fewest new edges between distinct vertices so that the resulting graph has no bridge. Parallel new edges are allowed.

Input: `n m`, followed by edges; `n,m <= 200000`.

Output the minimum number of edges.

Sample input
```text
4 3
1 2
2 3
3 4
```
Sample output
```text
1
```""",
    "sink_size": """People pass information along directed edges. Print the size of the unique strongly connected component from which no edge leaves to another component. If there is not exactly one such component, print `0`.

Input: `n m`, then directed edges; `n,m <= 200000`.

Sample input
```text
4 4
1 2
2 1
2 3
4 3
```
Sample output
```text
1
```""",
    "strong_repairs": """Add the minimum number of directed edges to make a directed graph strongly connected.

Input: `n m` and directed edges; `n,m <= 200000`.

Output the minimum number.

Sample input
```text
4 2
1 2
3 4
```
Sample output
```text
2
```""",
    "word_chain": """Each lowercase word is a directed edge from its first letter to its last. Order all words so consecutive words join. Among valid orders, print the lexicographically smallest sequence of words. Words are distinct.

Input: `n`, then `n` lowercase words; total length <= 200000.

Output the words on one line or `IMPOSSIBLE`.

Sample input
```text
3
ab
ba
ac
```
Sample output
```text
ab ba ac
```""",
    "robbins": """Decide whether every edge of a connected undirected multigraph can be oriented so that the directed graph is strongly connected.

Input: `n m`, then edges; `n,m <= 200000`.

Output `YES` or `NO`.

Sample input
```text
3 3
1 2
2 3
3 1
```
Sample output
```text
YES
```""",
    "failed_vertex": """For each `(u,v,c)`, vertex `c` fails. Answer whether `u` and `v` remain connected. Queries with `c=u` or `c=v` have answer `NO`.

Input: a connected undirected graph as `n m q`, its edges, then queries; bounds `200000`.

Sample input
```text
4 3 2
1 2
2 3
2 4
3 4 2
1 3 4
```
Sample output
```text
NO
YES
```""",
    "dominator_subtree": """All vertices are reachable from root `1` in a directed graph. For every query vertex `v`, print how many vertices `x` have the property that every path from `1` to `x` passes through `v`.

Input: `n m q`, directed edges, then query vertices. `n <= 1500`,
`m <= 10000`, and `q <= 200000`.

Sample input
```text
5 5 2
1 2
1 3
2 4
3 4
4 5
4
1
```
Sample output
```text
2
5
```""",
}

PY_COMMON = r'''import sys
from array import array
sys.setrecursionlimit(1_000_000)


def scc(n, edges):
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        reverse[v].append(u)
    seen = [False] * n
    order = []
    for start in range(n):
        if seen[start]:
            continue
        stack = [(start, 0)]
        seen[start] = True
        while stack:
            node, index = stack[-1]
            if index < len(graph[node]):
                target = graph[node][index]
                stack[-1] = (node, index + 1)
                if not seen[target]:
                    seen[target] = True
                    stack.append((target, 0))
            else:
                order.append(node)
                stack.pop()
    component = [-1] * n
    count = 0
    for start in reversed(order):
        if component[start] != -1:
            continue
        component[start] = count
        stack = [start]
        while stack:
            node = stack.pop()
            for target in reverse[node]:
                if component[target] == -1:
                    component[target] = count
                    stack.append(target)
        count += 1
    return component, count


def undirected_lowlink(n, edges):
    graph = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
    tin = [-1] * n
    low = [0] * n
    subtree = [0] * n
    bridges = [False] * len(edges)
    separating = [[] for _ in range(n)]
    timer = 0

    def dfs(node, parent_edge=-1):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        subtree[node] = 1
        for target, edge_id in graph[node]:
            if edge_id == parent_edge:
                continue
            if tin[target] != -1:
                low[node] = min(low[node], tin[target])
            else:
                dfs(target, edge_id)
                subtree[node] += subtree[target]
                low[node] = min(low[node], low[target])
                if low[target] > tin[node]:
                    bridges[edge_id] = True
                if low[target] >= tin[node]:
                    separating[node].append(subtree[target])

    dfs(0)
    return graph, tin, low, subtree, bridges, separating


def bridge_tree(n, edges):
    graph, _, _, _, bridges, _ = undirected_lowlink(n, edges)
    component = [-1] * n
    count = 0
    for start in range(n):
        if component[start] != -1:
            continue
        component[start] = count
        stack = [start]
        while stack:
            node = stack.pop()
            for target, edge_id in graph[node]:
                if not bridges[edge_id] and component[target] == -1:
                    component[target] = count
                    stack.append(target)
        count += 1
    tree = [[] for _ in range(count)]
    for edge_id, (u, v) in enumerate(edges):
        if bridges[edge_id]:
            a, b = component[u], component[v]
            tree[a].append(b)
            tree[b].append(a)
    return component, tree


def tree_lca(tree):
    size = len(tree)
    levels = max(1, size.bit_length())
    up = [array("i", [0]) * size for _ in range(levels)]
    depth = [0] * size
    stack = [(0, 0)]
    order = [0]
    while stack:
        node, parent = stack.pop()
        up[0][node] = parent
        for target in tree[node]:
            if target != parent:
                depth[target] = depth[node] + 1
                order.append(target)
                stack.append((target, node))
    for level in range(1, levels):
        previous = up[level - 1]
        up[level] = array(
            "i", (previous[previous[node]] for node in range(size))
        )

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        difference = depth[a] - depth[b]
        for level in range(levels):
            if difference >> level & 1:
                a = up[level][a]
        if a == b:
            return a
        for level in range(levels - 1, -1, -1):
            if up[level][a] != up[level][b]:
                a, b = up[level][a], up[level][b]
        return up[0][a]

    def distance(a, b):
        ancestor = lca(a, b)
        return depth[a] + depth[b] - 2 * depth[ancestor]

    return distance


def block_cut_tree(n, edges):
    graph = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
    tin = [-1] * n
    low = [0] * n
    edge_stack = []
    tree = [[] for _ in range(n)]
    timer = 0

    def dfs(node, parent_edge=-1):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        for target, edge_id in graph[node]:
            if edge_id == parent_edge:
                continue
            if tin[target] == -1:
                edge_stack.append(edge_id)
                dfs(target, edge_id)
                low[node] = min(low[node], low[target])
                if low[target] >= tin[node]:
                    vertices = set()
                    while True:
                        taken = edge_stack.pop()
                        vertices.update(edges[taken])
                        if taken == edge_id:
                            break
                    block = len(tree)
                    tree.append([])
                    for vertex in vertices:
                        tree[block].append(vertex)
                        tree[vertex].append(block)
            elif tin[target] < tin[node]:
                edge_stack.append(edge_id)
                low[node] = min(low[node], tin[target])

    dfs(0)
    return tree


def dominators(n, edges):
    predecessors = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        predecessors[v].append(u)
    reachable = 1
    stack = [0]
    while stack:
        node = stack.pop()
        for target in graph[node]:
            if not (reachable >> target & 1):
                reachable |= 1 << target
                stack.append(target)
    dom = [reachable] * n
    dom[0] = 1
    changed = True
    while changed:
        changed = False
        for node in range(1, n):
            if not (reachable >> node & 1):
                continue
            value = reachable
            for parent in predecessors[node]:
                if reachable >> parent & 1:
                    value &= dom[parent]
            value |= 1 << node
            if value != dom[node]:
                dom[node] = value
                changed = True
    return dom
'''

PY = {}

PY["condensation"] = PY_COMMON + r'''
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    edges = [(data[i] - 1, data[i + 1] - 1) for i in range(2, 2 + 2 * m, 2)]
    component, count = scc(n, edges)
    indegree, outdegree = [0] * count, [0] * count
    for u, v in edges:
        if component[u] != component[v]:
            outdegree[component[u]] = 1
            indegree[component[v]] = 1
    print(count, indegree.count(0), outdegree.count(0))
if __name__ == "__main__": main()
'''

PY["twosat"] = PY_COMMON + r'''
def main():
    data = list(map(int, sys.stdin.buffer.read().split())); n, m = data[:2]; edges = []
    def node(x): return 2 * (abs(x) - 1) + (x < 0)
    for i in range(2, 2 + 2 * m, 2):
        a, b = node(data[i]), node(data[i + 1]); edges.extend(((a ^ 1, b), (b ^ 1, a)))
    component, _ = scc(2 * n, edges)
    print("YES" if all(component[2*i] != component[2*i+1] for i in range(n)) else "NO")
if __name__ == "__main__": main()
'''

PY["euler"] = PY_COMMON + r'''
def main():
    data = list(map(int, sys.stdin.buffer.read().split())); n, m = data[:2]; graph=[[] for _ in range(n)]; indeg=[0]*n; out=[0]*n
    for i in range(2,2+2*m,2): u,v=data[i]-1,data[i+1]-1;graph[u].append(v);out[u]+=1;indeg[v]+=1
    for row in graph: row.sort(reverse=True)
    if m == 0: print(1); return
    plus=[v for v in range(n) if out[v]-indeg[v]==1];minus=[v for v in range(n) if indeg[v]-out[v]==1]
    valid=all(abs(out[v]-indeg[v])<=1 for v in range(n)) and ((not plus and not minus and out[0]) or (plus==[0] and len(minus)==1))
    if not valid: print("IMPOSSIBLE"); return
    stack=[0];path=[]
    while stack:
        if graph[stack[-1]]: stack.append(graph[stack[-1]].pop())
        else: path.append(stack.pop())
    if len(path)!=m+1: print("IMPOSSIBLE")
    else: print(*(x+1 for x in reversed(path)))
if __name__ == "__main__": main()
'''

PY["dominators"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];dom=dominators(n,edges)
    answer=[v+1 for v in range(1,n-1) if dom[n-1]>>v&1];print(len(answer));print(*answer)
if __name__ == "__main__": main()
'''

PY["bridge_distance"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m,q=data[:3];at=3;edges=[(data[i]-1,data[i+1]-1) for i in range(at,at+2*m,2)];at+=2*m;component,tree=bridge_tree(n,edges);distance=tree_lca(tree);print("\n".join(str(distance(component[data[i]-1],component[data[i+1]-1])) for i in range(at,at+2*q,2)))
if __name__ == "__main__": main()
'''

PY["articulation_damage"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];*_,separating=undirected_lowlink(n,edges);answer=[]
    for v in range(n):
        groups=separating[v];rest=n-1-sum(groups);seen=0;value=0
        for size in groups+[rest]: value+=seen*size;seen+=size
        answer.append(value)
    print(*answer)
if __name__ == "__main__": main()
'''

PY["mandatory"] = PY_COMMON + r'''
def main():
    data=array("i",map(int,sys.stdin.buffer.read().split()));n,m,q=data[:3];at=3;edges=[(data[i]-1,data[i+1]-1) for i in range(at,at+2*m,2)];at+=2*m;tree=block_cut_tree(n,edges);del edges;distance=tree_lca(tree);del tree;out=[]
    for i in range(at,at+3*q,3):
        u,v,c=data[i]-1,data[i+1]-1,data[i+2]-1;out.append("YES" if distance(u,v)==distance(u,c)+distance(c,v) else "NO")
    print("\n".join(out))
if __name__ == "__main__": main()
'''

PY["bridge_completion"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];_,tree=bridge_tree(n,edges);leaves=sum(len(row)==1 for row in tree);print((leaves+1)//2)
if __name__ == "__main__": main()
'''

PY["sink_size"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];component,count=scc(n,edges);out=[0]*count;size=[0]*count
    for v in range(n):size[component[v]]+=1
    for u,v in edges:
        if component[u]!=component[v]:out[component[u]]=1
    sinks=[c for c in range(count) if not out[c]];print(size[sinks[0]] if len(sinks)==1 else 0)
if __name__ == "__main__": main()
'''

PY["strong_repairs"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];component,count=scc(n,edges)
    if count==1:print(0);return
    inside=[0]*count;outside=[0]*count
    for u,v in edges:
        if component[u]!=component[v]:outside[component[u]]=inside[component[v]]=1
    print(max(inside.count(0),outside.count(0)))
if __name__ == "__main__": main()
'''

PY["word_chain"] = PY_COMMON + r'''
def main():
    words=sys.stdin.buffer.read().decode().split();n=int(words[0]);words=words[1:];graph=[[] for _ in range(26)];indeg=[0]*26;out=[0]*26
    for word in words:u=ord(word[0])-97;v=ord(word[-1])-97;graph[u].append((word,v));out[u]+=1;indeg[v]+=1
    starts=[v for v in range(26) if out[v]==indeg[v]+1];ends=[v for v in range(26) if indeg[v]==out[v]+1]
    if len(starts)>1 or len(ends)>1 or len(starts)!=len(ends):print("IMPOSSIBLE");return
    start=starts[0] if starts else next((v for v in range(26) if out[v]),0)
    for row in graph:row.sort(reverse=True)
    stack=[(start,None)];answer=[]
    while stack:
        v,_=stack[-1]
        if graph[v]:word,to=graph[v].pop();stack.append((to,word))
        else:
            _,word=stack.pop()
            if word is not None:answer.append(word)
    if len(answer)!=n:print("IMPOSSIBLE")
    else:print(*reversed(answer))
if __name__ == "__main__": main()
'''

PY["robbins"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m=data[:2];edges=[(data[i]-1,data[i+1]-1) for i in range(2,2+2*m,2)];*_,bridges,_=undirected_lowlink(n,edges);print("NO" if any(bridges) else "YES")
if __name__ == "__main__": main()
'''

PY["failed_vertex"] = PY_COMMON + r'''
def main():
    data=array("i",map(int,sys.stdin.buffer.read().split()));n,m,q=data[:3];at=3;edges=[(data[i]-1,data[i+1]-1) for i in range(at,at+2*m,2)];at+=2*m;tree=block_cut_tree(n,edges);del edges;distance=tree_lca(tree);del tree;out=[]
    for i in range(at,at+3*q,3):
        u,v,c=data[i]-1,data[i+1]-1,data[i+2]-1;bad=c in (u,v) or distance(u,v)==distance(u,c)+distance(c,v);out.append("NO" if bad else "YES")
    print("\n".join(out))
if __name__ == "__main__": main()
'''

PY["dominator_subtree"] = PY_COMMON + r'''
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));n,m,q=data[:3];at=3;edges=[(data[i]-1,data[i+1]-1) for i in range(at,at+2*m,2)];at+=2*m;dom=dominators(n,edges);size=[0]*n
    for target in range(n):
        bits=dom[target]
        while bits:bit=bits&-bits;size[bit.bit_length()-1]+=1;bits-=bit
    print("\n".join(str(size[data[i]-1]) for i in range(at,at+q)))
if __name__ == "__main__": main()
'''

CPP_COMMON = r'''#include <bits/stdc++.h>
using namespace std;
struct SCC{int n,c=0;vector<vector<int>>g,rg;vector<int>id,order;SCC(int n,vector<pair<int,int>>e):n(n),g(n),rg(n),id(n,-1){for(auto[u,v]:e)g[u].push_back(v),rg[v].push_back(u);vector<char>seen(n);for(int s=0;s<n;s++)if(!seen[s]){vector<pair<int,int>>st={{s,0}};seen[s]=1;while(!st.empty()){auto&[u,i]=st.back();if(i<(int)g[u].size()){int v=g[u][i++];if(!seen[v])seen[v]=1,st.push_back({v,0});}else order.push_back(u),st.pop_back();}}reverse(order.begin(),order.end());for(int s:order)if(id[s]<0){id[s]=c;vector<int>st={s};while(!st.empty()){int u=st.back();st.pop_back();for(int v:rg[u])if(id[v]<0)id[v]=c,st.push_back(v);}c++;}}};
struct LowLink{int n,timer=0;vector<pair<int,int>>e;vector<vector<pair<int,int>>>g;vector<int>tin,low,sub,parent_edge,it;vector<char>bridge;vector<vector<int>>parts;LowLink(int n,vector<pair<int,int>>e):n(n),e(e),g(n),tin(n,-1),low(n),sub(n),parent_edge(n,-1),it(n),bridge(e.size()),parts(n){for(int i=0;i<(int)e.size();i++){auto[u,v]=e[i];g[u].push_back({v,i});g[v].push_back({u,i});}tin[0]=low[0]=timer++;sub[0]=1;vector<int>st={0};while(!st.empty()){int u=st.back();if(it[u]<(int)g[u].size()){auto[v,id]=g[u][it[u]++];if(id==parent_edge[u])continue;if(tin[v]>=0)low[u]=min(low[u],tin[v]);else{parent_edge[v]=id;tin[v]=low[v]=timer++;sub[v]=1;st.push_back(v);}}else{st.pop_back();int id=parent_edge[u];if(id<0)continue;auto[a,b]=e[id];int p=a^b^u;sub[p]+=sub[u];low[p]=min(low[p],low[u]);if(low[u]>tin[p])bridge[id]=1;if(low[u]>=tin[p])parts[p].push_back(sub[u]);}}}};
pair<vector<int>,vector<vector<int>>> bridge_tree(int n,const vector<pair<int,int>>&e){LowLink l(n,e);vector<int>id(n,-1);int c=0;for(int s=0;s<n;s++)if(id[s]<0){id[s]=c;vector<int>st={s};while(!st.empty()){int u=st.back();st.pop_back();for(auto[v,k]:l.g[u])if(!l.bridge[k]&&id[v]<0)id[v]=c,st.push_back(v);}c++;}vector<vector<int>>t(c);for(int i=0;i<(int)e.size();i++)if(l.bridge[i]){auto[u,v]=e[i];u=id[u];v=id[v];t[u].push_back(v);t[v].push_back(u);}return{id,t};}
struct TreeDistance{int n,L;vector<int>d;vector<vector<int>>up;TreeDistance(vector<vector<int>>t):n(t.size()),L(max(1,(int)bit_width((unsigned)max(1,n)))),d(n),up(L,vector<int>(n)){vector<pair<int,int>>st={{0,0}};while(!st.empty()){auto[u,p]=st.back();st.pop_back();up[0][u]=p;for(int v:t[u])if(v!=p)d[v]=d[u]+1,st.push_back({v,u});}for(int j=1;j<L;j++)for(int i=0;i<n;i++)up[j][i]=up[j-1][up[j-1][i]];}int lca(int a,int b){if(d[a]<d[b])swap(a,b);int z=d[a]-d[b];for(int j=0;j<L;j++)if(z>>j&1)a=up[j][a];if(a==b)return a;for(int j=L-1;j>=0;j--)if(up[j][a]!=up[j][b])a=up[j][a],b=up[j][b];return up[0][a];}int dist(int a,int b){int c=lca(a,b);return d[a]+d[b]-2*d[c];}};
vector<vector<int>> block_cut(int n,const vector<pair<int,int>>&e){vector<vector<pair<int,int>>>g(n);for(int i=0;i<(int)e.size();i++){auto[u,v]=e[i];g[u].push_back({v,i});g[v].push_back({u,i});}vector<int>tin(n,-1),low(n),edges,parent(n,-1),it(n);vector<vector<int>>t(n);int timer=0;tin[0]=low[0]=timer++;vector<int>dfs={0};while(!dfs.empty()){int u=dfs.back();if(it[u]<(int)g[u].size()){auto[v,id]=g[u][it[u]++];if(id==parent[u])continue;if(tin[v]<0){parent[v]=id;edges.push_back(id);tin[v]=low[v]=timer++;dfs.push_back(v);}else if(tin[v]<tin[u])edges.push_back(id),low[u]=min(low[u],tin[v]);}else{dfs.pop_back();int id=parent[u];if(id<0)continue;auto[a,b]=e[id];int p=a^b^u;low[p]=min(low[p],low[u]);if(low[u]>=tin[p]){vector<int>vs;while(1){int x=edges.back();edges.pop_back();vs.push_back(e[x].first);vs.push_back(e[x].second);if(x==id)break;}sort(vs.begin(),vs.end());vs.erase(unique(vs.begin(),vs.end()),vs.end());int block=t.size();t.push_back({});for(int x:vs)t[block].push_back(x),t[x].push_back(block);}}}return t;}
vector<bitset<1500>> dominators(int n,const vector<pair<int,int>>&e){vector<vector<int>>g(n),pred(n);for(auto[u,v]:e)g[u].push_back(v),pred[v].push_back(u);bitset<1500>reach;reach[0]=1;vector<int>st={0};while(!st.empty()){int u=st.back();st.pop_back();for(int v:g[u])if(!reach[v])reach[v]=1,st.push_back(v);}vector<bitset<1500>>d(n,reach);d[0].reset();d[0][0]=1;bool change=1;while(change){change=0;for(int v=1;v<n;v++)if(reach[v]){bitset<1500>x=reach;for(int p:pred[v])if(reach[p])x&=d[p];x[v]=1;if(x!=d[v])d[v]=x,change=1;}}return d;}
'''

CPP = {}
CPP["condensation"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;SCC s(n,e);vector<char>in(s.c),out(s.c);for(auto[u,v]:e)if(s.id[u]!=s.id[v])out[s.id[u]]=in[s.id[v]]=1;cout<<s.c<<' '<<count(in.begin(),in.end(),0)<<' '<<count(out.begin(),out.end(),0)<<'\n';}'''
CPP["twosat"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e;auto node=[](int x){return 2*(abs(x)-1)+(x<0);};while(m--){int x,y;cin>>x>>y;int a=node(x),b=node(y);e.push_back({a^1,b});e.push_back({b^1,a});}SCC s(2*n,e);for(int i=0;i<n;i++)if(s.id[2*i]==s.id[2*i+1]){cout<<"NO\n";return 0;}cout<<"YES\n";}'''
CPP["euler"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<vector<int>>g(n);vector<int>in(n),out(n);for(int i=0,u,v;i<m;i++)cin>>u>>v,--u,--v,g[u].push_back(v),out[u]++,in[v]++;if(!m){cout<<1<<'\n';return 0;}vector<int>plus,minus;for(int v=0;v<n;v++){if(out[v]-in[v]==1)plus.push_back(v);else if(in[v]-out[v]==1)minus.push_back(v);else if(in[v]!=out[v]){cout<<"IMPOSSIBLE\n";return 0;}}if(!((plus.empty()&&minus.empty()&&out[0])||(plus==vector<int>{0}&&minus.size()==1))){cout<<"IMPOSSIBLE\n";return 0;}for(auto&v:g)sort(v.rbegin(),v.rend());vector<int>st={0},ans;while(!st.empty()){int u=st.back();if(g[u].empty())ans.push_back(u),st.pop_back();else{int v=g[u].back();g[u].pop_back();st.push_back(v);}}if((int)ans.size()!=m+1)cout<<"IMPOSSIBLE\n";else{reverse(ans.begin(),ans.end());for(int i=0;i<=m;i++)cout<<ans[i]+1<<" \n"[i==m];}}'''
CPP["dominators"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;auto d=dominators(n,e);vector<int>a;for(int v=1;v+1<n;v++)if(d[n-1][v])a.push_back(v+1);cout<<a.size()<<'\n';for(int x:a)cout<<x<<' ';cout<<'\n';}'''
CPP["bridge_distance"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;auto[id,t]=bridge_tree(n,e);TreeDistance d(t);while(q--){int u,v;cin>>u>>v;cout<<d.dist(id[--u],id[--v])<<'\n';}}'''
CPP["articulation_damage"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;LowLink l(n,e);for(int v=0;v<n;v++){long long ans=0,seen=0,sum=0;for(int z:l.parts[v])ans+=seen*z,seen+=z,sum+=z;long long rest=n-1-sum;ans+=seen*rest;cout<<ans<<" \n"[v+1==n];}}'''
CPP["mandatory"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;TreeDistance d(block_cut(n,e));while(q--){int u,v,c;cin>>u>>v>>c;--u;--v;--c;cout<<(d.dist(u,v)==d.dist(u,c)+d.dist(c,v)?"YES\n":"NO\n");}}'''
CPP["bridge_completion"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;auto[id,t]=bridge_tree(n,e);int leaves=0;for(auto&v:t)leaves+=v.size()==1;cout<<(leaves+1)/2<<'\n';}'''
CPP["sink_size"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;SCC s(n,e);vector<int>size(s.c);vector<char>out(s.c);for(int v=0;v<n;v++)size[s.id[v]]++;for(auto[u,v]:e)if(s.id[u]!=s.id[v])out[s.id[u]]=1;int sink=-1;for(int c=0;c<s.c;c++)if(!out[c]){if(sink!=-1){cout<<0<<'\n';return 0;}sink=c;}cout<<size[sink]<<'\n';}'''
CPP["strong_repairs"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;SCC s(n,e);if(s.c==1){cout<<0<<'\n';return 0;}vector<char>in(s.c),out(s.c);for(auto[u,v]:e)if(s.id[u]!=s.id[v])out[s.id[u]]=in[s.id[v]]=1;cout<<max(count(in.begin(),in.end(),0),count(out.begin(),out.end(),0))<<'\n';}'''
CPP["word_chain"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<vector<pair<string,int>>>g(26);vector<int>in(26),out(26);for(int i=0;i<n;i++){string w;cin>>w;int u=w.front()-'a',v=w.back()-'a';g[u].push_back({w,v});out[u]++;in[v]++;}vector<int>plus,minus;for(int v=0;v<26;v++){if(out[v]-in[v]==1)plus.push_back(v);else if(in[v]-out[v]==1)minus.push_back(v);else if(in[v]!=out[v]){cout<<"IMPOSSIBLE\n";return 0;}}if(plus.size()!=minus.size()||plus.size()>1){cout<<"IMPOSSIBLE\n";return 0;}int start=plus.empty()?-1:plus[0];if(start<0)for(int i=0;i<26;i++)if(out[i]){start=i;break;}for(auto&v:g)sort(v.rbegin(),v.rend());vector<pair<int,string>>st={{start,""}};vector<string>ans;while(!st.empty()){int u=st.back().first;if(g[u].empty()){if(!st.back().second.empty())ans.push_back(st.back().second);st.pop_back();}else{auto[w,v]=g[u].back();g[u].pop_back();st.push_back({v,w});}}if((int)ans.size()!=n)cout<<"IMPOSSIBLE\n";else{reverse(ans.begin(),ans.end());for(int i=0;i<n;i++)cout<<ans[i]<<" \n"[i+1==n];}}'''
CPP["robbins"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;LowLink l(n,e);cout<<(count(l.bridge.begin(),l.bridge.end(),1)?"NO\n":"YES\n");}'''
CPP["failed_vertex"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;TreeDistance d(block_cut(n,e));while(q--){int u,v,c;cin>>u>>v>>c;--u;--v;--c;bool bad=c==u||c==v||d.dist(u,v)==d.dist(u,c)+d.dist(c,v);cout<<(bad?"NO\n":"YES\n");}}'''
CPP["dominator_subtree"] = CPP_COMMON + r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<pair<int,int>>e(m);for(auto&[u,v]:e)cin>>u>>v,--u,--v;auto d=dominators(n,e);vector<int>size(n);for(int x=0;x<n;x++)for(int v=0;v<n;v++)size[v]+=d[x][v];while(q--){int v;cin>>v;cout<<size[v-1]<<'\n';}}'''

SAMPLES = {
    "condensation": ("4 4\n1 2\n2 1\n2 3\n3 4\n", "3 1 1\n"),
    "twosat": ("2 3\n1 2\n-1 2\n-2 1\n", "YES\n"),
    "euler": ("3 3\n1 2\n2 1\n1 3\n", "1 2 1 3\n"),
    "dominators": ("5 6\n1 2\n1 3\n2 4\n3 4\n4 5\n2 3\n", "1\n4\n"),
    "bridge_distance": ("4 4 2\n1 2\n2 3\n3 1\n3 4\n1 4\n1 2\n", "1\n0\n"),
    "articulation_damage": ("4 3\n1 2\n2 3\n2 4\n", "0 3 0 0\n"),
    "mandatory": ("4 3 2\n1 2\n2 3\n2 4\n1 3 2\n3 4 1\n", "YES\nNO\n"),
    "bridge_completion": ("4 3\n1 2\n2 3\n3 4\n", "1\n"),
    "sink_size": ("4 4\n1 2\n2 1\n2 3\n4 3\n", "1\n"),
    "strong_repairs": ("4 2\n1 2\n3 4\n", "2\n"),
    "word_chain": ("3\nab\nba\nac\n", "ab ba ac\n"),
    "robbins": ("3 3\n1 2\n2 3\n3 1\n", "YES\n"),
    "failed_vertex": ("4 3 2\n1 2\n2 3\n2 4\n3 4 2\n1 3 4\n", "NO\nYES\n"),
    "dominator_subtree": ("5 5 2\n1 2\n1 3\n2 4\n3 4\n4 5\n4\n1\n", "2\n5\n"),
}

LESSONS = {
79: r'''---
title: "Section 79 — Directed Graph Decomposition"
format: pdf
geometry: margin=1.8cm
---

# From cycles to a DAG

This lesson derives Problems A--C. Problem D is a fresh transfer problem whose derivation appears only in the editorial.

# Problem A: strongly connected components

Mutual reachability is an equivalence relation. Contracting each equivalence class removes every directed cycle between classes, so the condensation is a DAG. Kosaraju orders vertices by completed DFS time, then explores the reversed graph in decreasing completion order. The key boundary fact is that the first still-unassigned vertex cannot be entered from another unassigned source component in the reversed condensation.

Once component IDs are known, scan original edges and mark inter-component indegrees and outdegrees. Parallel condensation edges do not change zero/nonzero status.

# Problem B: 2-SAT as SCC contradiction

Clause `(a OR b)` is equivalent to implications `not a -> b` and `not b -> a`. An assignment is impossible exactly when a literal and its negation lie in the same SCC: each would force the other. Conversely, processing SCCs in reverse condensation order lets the first member of each unassigned complementary pair be set false, producing a consistent assignment.

# Problem C: directed Euler trails

An open Euler trail has one vertex with `out=in+1`, one with `in=out+1`, and balanced degrees elsewhere. A circuit balances every vertex. These conditions are necessary but not sufficient: all used edges must also belong to the traversal reachable from the requested start.

Hierholzer follows unused edges until stuck and appends vertices while backtracking. Each edge is removed once. Sorting outgoing edges in reverse lets the smallest available endpoint be popped in constant time; the final length check detects disconnected edge sets.

# Recognition and proof habits

- Mutual reachability suggests SCC contraction.
- Boolean implications suggest a graph on literals.
- “Use every edge once” suggests Euler, not Hamilton.
- “Every path from a root” suggests dominators, the editorial-only transfer.

# Exercises

A--C correspond to the three derivations. D deliberately supplies no lesson recipe.
''',
80: r'''---
title: "Section 80 — Undirected Connectivity Decomposition"
format: pdf
geometry: margin=1.8cm
---

# Low links describe escape routes

This lesson derives Problems A--C. Problem D is reserved for the editorial.

# Problem A: bridges and the bridge forest

During DFS, `tin[u]` is the entry time and `low[u]` is the smallest entry time reachable from `u`'s subtree using tree edges and at most one back edge. A tree edge `u-v` is a bridge exactly when `low[v] > tin[u]`: the subtree has no route to `u` or an ancestor without that edge.

Remove bridges and flood-fill the remaining edge-biconnected components. Every bridge becomes an edge between components, forming a tree for a connected graph. Therefore the mandatory bridge count between two vertices is their tree distance, answered by LCA.

Use edge IDs, not parent vertices: otherwise two parallel edges are incorrectly treated as one bridge.

# Problem B: articulation damage

For a child `v` with `low[v] >= tin[u]`, deleting `u` isolates the entire DFS subtree of `v`. These child-subtree sizes and the one remaining outside group partition all surviving vertices. The answer is the sum of products over distinct groups; accumulate it incrementally as `answer += seen * group_size`.

# Problem C: block-cut trees

Keep DFS edges on a stack. Whenever `low[v] >= tin[u]`, pop through edge `u-v`; the popped endpoints form one vertex-biconnected block. Build a bipartite tree containing original vertices and block nodes. An original vertex `c` lies on every `u-v` path exactly when its node lies on the unique block-cut-tree path from `u` to `v`, testable with three distances.

# Exercises

A--C develop bridges, articulation partitions, and block-cut paths. D is the independent transfer problem.
''',
81: r'''---
title: "Section 81 — Master Graph Decomposition Mixed Contest"
format: pdf
geometry: margin=1.8cm
---

# Contest contract

Six new problems mix condensation degrees, Euler reconstruction, bridge theorems, block-cut paths, and dominator sets. Suggested order: A, D, B, C, E, F.

| Problem | Main invariant |
|---|---|
| A | the only possible universal destination is the unique sink SCC |
| B | every source and sink SCC needs a new incident direction |
| C | words are labeled directed edges consumed by Hierholzer |
| D | Robbins' theorem: a connected undirected graph is strongly orientable iff it has no bridge |
| E | failed-vertex connectivity is the negation of block-cut path membership |
| F | a vertex dominates exactly the targets whose dominator set contains it |

# Exercises

Problems A--F form the complete mixed contest.
'''
}

NOTES = {
"condensation": "Contract mutual-reachability classes; the quotient is a DAG. Scan only inter-component edges to mark sources and sinks.",
"twosat": "Translate every clause into two contraposed implications. Unsatisfiability is exactly collision of a literal with its negation inside one SCC.",
"euler": "Check degree imbalance, consume sorted outgoing edges with Hierholzer, and require exactly m+1 output vertices.",
"dominators": "Start with every reachable vertex as a possible dominator, intersect predecessor sets to a fixed point, and inspect the target's set.",
"bridge_distance": "Delete bridges conceptually, contract the remaining components, and answer distance in the resulting bridge tree.",
"articulation_damage": "Low-link separating child subtrees plus the outside remainder are precisely the components after deletion; sum cross-group pairs.",
"mandatory": "Construct vertex-biconnected blocks. The queried station is mandatory exactly when its original-vertex node lies on the block-cut-tree path.",
"bridge_completion": "Every leaf of the bridge tree needs a new route; one added edge can repair two leaves, and pairing leaves attains the lower bound.",
"sink_size": "Every eventual universal destination must lie in a sink SCC; it exists exactly when that sink is unique.",
"strong_repairs": "Unless already strongly connected, each condensation source needs an incoming edge and each sink an outgoing edge; cyclic pairing attains the maximum of the counts.",
"word_chain": "Treat each word as a labeled edge and run lexicographic Hierholzer after checking Euler degree conditions.",
"robbins": "A bridge can never lie on a directed cycle, while DFS back edges orient every bridgeless tree edge into a strongly connected orientation.",
"failed_vertex": "Removing c disconnects u and v exactly when c lies on every original u-v path, including the endpoint cases.",
"dominator_subtree": "The fixed-point equation `Dom[v]={v} union intersection Dom[p]` characterizes all mandatory root-to-v checkpoints; invert membership counts.",
}

PROOFS = {
"condensation": "SCCs partition the vertices by mutual reachability. Any directed cycle between contracted classes would make all classes on it mutually reachable, a contradiction, so the quotient is a DAG. The final scan marks a class precisely when an original edge crosses its boundary; therefore the unmarked indegrees and outdegrees are exactly those requested.",
"twosat": "If a literal and its negation share an SCC, each implies the other, so either truth choice forces a contradiction. If no pair collides, take SCCs in reverse topological order and set an unassigned component false and its complementary component true. Every implication goes forward in this order, so no true premise can have a false conclusion; hence every clause holds.",
"euler": "The degree conditions follow by counting arrivals and departures of a trail. Hierholzer appends a vertex only when it has no unused outgoing edge, so reversing the appended list makes consecutive vertices endpoints of consumed edges and uses every consumed edge once. A list of length `m+1` proves all edges were consumed; otherwise the edge set was disconnected from the start. Ordered adjacency gives the first differing feasible edge the smallest endpoint.",
"dominators": "The root dominates only itself initially. For any other reachable vertex, a checkpoint dominates it exactly when it dominates every immediate predecessor, except the vertex itself which always dominates itself. Thus the fixed-point equation is necessary. Starting from the universal reachable set and repeatedly intersecting can only delete false candidates and converges to the greatest solution, which is the actual family of all-path dominators.",
"bridge_distance": "A DFS tree edge is a bridge exactly when its child subtree has no back edge reaching the parent or above. Contracting all nonbridge edges preserves precisely the separations caused by bridges. The quotient is a tree: a quotient cycle would give every edge on it an alternate route. Hence every route between two components crosses exactly the bridge-tree path, whose length is the answer.",
"articulation_damage": "For every child with `low[child] >= tin[v]`, no vertex in that child subtree can escape to the rest after deleting `v`; different such subtrees become different components. All vertices not in these subtrees form one remaining component. These groups partition the survivors, and a pair is disconnected exactly when its endpoints lie in distinct groups, which the incremental cross-product sum counts once.",
"mandatory": "Every original path alternates through the biconnected blocks containing its vertices, and every block offers internal routes avoiding any other non-endpoint vertex. Consequently an original vertex is unavoidable between `u` and `v` exactly when its node separates their nodes in the block-cut tree. In a tree this is equivalent to `dist(u,v)=dist(u,c)+dist(c,v)`.",
"bridge_completion": "Each leaf component of the bridge tree has only one old edge to the remainder, so any bridgeless augmentation must give it at least one new incident route. One added edge can serve at most two leaves, giving `ceil(leaves/2)` as a lower bound. Pairing leaves across the tree creates cycles covering their incident bridge paths and attains this bound.",
"sink_size": "From any SCC that can be the eventual destination for all vertices, no condensation edge may leave it; otherwise following that edge reaches a different class that cannot return. If two sinks exist, neither reaches the other. If exactly one sink exists, every condensation-DAG path extended until it stops ends there, so every vertex reaches precisely that component.",
"strong_repairs": "Every source SCC needs a new incoming edge and every sink SCC needs a new outgoing edge, so at least the larger count is necessary. List sources and sinks cyclically (repeating entries from the shorter list) and connect each sink to the next source. The added cycle links every old DAG region into one strongly connected tour, attaining the bound.",
"word_chain": "The first and last letters make each word one distinct directed edge, so a valid ordering is exactly an Euler trail. Hierholzer consumes every word once and produces a valid chain after reversal. If fewer than `n` words return, another used-edge component was unreachable. Sorting labeled edges makes the first differing word in the resulting valid itinerary minimal.",
"robbins": "A bridge cannot receive a strongly connected orientation because whichever direction it receives blocks reachability across it in the reverse direction. Conversely, in a connected bridgeless graph orient DFS tree edges downward and back edges toward ancestors. Every subtree has a back-edge escape above its parent edge, and induction gives directed routes both to and from the root; thus all vertices are mutually reachable.",
"failed_vertex": "When the failed vertex is an endpoint, connection is impossible. Otherwise `u` and `v` disconnect after removing `c` exactly when every old path used `c`. Section 80's block-cut characterization tests this all-path property exactly, so negating it yields precisely the surviving-connectivity answer.",
"dominator_subtree": "After fixed-point convergence, `v` belongs to `Dom[x]` exactly when every root-to-`x` path contains `v`. Counting this membership over all targets therefore counts exactly the vertices in `v`'s dominator-tree subtree, including `v` itself, without needing to construct the immediate-dominator edges.",
}

COMPLEXITY = {
    **{k: "`O(n+m)` time and memory." for k in ("condensation","twosat","euler","sink_size","strong_repairs","word_chain","robbins")},
    **{k: "`O((n+m) log n + q log n)` time and `O((n+m) log n)` memory." for k in ("bridge_distance","mandatory","failed_vertex")},
    "articulation_damage": "`O(n+m)` time and memory.",
    "bridge_completion": "`O(n+m)` time and memory.",
    "dominators": "At most `O(n(n+m))` set-intersection work under `n <= 1500`; bit-parallel storage uses `O(n^2 / word_size)` machine words.",
    "dominator_subtree": "The same bounded dominator fixed point plus `O(n^2)` membership aggregation.",
}


def editorial(section):
    chunks=[f'''---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat: pdf\ngeometry: margin=1.65cm\nfontsize: 9pt\n---\n''']
    for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
        chunks.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{NOTES[kind]}\n\n## Correctness\n\n{PROOFS[kind]}\n\n## Complexity\n\n{COMPLEXITY[kind]}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
    return "\n".join(chunks)


def generate():
    for section,(directory,title) in SECTIONS.items():
        base=ROOT/"sections"/f"{section:02d}_{directory}";base.mkdir(parents=True,exist_ok=True)
        (base/"lesson.qmd").write_text(LESSONS[section],encoding="utf-8")
        (base/"editorial.qmd").write_text(editorial(section),encoding="utf-8")
        links=[];checks=[]
        for slug,name,kind in PROBLEMS[section]:
            links.append(f"- [{name}](problems/{slug}/README.md)");checks.append(f"- [ ] [{name}](problems/{slug}/README.md)")
            p=base/"problems"/slug;p.mkdir(parents=True,exist_ok=True);tests=p/"tests";tests.mkdir(exist_ok=True)
            (p/"README.md").write_text(f"# {name}\n\n{STATEMENTS[kind]}\n",encoding="utf-8")
            (p/"solve.cpp").write_text(CPP_STUB,encoding="utf-8");(p/"solve.py").write_text(PY_STUB,encoding="utf-8")
            (p/"solution.cpp").write_text(CPP[kind],encoding="utf-8");(p/"solution.py").write_text(PY[kind],encoding="utf-8")
            (p/"manifest.json").write_text(json.dumps({"title":name,"checker":"tokens","time_limit_seconds":7})+"\n",encoding="utf-8")
            inp,out=SAMPLES[kind];(tests/"sample1.in").write_text(inp,encoding="utf-8");(tests/"sample1.out").write_text(out,encoding="utf-8")
            (tests/"random_cases.py").write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"graph_decomposition_random.py"),"{kind}",*sys.argv[1:]]))\n''',encoding="utf-8")
        extra="The lesson derives A--C; D is explained only in the editorial." if section<81 else "Exactly six new problems form the mixed contest."
        (base/"README.md").write_text(f"# Section {section}: {title}\n\n{extra}\n\n## Problems\n\n"+"\n".join(links)+"\n",encoding="utf-8")
        (base/"PRACTICE.md").write_text(f"# Section {section} Practice\n\n"+"\n".join(checks)+"\n",encoding="utf-8")
        names=",\n        ".join(repr(x[0]) for x in PROBLEMS[section])
        (base/"check.py").write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''',encoding="utf-8")


if __name__=="__main__":generate()
