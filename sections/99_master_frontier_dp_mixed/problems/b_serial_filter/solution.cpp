#include <bits/stdc++.h>
using namespace std;
using ll=long long;
string digits,pattern;
vector<int>failure;
int target;
map<tuple<int,int,int,bool,bool>,ll>memo;
int step(int j,int d) {
    char c='0'+d;
    while(j&&pattern[j]!=c)j=failure[j-1];
    if(pattern[j]==c)j++;
    return j;
}
ll dfs(int pos,int j,int sum,bool tight,bool started) {
    if(sum>target)return 0;
    if(pos==(int)digits.size())return sum==target&&(started||pattern!="0");
    auto key=tuple {
        pos,j,sum,tight,started
    }
    ;
    if(!tight&&memo.count(key))return memo[key];
    int limit=tight?digits[pos]-'0':9;
    ll answer=0;
    for(int d=0;d<=limit;d++) {
        bool next_tight=tight&&d==limit;
        if(!started&&d==0)answer+=dfs(pos+1,0,sum,next_tight,false);
        else {
            int next=step(j,d);
            if(next<(int)pattern.size())answer+=dfs(pos+1,next,sum+d,next_tight,true);
        }
    }
    if(!tight)memo[key]=answer;
    return answer;
}
ll solve(ll n,string p,int s) {
    digits=to_string(n);
    pattern=p;
    target=s;
    failure.assign(p.size(),0);
    for(int i=1;i<(int)p.size();i++) {
        int j=failure[i-1];
        while(j&&p[i]!=p[j])j=failure[j-1];
        if(p[i]==p[j])j++;
        failure[i]=j;
    }
    memo.clear();
    return dfs(0,0,0,true,false);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin>>q;
    while(q--) {
        ll n;
        string p;
        int s;
        cin>>n>>p>>s;
        cout<<solve(n,p,s)<<'\n';
    }
}
