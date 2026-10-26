# SAM construction playground

Open `index.html` directly in a browser. The page is self-contained and works
offline; it has no runtime dependencies and sends no input text to a server.
Its interface is in French and uses ASCII labels.

- Load a text, or choose an example such as `abb` or `abcbc`.
- Step through instructions, advance to the end of one character, or play
  automatically. The active C++ line, variables, graph and state table agree
  with the same execution frame.
- Move backward or seek through the explored history without losing state.
- Append characters at any time, including during an update. They are queued
  after the existing input, preserving the current position.
- Click a state to inspect its strings and ending positions. Intermediate
  groups are marked as provisional; inconsistent groups are identified.
- Toggle suffix links, zoom the graph, or fit it to the available width.

Keyboard shortcuts: left/right arrows for previous/next instruction, and
space to play/pause, when focus is outside an input or button.

The trace displays executable statements and condition evaluations from
`extend(ch)`. Orange marks the latest changed transition/state; blue identifies
clones and suffix links. Character positions count Unicode code points.

## Checks

The pure trace engine is embedded in the page and can be tested with Node:

```bash
node sections/44_string_algorithms_ii/sam_playground/tests/engine.test.mjs
```

The independent substring oracle covers every text over `abc` through length
6, plus clone, Unicode, whitespace and special-character cases. The checks
also cover state groups, ending positions, membership and immutable history.

Optional browser checks require Chromium and Python's `websocket-client`:

```bash
python3 sections/44_string_algorithms_ii/sam_playground/tests/browser_test.py
```

These checks open the actual standalone file, exercise the controls on desktop
and mobile, and save screenshots under `/tmp`.

## Hosted copy

The private Sites copy is published at:

https://sam-pas-a-pas.wittyrice514.chatgpt.site

`.openai/hosting.json` records its identity. For publication, the exact tested
`index.html` is copied into `dist/` in a separate deployment checkout; the
local standalone file remains the source of truth. The Sites source helper
handles source synchronization and packaging. Do not store source-access
tokens in this directory.
