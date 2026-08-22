#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const int MOD=1e9+7;
using State=pair<vector<int>,bool>;
vector<int>canon(vector<int>a) {
    map<int,int>mp;
    int nxt=1;
    for(int&x:a)if(x) {
        if(!mp.count(x))mp[x]=nxt++;
        x=mp[x];
    }
    return a;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int h,w;
    cin>>h>>w;
    vector<string>g(h);
    for(auto&s:g)cin>>s;
    map<State,int>dp;
    dp[ {
        vector<int>(w),false
    }
    ]=1;
    for(int r=0;r<h;r++)for(int c=0;c<w;c++) {
        map<State,int>nd;
        for(auto[state,value]:dp) {
            auto labels=state.first;
            bool closed=state.second;
            int up=labels[c],left=c?labels[c-1]:0;
            auto z=labels;
            z[c]=0;
            bool vanished=up&&find(z.begin(),z.end(),up)==z.end();
            if(!vanished||(!closed&&count_if(z.begin(),z.end(),[](int x){return x;})==0)) {
                State key= {
                    canon(z),closed||vanished
                }
                ;
                nd[key]=(nd[key]+value)%MOD;
            }
            if(g[r][c]=='.'&&!closed) {
                z=labels;
                if(left&&up&&left!=up)for(int&x:z)if(x==up)x=left;
                z[c]=left?left:(up?up:*max_element(z.begin(),z.end())+1);
                State key= {
                    canon(z),false
                }
                ;
                nd[key]=(nd[key]+value)%MOD;
            }
        }
        dp.swap(nd);
    }
    ll answer=0;
    for(auto[state,value]:dp) {
        set<int>s(state.first.begin(),state.first.end());
        s.erase(0);
        if(state.second||s.size()==1)answer+=value;
    }
    cout<<answer%MOD<<'\n';
}
