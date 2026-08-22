# Practice order

1. Draw which nodes two adjacent persistent roots share in A.
2. For B, state whether each stored sum includes its node's lazy tag.
3. For C, convert every edge lifetime into a half-open time interval before
   choosing how to traverse those intervals.
4. Attempt D blind. Try to express a tree path as signed root-to-vertex
   prefixes before thinking about its segment-tree implementation.

Stress every implementation against a complete copied-state oracle on tiny
inputs. Sharing and rollback bugs often survive hand-picked samples.
