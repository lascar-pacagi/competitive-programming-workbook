# Competitive Programming Course: Curriculum Plan

## Goal And Audience

This course is for a programmer who already knows C++ and Python and wants a
long, structured path toward red-coder-level competitive programming. The goal
is not only to memorize algorithms, but to develop the habits that make hard
problems solvable under contest pressure:

- reading constraints and choosing the right asymptotic target;
- extracting invariants and monotonicity;
- proving greedy and dynamic programming transitions;
- modeling problems as graphs, flows, matchings, or data-structure queries;
- stress-testing and debugging quickly;
- practicing with Codeforces, AtCoder, and ICPC-style tasks.

The intended finish line is comfort with Codeforces 2400+ problems,
AtCoder ARC/AGC hard problems, and ICPC regional/world-finals style modeling.
That level requires many contests outside the course; this repository provides
the structured spine.

## Deliverables Per Completed Section

Each section should contain:

1. `lesson.qmd` and generated `lesson.pdf`.
2. `editorial.qmd` and generated `editorial.pdf`.
3. `README.md` with goals, study order, and commands.
4. `problems/` with C++ and Python stubs.
5. Reference C++ and Python solutions.
6. Local judge tests: samples, edge cases, and generated tests when useful.
7. Diagrams or generated figures for concepts that benefit from visualization.
8. A practice queue that includes Codeforces, AtCoder, and ICPC entries.

External statements are linked, not copied. Local exercises use original
statements or short summaries plus an input/output contract for testing.

## Pedagogical Pattern

Each lesson follows this rhythm:

1. A motivating contest situation.
2. The naive idea and why it fails.
3. The key observation.
4. A diagram, table, or small trace.
5. The formal algorithm.
6. Proof of correctness.
7. Complexity.
8. C++ implementation notes.
9. Python implementation notes.
10. Common mistakes.
11. Exercises in increasing difficulty.

Each editorial follows this rhythm:

1. Restatement.
2. Observations.
3. Derivation.
4. Proof.
5. Complexity.
6. Full C++ solution.
7. Full Python solution where Python is viable.
8. Stress-test strategy.
9. Alternative approaches.

## Difficulty Scale

The course uses these broad bands:

- Foundation: Codeforces 800-1200, AtCoder ABC A-D.
- Core: Codeforces 1200-1700, AtCoder ABC E/F and beginner ARC.
- Advanced: Codeforces 1700-2200, AtCoder ARC C/D, ICPC regional.
- Red training: Codeforces 2200-2800, AtCoder ARC/AGC hard, ICPC finals.

## Phase 0: Contest Foundations

Goal: remove avoidable losses from setup, I/O, complexity mistakes, and
implementation bugs.

1. **Complexity, I/O, And Constraints**
   - Big-O from contest constraints.
   - Reading many test cases.
   - Integer range and overflow.
   - Local judging workflow.
   - Exercises: original local tasks plus easy CF/AtCoder/ICPC links.

2. **Simulation And Brute Force**
   - State updates.
   - Loop bounds.
   - Enumerating small search spaces.
   - Knowing when brute force is intended.

3. **Counting, Frequencies, And Maps**
   - Frequency arrays versus hash maps.
   - Coordinate ranges.
   - Histograms and mode/count queries.

4. **Prefix Sums And Difference Arrays**
   - One-dimensional prefix sums.
   - Range update, point query.
   - Point update, range query as a lead-in to Fenwick trees.

5. **Sorting As A Tool**
   - Custom comparators.
   - Stable reasoning after sorting.
   - Sorting to expose adjacency or order.

6. **Two Pointers And Sliding Windows**
   - Monotone window movement.
   - Counting subarrays.
   - Maintaining aggregate state.

7. **Foundation Mixed Contest**
   - Timed set of easy-to-medium tasks.
   - Editorial emphasizes decision process and debugging.

## Phase 1: Core Patterns

Goal: become reliable on the patterns that dominate medium contest problems.

8. **Binary Search On The Answer**
   - Monotone predicates.
   - Integer and real-valued search.
   - Feasibility checking.

9. **Greedy I: Local Choices And Exchange**
   - Exchange arguments.
   - Earliest finish, smallest sufficient, largest remaining.
   - Counterexample search.

10. **Greedy II: Invariants And Constructive Problems**
    - Preserving an invariant.
    - Building an object step by step.
    - Detecting impossibility.

11. **Intervals And Sweep Line**
    - Events.
    - Active sets.
    - Endpoint conventions.

12. **Stacks, Queues, And Deques**
    - Monotonic stacks.
    - Next greater/smaller.
    - Deque optimization basics.

13. **Offline Processing**
    - Reordering queries.
    - Coordinate compression.
    - Answer restoration.

14. **Core Patterns Mixed Contest**
    - Codeforces, AtCoder, and ICPC-style pattern mix.

## Phase 2: Graphs I

Goal: model and solve standard graph problems quickly and correctly.

15. **BFS And Unweighted Shortest Paths**
    - Grid BFS.
    - Multi-source BFS.
    - State-space BFS.

16. **DFS, Components, And Cycles**
    - Recursive and iterative DFS.
    - Connected components.
    - Directed cycle detection.

17. **Topological Sorting And DAG DP**
    - Kahn and DFS order.
    - Longest path in DAG.
    - Dependency modeling.

18. **DSU And Minimum Spanning Trees**
    - Union-find.
    - Kruskal.
    - Connectivity under added edges.

19. **Dijkstra And Weighted Modeling**
    - Priority queues.
    - Graph construction from problem states.
    - Duplicate heap entries.

20. **0-1 BFS And Shortest Path Variants**
    - Deque shortest paths.
    - Edge weights 0 and 1.
    - Layered graphs.

21. **Graphs I Mixed Contest**
    - Regional-style modeling plus standard CF/AtCoder graph tasks.

## Phase 3: Dynamic Programming I

Goal: identify states, transitions, and computation orders.

22. **One-Dimensional DP**
    - Recurrences.
    - Base cases.
    - Rolling arrays.

23. **Knapsack And Subset DP**
    - 0/1 and complete knapsack.
    - Sum feasibility.
    - State compression.

24. **Grid DP**
    - Paths.
    - Obstacles.
    - Counting under modulo.

25. **Interval DP**
    - Length order.
    - Splitting intervals.
    - Parsing and merging problems.

26. **Tree DP Basics**
    - Rooting trees.
    - Parent/child transitions.
    - Independent set and matching patterns.

27. **Bitmask DP**
    - Traveling subsets.
    - Assignment.
    - Submask iteration.

28. **DP I Mixed Contest**
    - AtCoder Educational DP-style set plus CF and ICPC tasks.

## Phase 4: Number Theory And Combinatorics

Goal: handle modular arithmetic, divisibility, and counting without treating
math as a black box.

29. **Modular Arithmetic**
    - Mod normalization.
    - Fast exponentiation.
    - Modular inverses.

30. **GCD, LCM, And Diophantine Equations**
    - Euclid.
    - Extended Euclid.
    - Linear combinations.

31. **Sieve, Primes, And Factorization**
    - Eratosthenes.
    - Smallest prime factor.
    - Divisor enumeration.

32. **Combinatorics Under Modulo**
    - Factorials.
    - Binomial coefficients.
    - Stars and bars.

33. **Inclusion-Exclusion**
    - Overcounting.
    - Subset signs.
    - Divisibility counting.

34. **Probability And Expected Value**
    - Linearity.
    - Markov chains at a contest level.
    - Expected DP.

35. **Math Mixed Contest**
    - Balanced CF/AtCoder/ICPC math tasks.

## Phase 5: Advanced Data Structures

Goal: answer dynamic queries and tree queries efficiently.

36. **Fenwick Tree**
    - Prefix aggregates.
    - Point update/range query.
    - Order statistic via binary lifting.

37. **Segment Tree**
    - Merge functions.
    - Point update/range query.
    - Iterative and recursive styles.

38. **Static Queries And Binary Lifting**
    - Idempotent queries.
    - Binary lifting over arrays.
    - Static RMQ applications.

39. **Heaps And Priority Queues**
    - Sweep-line active data.
    - Median maintenance.
    - Generating the next-best candidate.

40. **Data Structures Mixed Contest**
    - Query-heavy reductions across earlier structures.
    - Choosing between online and offline processing.

41. **Euler Tour, LCA, And Binary Lifting**
    - Tree flattening.
    - Ancestors.
    - Path queries.

42. **Advanced Data Structures Mixed Contest**
    - Order statistics with Fenwick binary lifting.
    - Range-add/range-sum with two Fenwick trees.
    - Offline rectangle counting.

**Appendix A. Lazy Propagation**
    - Range update/range query.
    - Tag composition and operation order.
    - Push/pull discipline, with Section 37's range-update exercise as the
      implementation bridge.

## Phase 6: Advanced Algorithms

Goal: learn the standard tools that appear in high blue, purple, and early red
problems.

43. **String Algorithms I**
    - Prefix function.
    - KMP.
    - Z-function.

44. **String Algorithms II**
    - Rolling hash.
    - Tries.
    - Suffix array basics.

45. **Flows And Matchings**
    - Max flow.
    - Min cut.
    - Bipartite matching.

46. **Rerooting And Advanced Tree DP**
    - Down/up values.
    - All-root answers.
    - Associative rerooting patterns.

47. **Meet-In-The-Middle**
    - Split enumeration.
    - Sorting and matching halves.
    - Memory/time tradeoffs.

48. **Divide And Conquer Optimization**
    - DP transition monotonicity.
    - Proof obligations.
    - Implementation template.

49. **Convex Hull Trick And Li Chao Tree**
    - Lines and minima.
    - Monotone variants.
    - Fully dynamic Li Chao tree.

50. **Advanced Algorithms Mixed Contest**
    - CF 2000-2400, AtCoder ARC, and ICPC regional/finals tasks.

## Phase 7: Red-Coder Training

Goal: train problem-solving depth, proof flexibility, and contest execution on
harder mixed problems.

51. **Invariants In Hard Problems**
    - Conservation laws.
    - Parity and modular invariants.
    - Constructive proofs.

52. **Game Theory**
    - Winning and losing states.
    - Sprague-Grundy.
    - Nim reductions.

53. **Advanced Combinatorics**
    - Generating functions at a contest level.
    - Recurrence manipulation.
    - Counting structures.

54. **Geometry**
    - Orientation.
    - Convex hull.
    - Intersections and precision.

55. **Randomization And Hashing**
    - Randomized checks.
    - Collision risk.
    - Las Vegas versus Monte Carlo reasoning.

56. **Hard Greedy And Matroids Intro**
    - When exchange arguments scale.
    - Matroid-like independence.
    - Counterexamples.

57. **Reductions And Modeling**
    - Turning strange tasks into known structures.
    - Dual viewpoints.
    - Flow, matching, graph, and DP reductions.

58. **Full Virtual Contest Workflow**
    - Triage.
    - Partial progress.
    - Upsolving.
    - Post-contest notebook updates.

59. **ICPC Team Strategy**
    - Role allocation.
    - Shared debugging.
    - Problem picking.
    - Notebook and template maintenance.

60. **Final Capstone**
    - A curated multi-source set with red-level stretch problems.
    - Editorial emphasizes the path from first observation to accepted code.

61. **ICPC Contest Readiness**
    - Scoreboard rules, time-boxing, and submission discipline.
    - One-keyboard team communication and handoffs.
    - A five-hour simulation protocol, postmortem, and targeted retraining.

62. **Codeforces Course Ladder**
    - An offline problem sheet with direct Codeforces links and original
      restatements of selected tasks.
    - A simple-to-hard progression across foundations, graphs, DP, math,
      data structures, strings, flows, geometry, and advanced optimization.
    - Original pedagogical editorials that connect each task back to the
      relevant course sections.

## Practice Queue Policy

Every mature section should eventually include:

- at least two Codeforces problems;
- at least two AtCoder problems;
- at least one ICPC-style problem;
- at least one original local exercise with full automatic tests;
- one stretch problem above the section's nominal level.

Each external problem entry should record:

```text
source:
link:
difficulty:
topics:
status: required | optional | challenge
local_tested: yes | no
notes:
```

## Milestone Plan

The first committed milestone is intentionally small and complete:

1. Repository scaffold.
2. Shared local judge.
3. Full 60-section plan.
4. Complete Section 1 as the canonical template.

After reviewing Section 1, future milestones can add sections in batches of
three to five, preserving the same structure.
