#include <bits/stdc++.h>
using namespace std;
using ll=long long;
string digits,pat;
vector<int>fail;
map<tuple<int,int,bool,bool>,ll>memo;
int step(int j,int d) {
    char c='0'+d;
    while(j&&pat[j]!=c)j=fail[j-1];
    if(pat[j]==c)j++;
    return j;
}
ll dfs(int pos,int j,bool tight,bool started) {
    if(pos==(int)digits.size())return started||pat!="0";
    auto key=tuple {
        pos,j,tight,started
    }
    ;
    if(!tight&&memo.count(key))return memo[key];
    int lim=tight?digits[pos]-'0':9;
    ll ans=0;
    for(int d=0;d<=lim;d++) {
        bool nt=tight&&d==lim;
        if(!started&&d==0)ans+=dfs(pos+1,0,nt,0);
        else {
            int nj=step(j,d);
            if(nj<(int)pat.size())ans+=dfs(pos+1,nj,nt,1);
        }
    }
    if(!tight)memo[key]=ans;
    return ans;
}
ll solve(ll n,string p) {
    digits=to_string(n);
    pat=p;
    fail.assign(p.size(),0);
    for(int i=1;i<(int)p.size();i++) {
        int j=fail[i-1];
        while(j&&p[i]!=p[j])j=fail[j-1];
        if(p[i]==p[j])j++;
        fail[i]=j;
    }
    memo.clear();
    return dfs(0,0,1,0);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin>>q;
    while(q--) {
        ll n;
        string p;
        cin>>n>>p;
        cout<<solve(n,p)<<'\n';
    }
}
