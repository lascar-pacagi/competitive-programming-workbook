"""Independent small geometric oracles for Sections 94--96."""
import argparse,itertools,math,random
from pathlib import Path
EPS=1e-8
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def dist(a,b):return math.hypot(a[0]-b[0],a[1]-b[1])
def polygon(r,n=None):
 n=n or r.randint(3,9);angles=sorted(r.random()*2*math.pi for _ in range(n));return [(r.uniform(4,12)*math.cos(a),r.uniform(4,12)*math.sin(a)) for a in angles]
def hull(points):
 p=sorted(set(points))
 def side(part):
  out=[]
  for x in part:
   while len(out)>=2 and cross(out[-2],out[-1],x)<=0:out.pop()
   out.append(x)
  return out
 return side(p)[:-1]+side(reversed(p))[:-1]
def area(p):return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2
def clip(poly,a,b):
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  cp=cross(a,b,p);cq=cross(a,b,q)
  if cp>=-EPS:out.append(p)
  if (cp>=-EPS)!=(cq>=-EPS):
   t=cp/(cp-cq);out.append((p[0]+(q[0]-p[0])*t,p[1]+(q[1]-p[1])*t))
 return out
def clipped(lines):
 p=[(-1e5,-1e5),(1e5,-1e5),(1e5,1e5),(-1e5,1e5)]
 for a,b in lines:p=clip(p,a,b)
 return p
def circle2(a,b):return((a[0]+b[0])/2,(a[1]+b[1])/2,dist(a,b)/2)
def circle3(a,b,c):
 d=2*cross(a,b,c);aa=a[0]**2+a[1]**2;bb=b[0]**2+b[1]**2;cc=c[0]**2+c[1]**2
 x=(aa*(b[1]-c[1])+bb*(c[1]-a[1])+cc*(a[1]-b[1]))/d;y=(aa*(c[0]-b[0])+bb*(a[0]-c[0])+cc*(b[0]-a[0]))/d;return(x,y,dist((x,y),a))
def contains(c,p):return dist(c[:2],p)<=c[2]+1e-7
def brute_mec(p):
 cand=[(x,y,0) for x,y in p]+[circle2(a,b) for a,b in itertools.combinations(p,2)]+[circle3(a,b,c) for a,b,c in itertools.combinations(p,3) if abs(cross(a,b,c))>EPS]
 return min((c for c in cand if all(contains(c,x) for x in p)),key=lambda c:c[2])
def triangles(p):
 out=[]
 for i,j,k in itertools.combinations(range(len(p)),3):
  if abs(cross(p[i],p[j],p[k]))<EPS:continue
  c=circle3(p[i],p[j],p[k])
  if all(t in (i,j,k) or dist(c[:2],p[t])>=c[2]-1e-7 for t in range(len(p))):out.append((i,j,k,c[2]))
 return out
def complete_mst(p):
 n=len(p);used=[False]*n;best=[float('inf')]*n;best[0]=0;ans=0
 for _ in range(n):
  u=min((i for i in range(n) if not used[i]),key=lambda i:best[i]);used[u]=True;ans+=best[u]
  for v in range(n):
   if not used[v]:best[v]=min(best[v],dist(p[u],p[v]))
 return ans
def points(r,n):
 while True:
  p=[(r.uniform(-10,10)+i*1e-4,r.uniform(-10,10)+i*i*1e-5) for i in range(n)]
  if all(abs(cross(a,b,c))>1e-5 for a,b,c in itertools.combinations(p,3)):return p
def one(kind,r):
 base={'hpi_story':'hpi','incircle_story':'incircle','overlap_story':'overlap','mec_story':'mec','empty_story':'empty','mst_story':'mst'}.get(kind,kind)
 if base=='hpi':
  p=hull(points(r,r.randint(4,9)));lines=list(zip(p,p[1:]+p[:1]));r.shuffle(lines);text=f'{len(lines)}\n'+''.join(f'{a[0]} {a[1]} {b[0]} {b[1]}\n' for a,b in lines);return text,f'{area(p):.12f}\n'
 if base=='overlap':
  c=[r.uniform(-5,5),r.uniform(-5,5),r.uniform(.1,6),r.uniform(-5,5),r.uniform(-5,5),r.uniform(.1,6)];d=math.hypot(c[0]-c[3],c[1]-c[4]);a,b=c[2],c[5]
  if d>=a+b:ans=0
  elif d<=abs(a-b):ans=math.pi*min(a,b)**2
  else:x=math.acos((d*d+a*a-b*b)/(2*d*a));y=math.acos((d*d+b*b-a*a)/(2*d*b));ans=a*a*x+b*b*y-d*a*math.sin(x)
  return ' '.join(map(str,c[:3]))+'\n'+' '.join(map(str,c[3:]))+'\n',f'{ans:.12f}\n'
 if base=='tangents':
  c=[r.uniform(-5,5),r.uniform(-5,5),r.uniform(.1,5),r.uniform(-5,5),r.uniform(-5,5),r.uniform(.1,5)];d=math.hypot(c[0]-c[3],c[1]-c[4]);ans=sum(2 if d>x+EPS else (1 if abs(d-x)<=EPS else 0) for x in (abs(c[2]-c[5]),c[2]+c[5]));return ' '.join(map(str,c[:3]))+'\n'+' '.join(map(str,c[3:]))+'\n',f'{ans}\n'
 if base=='incircle':
  p=hull(points(r,r.randint(4,9)));lo=0;hi=30
  for _ in range(80):
   m=(lo+hi)/2;lines=[]
   for a,b in zip(p,p[1:]+p[:1]):dx=b[0]-a[0];dy=b[1]-a[1];z=math.hypot(dx,dy);s=(-dy*m/z,dx*m/z);lines.append(((a[0]+s[0],a[1]+s[1]),(b[0]+s[0],b[1]+s[1])))
   if clipped(lines):lo=m
   else:hi=m
  return f'{len(p)}\n'+''.join(f'{x} {y}\n' for x,y in p),f'{lo:.12f}\n'
 n=r.randint(1,9) if base in {'mec','mst'} else r.randint(3,8);p=points(r,n);text=f'{n}\n'+''.join(f'{x} {y}\n' for x,y in p)
 if base=='mec':c=brute_mec(p);return text,f'{c[0]:.12f} {c[1]:.12f} {c[2]:.12f}\n'
 if base=='mst':return text,f'{complete_mst(p):.12f}\n'
 values=[x[3] for x in triangles(p)];ans=max(values) if base=='empty' else sum(values);return text,f'{ans:.12f}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('kind');p.add_argument('--count',type=int,default=20);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=one(a.kind,r);stem=a.out_dir/f'case{i:03d}';stem.with_suffix('.in').write_text(x);stem.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
