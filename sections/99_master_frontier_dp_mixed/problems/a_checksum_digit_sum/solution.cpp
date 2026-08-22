#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Query {
    ll left,right;
    int target,mod;
}
;
using Ways=vector<vector<vector<ll>>>;
Ways build(int mod) {
    Ways ways(20,vector<vector<ll>>(172,vector<ll>(mod)));
    ways[0][0][0]=1;
    for(int length=1;length<20;length++)for(int total=0;total<=171;total++)for(int digit=0;digit<=9&&digit<=total;digit++)for(int remainder=0;remainder<mod;remainder++)ways[length][total][(remainder*10+digit)%mod]+=ways[length-1][total-digit][remainder];
    return ways;
}
ll count_to(ll n,int target,int mod,const Ways&ways) {
    if(n<0)return 0;
    string digits=to_string(n);
    vector<int>power(20,1%mod);
    for(int i=1;i<20;i++)power[i]=power[i-1]*10%mod;
    ll answer=0;
    int prefix_sum=0,prefix_rem=0;
    for(int pos=0;pos<(int)digits.size();pos++) {
        int limit=digits[pos]-'0',remaining=digits.size()-pos-1;
        for(int digit=0;digit<limit;digit++) {
            int needed_sum=target-prefix_sum-digit;
            if(0<=needed_sum&&needed_sum<=171) {
                int next_rem=(prefix_rem*10+digit)%mod;
                int needed_rem=(mod-(ll)next_rem*power[remaining]%mod)%mod;
                answer+=ways[remaining][needed_sum][needed_rem];
            }
        }
        prefix_sum+=limit;
        prefix_rem=(prefix_rem*10+limit)%mod;
    }
    return answer+(prefix_sum==target&&prefix_rem==0);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin>>q;
    vector<Query>queries(q);
    map<int,vector<int>>groups;
    for(int i=0;i<q;i++) {
        auto&x=queries[i];
        cin>>x.left>>x.right>>x.target>>x.mod;
        groups[x.mod].push_back(i);
    }
    vector<ll>answer(q);
    for(auto&[mod,indices]:groups) {
        Ways ways=build(mod);
        for(int index:indices) {
            auto x=queries[index];
            answer[index]=count_to(x.right,x.target,mod,ways)-count_to(x.left-1,x.target,mod,ways);
        }
    }
    for(ll value:answer)cout<<value<<'\n';
}
