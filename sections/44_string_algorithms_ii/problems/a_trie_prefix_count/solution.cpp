#include <bits/stdc++.h>
using namespace std; struct Node{array<int,26> nx{}; int cnt=0;};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q)) return 0; vector<Node> tr(1); for(int i=0;i<n;i++){string s;cin>>s;int v=0;tr[v].cnt++;for(char c:s){int x=c-'a';if(!tr[v].nx[x]){tr[v].nx[x]=tr.size();tr.push_back(Node());}v=tr[v].nx[x];tr[v].cnt++;}} while(q--){string p;cin>>p;int v=0;bool ok=true;for(char c:p){int x=c-'a';if(!tr[v].nx[x]){ok=false;break;}v=tr[v].nx[x];} cout<<(ok?tr[v].cnt:0)<<'\n';}}
