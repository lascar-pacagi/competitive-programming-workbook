#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const int MOD=1e9+7;
using Matrix=vector<vector<int>>;
Matrix multiply(const Matrix&a,const Matrix&b) {
    int n=a.size();
    Matrix c(n,vector<int>(n));
    for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(a[i][k])for(int j=0;j<n;j++)c[i][j]=(c[i][j]+(ll)a[i][k]*b[k][j])%MOD;
    return c;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long h;
    int p,w;
    cin>>h>>p>>w;
    vector<string>rows(p);
    for(auto&row:rows)cin>>row;
    int size=1<<w;
    Matrix block(size,vector<int>(size));
    for(int i=0;i<size;i++)block[i][i]=1;
    for(auto row:rows) {
        int blocked=0;
        for(int c=0;c<w;c++)if(row[c]=='#')blocked|=1<<c;
        Matrix transition(size,vector<int>(size));
        for(int incoming=0;incoming<size;incoming++)if(!(incoming&blocked)) {
            function<void(int,int,int)>fill=[&](int c,int used,int outgoing) {
                if(c==w) {
                    transition[incoming][outgoing]++;
                    return;
                }
                int bit=1<<c;
                if((used|blocked)&bit)fill(c+1,used,outgoing);
                else {
                    if(c+1<w&&!((used|blocked)&(bit<<1)))fill(c+2,used|bit|(bit<<1),outgoing);
                    fill(c+1,used|bit,outgoing|bit);
                }
            }
            ;
            fill(0,incoming,0);
        }
        block=multiply(block,transition);
    }
    Matrix answer(size,vector<int>(size));
    for(int i=0;i<size;i++)answer[i][i]=1;
    while(h) {
        if(h&1)answer=multiply(answer,block);
        block=multiply(block,block);
        h>>=1;
    }
    cout<<answer[0][0]<<'\n';
}
