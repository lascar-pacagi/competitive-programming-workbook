import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const page = new URL('../index.html', import.meta.url);
const html = fs.readFileSync(page, 'utf8');
const sandbox = vm.createContext({structuredClone});
vm.runInContext(html.match(/<script id="algorithm-core">([\s\S]*?)<\/script>/)[1], sandbox);
const {parseGraph, flowTrace, matchingTrace, PRESETS, FLOW_CODE, MATCH_CODE} = sandbox.FlowLab;
assert.equal(FLOW_CODE, fs.readFileSync(new URL('../implementations/dinic.py', page), 'utf8'));
assert.equal(MATCH_CODE, fs.readFileSync(new URL('../implementations/bipartite_matching.py', page), 'utf8'));
function cut(n,edges){let best=Infinity;for(let mask=1;mask<(1<<n);mask+=2){if(mask&(1<<(n-1)))continue;let total=0;for(const {u,v,c} of edges)if((mask>>u&1)&&!(mask>>v&1))total+=c;best=Math.min(best,total);}return best;}
function matching(n,r,edges){const adj=Array.from({length:n},()=>[]);for(const {u,v}of edges)adj[u].push(v);const memo=new Map();function go(u,mask){if(u===n)return 0;const key=u+':'+mask;if(memo.has(key))return memo.get(key);let result=go(u+1,mask);for(const v of adj[u])if(!(mask>>v&1))result=Math.max(result,1+go(u+1,mask|(1<<v)));memo.set(key,result);return result;}return go(0,0);}
let flowCases=0,matchCases=0,reverse=false;
function check(input){
 const iterator=input.mode==='flow'?flowTrace(input):matchingTrace(input);
 let count=0,first,firstText,last;
 for(const frame of iterator){
  assert.ok(++count<15000);
  assert.ok(Number.isInteger(frame.line)&&frame.line>=0);
  if(!first){first=frame;firstText=JSON.stringify(frame);}
  if(input.mode==='flow'){
   input.edges.forEach((e,i)=>{assert.equal(frame.cap[2*i]+frame.cap[2*i+1],e.c);assert.ok(frame.cap[2*i]>=0&&frame.cap[2*i+1]>=0);});
   if(frame.checkpoint||frame.done){
    const net=Array(input.n).fill(0);
    input.edges.forEach((e,i)=>{net[e.u]+=frame.cap[2*i+1];net[e.v]-=frame.cap[2*i+1];});
    assert.deepEqual(net,[frame.total,...Array(input.n-2).fill(0),frame.total===0?0:-frame.total]);
    if(frame.path.some(e=>e%2))reverse=true;
   }
  }else if(!frame.provisional){
   let size=0;
   frame.left.forEach((v,u)=>{if(v!==-1){size++;assert.equal(frame.right[v],u);assert.ok(input.edges.some(e=>e.u===u&&e.v===v));}});
   frame.right.forEach((u,v)=>{if(u!==-1)assert.equal(frame.left[u],v);});
   assert.equal(frame.total,size);
  }
  last=frame;
 }
 assert.equal(JSON.stringify(first),firstText,'snapshots must not mutate');
 assert.ok(last.done);
 if(input.mode==='flow'){
  flowCases++;assert.equal(last.total,cut(input.n,input.edges));assert.ok(last.side[0]&&!last.side[input.n-1]);
  assert.equal(input.edges.reduce((sum,e)=>sum+(last.side[e.u]&&!last.side[e.v]?e.c:0),0),last.total);
 }else{matchCases++;assert.equal(last.total,matching(input.n,input.r,input.edges));}
}
for(const mode of ['flow','matching'])for(const p of PRESETS[mode])check(parseGraph(mode,p.text));
let seed=45045;const rand=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n;};
for(let i=0;i<160;i++){
 const n=2+rand(5),edges=[];for(let j=rand(18);j>0;j--)edges.push({u:rand(n),v:rand(n),c:[0,1,3,1000000000][rand(4)]});
 check({mode:'flow',n,edges});
}
for(let mask=0;mask<64;mask++){const edges=[];for(let u=0;u<2;u++)for(let v=0;v<3;v++)if(mask>>(u*3+v)&1)edges.push({u,v});check({mode:'matching',n:2,r:3,edges});}
for(let i=0;i<100;i++){const n=1+rand(6),r=1+rand(6),edges=[];for(let u=0;u<n;u++)for(let v=0;v<r;v++)if(rand(3))edges.push({u,v});check({mode:'matching',n,r,edges});}
for(const [mode,text] of [['flow',''],['flow','2 1 0 2 1'],['flow','2 1 0 1 -1'],['flow','11 0'],['flow','2 0 extra'],['matching','2 2 1 0 2'],['matching','0 2 0']])assert.throws(()=>parseGraph(mode,text));
assert.ok(reverse,'must exercise an actual cancellation edge');
console.log(`Accepted: ${flowCases} flow traces and ${matchCases} matching traces, code parity, snapshots and invalid input.`);
