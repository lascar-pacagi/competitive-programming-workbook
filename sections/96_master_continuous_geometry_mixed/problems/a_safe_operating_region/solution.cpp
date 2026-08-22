#include <bits/stdc++.h>
using namespace std;
const double EPS=1e-10,PI=acos(-1.0);
struct P {
    double x,y;
    P operator+(P b)const {
        return {
            x+b.x,y+b.y
        }
        ;
    }
    P operator-(P b)const {
        return {
            x-b.x,y-b.y
        }
        ;
    }
    P operator*(double k)const {
        return {
            x*k,y*k
        }
        ;
    }
}
;
double cross(P a,P b) {
    return a.x*b.y-a.y*b.x;
}
double dot(P a,P b) {
    return a.x*b.x+a.y*b.y;
}
double norm(P a) {
    return hypot(a.x,a.y);
}
struct L {
    P p,v;
    double angle;
}
;
P meet(L a,L b) {
    double t=cross(b.p-a.p,b.v)/cross(a.v,b.v);
    return a.p+a.v*t;
}
vector<P>halfplanes(vector<pair<P,P>>raw) {
    vector<L>a;
    for(auto[p,q]:raw) {
        P v=q-p;
        a.push_back({p,v,atan2(v.y,v.x)});
    }
    sort(a.begin(),a.end(),[](L x,L y){return x.angle<y.angle;});
    vector<L>u;
    for(L z:a) {
        if(!u.empty()&&abs(cross(u.back().v,z.v))<=EPS&&dot(u.back().v,z.v)>0) {
            if(cross(u.back().v,z.p-u.back().p)>EPS)u.back()=z;
        }
        else u.push_back(z);
    }
    deque<L>q;
    deque<P>pts;
    auto inside=[](L l,P p) {
        return cross(l.v,p-l.p)>=-EPS;
    }
    ;
    for(L z:u) {
        while(!pts.empty()&&!inside(z,pts.back()))pts.pop_back(),q.pop_back();
        while(!pts.empty()&&!inside(z,pts.front()))pts.pop_front(),q.pop_front();
        if(!q.empty()&&abs(cross(q.back().v,z.v))<=EPS)return {
        }
        ;
        if(!q.empty())pts.push_back(meet(q.back(),z));
        q.push_back(z);
    }
    while(!pts.empty()&&!inside(q.front(),pts.back()))pts.pop_back(),q.pop_back();
    while(!pts.empty()&&!inside(q.back(),pts.front()))pts.pop_front(),q.pop_front();
    if(q.size()<3)return {
    }
    ;
    pts.push_back(meet(q.back(),q.front()));
    return vector<P>(pts.begin(),pts.end());
}
double area(vector<P>p) {
    double s=0;
    for(int i=0;i<(int)p.size();i++)s+=cross(p[i],p[(i+1)%p.size()]);
    return abs(s)/2;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout<<fixed<<setprecision(10);
    int n;
    cin>>n;
    vector<pair<P,P>>l(n);
    for(auto&[a,b]:l)cin>>a.x>>a.y>>b.x>>b.y;
    cout<<area(halfplanes(l))<<'\n';
}
