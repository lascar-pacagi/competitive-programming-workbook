import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const path = fileURLToPath(new URL('../index.html', import.meta.url));
const html = readFileSync(path, 'utf8');
const core = html.match(/<script id="sam-core">([\s\S]*?)<\/script>/)[1];
const context = vm.createContext({});
vm.runInContext(core, context);
const SAM = context.SAM;
const encode = object => JSON.stringify(object);

function substrings(text) {
  const letters = Array.from(text), words = new Set();
  for (let l = 0; l < letters.length; l++) {
    for (let r = l + 1; r <= letters.length; r++) {
      words.add(letters.slice(l, r).join(''));
    }
  }
  return words;
}
function finish(machine, ch) {
  const frames = Array.from(SAM.traceCharacter(machine, ch));
  assert.equal(frames.at(-1).phase, 'complete');
  assert.equal(frames.at(-1).line, 30);
  for (const f of frames) {
    assert.ok(f.line > 0 && f.line <= SAM.CODE.length);
    for (const s of f.states) {
      for (const to of Object.values(s.next)) {
        assert.ok(Number.isInteger(to) && to >= 0 && to < f.states.length);
      }
    }
  }
  return frames;
}
function check(text) {
  const m = SAM.createMachine();
  assert.equal(SAM.countDistinct(m.states), 0);
  assert.equal(SAM.contains(m.states, ''), true);
  const initial = SAM.frame(m), original = encode(initial);
  for (const ch of Array.from(text)) {
    const before = m.states.length;
    const frames = finish(m, ch);
    assert.ok(m.states.length - before >= 1 && m.states.length - before <= 2);
    assert.equal(encode(initial), original, 'old frames must remain immutable');
    const snapshot = frames[0], snapshotData = encode(snapshot);
    const prefix = m.text.join(''), expected = substrings(prefix);
    assert.equal(m.distinct, expected.size);
    assert.equal(SAM.countDistinct(m.states), expected.size);
    for (const word of [...expected, 'zz', 'abc', 'bb', 'cbc']) {
      assert.equal(SAM.contains(m.states, word), expected.has(word));
    }
    const collected = new Set();
    for (let v = 1; v < m.states.length; v++) {
      const info = SAM.wordsInState(SAM.frame(m), v, Infinity);
      assert.equal(info.pending, false);
      assert.equal(info.words.length, info.total);
      const endsets = [];
      for (const word of info.words) {
        assert.ok(expected.has(word));
        assert.ok(!collected.has(word));
        collected.add(word);
        endsets.push(encode(SAM.endings(m.text, word)));
      }
      assert.ok(endsets.every(set => set === endsets[0]));
    }
    assert.equal(collected.size, expected.size);
    assert.equal(encode(snapshot), snapshotData);
  }
  return m;
}
let total = 0;
function enumerate(prefix, depth) {
  check(prefix); total++;
  if (depth) for (const ch of 'abc') enumerate(prefix + ch, depth - 1);
}
enumerate('', 6);
for (const text of ['abcbc', 'abcbcd', 'abcbcac', 'abbc', 'banana', 'mississippi', '<>&"', 'a b', '\u{1f600}a\u{1f600}']) {
  check(text); total++;
}
const m = SAM.createMachine();
finish(m, 'a');
const case1 = finish(m, 'b');
assert.ok(case1.some(f => f.line === 8 && f.vars.p === 0));
assert.ok(case1.some(f => f.line === 8 && f.vars.p === -1));
const case3 = finish(m, 'b');
assert.ok(case3.some(f => f.line === 17 && f.vars.clone === 4));
assert.equal(m.states[0].next.b, 4);
assert.equal(m.states[4].cloneOf, 2);
assert.notEqual(m.states[4].next, m.states[2].next);
assert.equal(m.states[2].link, 4);
assert.equal(m.states[3].link, 4);
const a = check('abcbc');
assert.equal(a.states.length, 8);
assert.equal(a.last, 6);
assert.equal(a.distinct, 12);
console.log(`Engine: ${total} texts pass independent substring, membership, group/endpos and trace checks.`);
