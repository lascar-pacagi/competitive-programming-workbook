# Flow and matching laboratory

Open `index.html` directly in a browser. It is self-contained and works offline.

- Dinic: BFS levels, current pointers, explicit path stacks, bottlenecks,
  paired residual updates, and the final minimum-cut source side.
- Bipartite matching: alternating searches, owner queues, predecessors,
  individual partner assignments, and completed augmentations.
- Both: editable input, presets, next/previous, next augmentation, finish,
  playback speed, and a history slider.

IDs are 0-based throughout. Flow input is `n m` followed by `m` triples
`u v capacity`; source is `0` and sink is `n-1`. Matching input is `L R E`
followed by `E` pairs `left right`. Loading a graph starts a fresh execution.

The displayed Python comes directly from `../implementations/`. The JavaScript
trace engine performs the same operations, with immutable snapshots. Flow
updates are displayed atomically for the whole path. Matching's individual
assignments are shown with a notice while the partner arrays are provisional.

From the course root:

```sh
python3 sections/45_flows_and_matchings/implementations/check.py
node sections/45_flows_and_matchings/flow_playground/tests/engine.test.mjs
python3 sections/45_flows_and_matchings/flow_playground/tests/browser_test.py
```

Engine checks compare flow values with exhaustive cuts and matching values
with an independent exhaustive oracle. They also check residual pair sums,
conservation, final cuts, partner consistency, snapshots, and invalid input.
Browser checks require Chromium and Python `websocket-client`, and exercise
real controls through the Chrome DevTools protocol. Screenshots go to `/tmp`.

The hosting identity is retained in `.openai/hosting.json`. The hosted copy
uses an isolated source checkout; this directory remains the course source.
