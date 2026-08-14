"""Curated task data for Section 63's AtCoder difficulty ladder.

Ratings are rounded AtCoder Problems estimates captured when the section was
authored. They are guideposts, not official AtCoder labels.
"""

from __future__ import annotations


TASKS = [
    {
        "id": "abc083_b",
        "title": "Some Sums",
        "rating": 100,
        "bridge": "Sections 1-2",
        "summary": (
            "Given N, A, and B, sum every integer x in 1..N whose decimal digit "
            "sum lies in the inclusive interval [A,B]. The bounds are small "
            "enough to inspect every candidate."
        ),
        "idea": (
            "Enumerate x and compute its digit sum by repeatedly taking x % 10 "
            "and dividing by 10. Add the original x exactly when the sum is in "
            "[A,B]. This is the deliberately short entry ramp."
        ),
        "proof": (
            "Every eligible integer is visited once, and the test is exactly the "
            "definition of eligibility; therefore the accumulator contains all "
            "and only required integers."
        ),
        "complexity": "O(N log N) time and O(1) auxiliary memory.",
        "traps": "The interval is inclusive, and the number added is x, not its digit sum.",
    },
    {
        "id": "abc210_c",
        "title": "Colorful Candies",
        "rating": 400,
        "bridge": "Sections 3, 6, and 12",
        "summary": (
            "Given N candy colors and a window length K, find the maximum number "
            "of distinct colors in any K consecutive positions."
        ),
        "idea": (
            "Maintain a frequency map for the current fixed-length window. When "
            "the right endpoint advances, insert the entering color and erase "
            "the leaving color if its count becomes zero. Track the map size."
        ),
        "proof": (
            "After each update the map stores exactly the multiplicity of every "
            "color in the current K positions, so its number of keys is precisely "
            "that window's distinct count. Taking the maximum checks all windows."
        ),
        "complexity": "O(N) expected time with a hash map and O(K) memory.",
        "traps": "A zero frequency must stop contributing to the distinct count.",
    },
    {
        "id": "abc167_d",
        "title": "Teleporter",
        "rating": 800,
        "bridge": "Sections 16 and 27",
        "summary": (
            "A functional graph gives one next town for each town. Starting at "
            "town 1, report the town reached after exactly K moves, where K may "
            "be as large as 10^18."
        ),
        "idea": (
            "Record the first step at which each visited town appears and store "
            "the walk order. The first repeated town identifies a tail and a "
            "cycle. If K passes the tail, reduce only the remaining distance "
            "modulo the cycle length."
        ),
        "proof": (
            "Before the first repetition the walk has no choice and no duplicate. "
            "After entering the repeated suffix, determinism makes the same cycle "
            "repeat forever, so positions differing by its length are identical."
        ),
        "complexity": "O(N) time and O(N) memory.",
        "traps": "K counts edges from the starting town at step 0; reduce K-tail, not K.",
    },
    {
        "id": "abc130_d",
        "title": "Enough Array",
        "rating": 900,
        "bridge": "Sections 4 and 6",
        "summary": (
            "For a positive array, count subarrays whose sum is at least K. N is "
            "large enough that enumerating both endpoints is too slow."
        ),
        "idea": (
            "For each left endpoint, advance a shared right endpoint until the "
            "window first reaches K. Positivity implies that every later right "
            "endpoint also works, contributing N-right choices, after which remove "
            "the left value."
        ),
        "proof": (
            "Because all values are positive, extending a window cannot decrease "
            "its sum. Thus the first feasible right endpoint separates all "
            "infeasible endings from all feasible endings, and the pointer never "
            "needs to move backward."
        ),
        "complexity": "O(N) time and O(1) auxiliary memory.",
        "traps": "Use a 64-bit answer; there can be N(N+1)/2 valid subarrays.",
    },
    {
        "id": "abc138_d",
        "title": "Ki",
        "rating": 900,
        "bridge": "Sections 16 and 26",
        "summary": (
            "Root a tree at vertex 1. Each query adds a value to one vertex and "
            "every descendant of that vertex. Print the final value at every "
            "vertex."
        ),
        "idea": (
            "Accumulate all query values directly at their named vertices. A "
            "single root-to-leaf traversal then adds the parent's accumulated "
            "value to each child."
        ),
        "proof": (
            "On reaching a vertex, its accumulator contains exactly the updates "
            "issued at its ancestors already propagated along the root path, plus "
            "its own updates. Passing that sum to children preserves the invariant."
        ),
        "complexity": "O(N+Q) time and O(N) memory.",
        "traps": "The input edges are undirected; carry a parent or visited array.",
    },
    {
        "id": "abc218_e",
        "title": "Destruction",
        "rating": 1000,
        "bridge": "Section 18",
        "summary": (
            "Delete edges from a connected weighted undirected graph while keeping "
            "it connected, maximizing the sum of deleted edge weights. Weights may "
            "be negative."
        ),
        "idea": (
            "Keep every non-positive edge because deleting it cannot improve the "
            "score. Process positive edges by Kruskal order: keep one only when it "
            "joins different DSU components; otherwise delete it and add its weight."
        ),
        "proof": (
            "Non-positive deletion is never beneficial. Among positive edges, the "
            "kept edges need only supply connectivity; Kruskal minimizes their "
            "total weight by the cut property, which equivalently maximizes the "
            "positive weight left for deletion."
        ),
        "complexity": "O(M log M) time and O(N) DSU memory.",
        "traps": "Blindly computing total minus an MST incorrectly deletes negative edges.",
    },
    {
        "id": "abc075_c",
        "title": "Bridge",
        "rating": 1100,
        "bridge": "Section 16",
        "summary": (
            "In a small connected undirected graph, count edges whose individual "
            "removal disconnects the graph."
        ),
        "idea": (
            "The small limits allow a direct definition-driven method: temporarily "
            "skip each edge, run DFS or BFS from one vertex, and test whether all "
            "vertices remain reachable."
        ),
        "proof": (
            "For a tested edge, reachability in the graph with exactly that edge "
            "removed is precisely the definition of whether it is a bridge. Testing "
            "every edge therefore counts all and only bridges."
        ),
        "complexity": "O(M(N+M)) time and O(N+M) memory.",
        "traps": "Skip an edge by its unique input index, not merely by its endpoints.",
    },
    {
        "id": "abc180_e",
        "title": "Traveling Salesman among Aerial Cities",
        "rating": 1300,
        "bridge": "Section 27",
        "summary": (
            "Visit every 3D city, starting and ending at city 1. Travel cost is "
            "|dx|+|dy|+max(0,z_destination-z_source), so direction matters."
        ),
        "idea": (
            "Use subset DP: dp[mask][v] is the minimum cost of starting at city 1, "
            "visiting exactly mask, and ending at v. Extend to each unvisited city, "
            "then add the directed cost back to city 1."
        ),
        "proof": (
            "Every tour has a unique penultimate state obtained by deleting its "
            "last visited city. Conversely every transition appends one new city "
            "to a valid partial tour. Taking minima therefore covers exactly all "
            "visit orders."
        ),
        "complexity": "O(N^2 2^N) time and O(N 2^N) memory.",
        "traps": "The height term makes cost(u,v) different from cost(v,u).",
    },
    {
        "id": "abc137_d",
        "title": "Summer Vacation",
        "rating": 1300,
        "bridge": "Sections 9 and 39",
        "summary": (
            "There are M working days. Job i becomes available after A_i days and "
            "pays B_i; at most one job can be completed per day. Maximize reward."
        ),
        "idea": (
            "Sort jobs by availability. Sweep the days, insert rewards of every job "
            "that has become available into a max-heap, and perform the currently "
            "most rewarding available job."
        ),
        "proof": (
            "On a day, replacing a chosen available job by the maximum-reward "
            "available job cannot reduce today's reward. The displaced lower-value "
            "job remains no less available for later days, so the exchange preserves "
            "feasibility."
        ),
        "complexity": "O((N+M) log N) time and O(N) memory.",
        "traps": "Availability and deadlines are easy to reverse; trace the day convention.",
    },
    {
        "id": "abc135_d",
        "title": "Digits Parade",
        "rating": 1300,
        "bridge": "Sections 22 and 31",
        "summary": (
            "Replace every '?' in a decimal string by a digit. Count replacements "
            "whose resulting integer is congruent to 5 modulo 13, modulo 1e9+7."
        ),
        "idea": (
            "Scan left to right. dp[r] counts assignments of the processed prefix "
            "with remainder r. Appending digit d changes r to (10r+d) mod 13; for "
            "'?' try all ten digits."
        ),
        "proof": (
            "Each completed assignment has one previous-prefix remainder and one "
            "last digit, so it follows exactly one transition. Conversely every "
            "transition appends a permitted digit, making the DP a partition of all "
            "assignments by remainder."
        ),
        "complexity": "O(130|S|) time and O(13) memory.",
        "traps": "Reduce after every addition and distinguish the character '?' from a digit.",
    },
    {
        "id": "abc187_e",
        "title": "Through Path",
        "rating": 1400,
        "bridge": "Sections 4 and 26",
        "summary": (
            "Each query names a tree edge, chooses one of its two sides, and adds x "
            "to every vertex on that side. Print all final vertex values."
        ),
        "idea": (
            "Root the tree. For a query affecting a child's subtree, add x at the "
            "child. For the complementary side, add x to a global/root difference "
            "and subtract x at that child. One prefix propagation resolves all "
            "queries."
        ),
        "proof": (
            "A rooted edge splits the tree into exactly the child's subtree and its "
            "complement. The two difference encodings mark precisely one of those "
            "sets; root-to-leaf prefix sums convert the markers into per-vertex totals."
        ),
        "complexity": "O(N+Q) time and O(N) memory.",
        "traps": "Determine which endpoint is the child before interpreting the query type.",
    },
    {
        "id": "abc184_e",
        "title": "Third Avenue",
        "rating": 1400,
        "bridge": "Section 15",
        "summary": (
            "Find a shortest path through a grid with walls. Equal lowercase letters "
            "are teleport stations: from a letter cell one move may reach any other "
            "cell with that letter."
        ),
        "idea": (
            "Run BFS. When a letter is first expanded, enqueue every cell carrying "
            "that letter, then clear or mark that letter's list so it is never "
            "expanded globally again."
        ),
        "proof": (
            "BFS processes states in nondecreasing distance, so the first expansion "
            "of a letter already offers its cheapest possible teleport distance. "
            "Repeating the same complete teleport list later cannot improve any cell."
        ),
        "complexity": "O(HW) time and O(HW) memory.",
        "traps": "Without consuming each letter group once, repeated scans become quadratic.",
    },
    {
        "id": "abc245_f",
        "title": "Endless Walk",
        "rating": 1500,
        "bridge": "Sections 17 and 38",
        "summary": (
            "Count vertices of a directed graph from which one can follow directed "
            "edges forever."
        ),
        "idea": (
            "Compress strongly connected components. A component is cyclic when it "
            "has at least two vertices or a self-loop. In the reversed condensation "
            "DAG, mark every component that can reach a cyclic component."
        ),
        "proof": (
            "An infinite walk in a finite graph must repeat a vertex and hence reach "
            "a directed cycle. Conversely, after reaching a cyclic SCC one can loop "
            "forever. Reverse reachability therefore characterizes exactly the valid "
            "starting components."
        ),
        "complexity": "O(N+M) time and O(N+M) memory.",
        "traps": "A one-vertex SCC is cyclic only if it has a self-loop.",
    },
    {
        "id": "abc174_f",
        "title": "Range Set Query",
        "rating": 1500,
        "bridge": "Sections 13 and 36",
        "summary": (
            "Answer many inclusive array-range queries asking for the number of "
            "distinct colors."
        ),
        "idea": (
            "Sort queries by right endpoint. During a left-to-right sweep, keep a "
            "Fenwick 1 only at the latest occurrence of each color: erase the old "
            "position, add the new one, then range-sum [L,R]."
        ),
        "proof": (
            "At sweep position R, a color contributes one marker to [L,R] exactly "
            "when its latest occurrence at or before R is at least L, which is "
            "equivalent to that color occurring in the queried range."
        ),
        "complexity": "O((N+Q) log N) time and O(N+Q) memory.",
        "traps": "Queries must be answered only after the sweep reaches their R.",
    },
    {
        "id": "abc210_d",
        "title": "National Railway",
        "rating": 1500,
        "bridge": "Sections 22 and 28",
        "summary": (
            "Choose two distinct grid cells for stations. Their cost is both cell "
            "prices plus C times Manhattan distance; minimize it."
        ),
        "idea": (
            "For a second station (i,j), the best earlier station contributes "
            "A[x][y]-C(x+y), while the new station contributes A[i][j]+C(i+j). "
            "Scan a direction while maintaining the minimum transformed value, then "
            "mirror columns and repeat for the missing orientation."
        ),
        "proof": (
            "Within one scan orientation the Manhattan absolute values have fixed "
            "signs, so the pair cost separates into an earlier-station term and a "
            "current-station term. The mirrored pass covers every unordered pair."
        ),
        "complexity": "O(HW) time and O(1) extra memory beyond the grid.",
        "traps": "Update the answer before inserting the current cell to forbid choosing it twice.",
    },
    {
        "id": "abc190_e",
        "title": "Magical Ornament",
        "rating": 1600,
        "bridge": "Sections 15 and 27",
        "summary": (
            "In an unweighted graph, find the minimum number of visited vertices in "
            "a walk that visits every one of K special vertices, or report impossibility."
        ),
        "idea": (
            "BFS from each special vertex to obtain pairwise shortest distances. "
            "Then run subset DP where dp[mask][last] is the minimum edge count of a "
            "walk visiting mask and ending at special vertex last."
        ),
        "proof": (
            "Between consecutive special vertices an optimal walk may use a shortest "
            "path. The subset DP enumerates every order of first visits, and replacing "
            "each segment by its BFS distance cannot worsen a solution."
        ),
        "complexity": "O(K(N+M)+K^2 2^K) time and O(KN+K2^K) memory.",
        "traps": "The requested number of vertices is the minimum edge count plus one.",
    },
    {
        "id": "abc196_e",
        "title": "Filters",
        "rating": 1700,
        "bridge": "Sections 10 and 49",
        "summary": (
            "Compose many operations of three kinds on a number: add a, replace by "
            "max(x,a), or replace by min(x,a). Answer the final value for many inputs."
        ),
        "idea": (
            "Any prefix of operations is a translated clamp: clamp(x+add, low, high). "
            "Update add and both bounds for an addition; update the bounds under max "
            "or min. Evaluate each query with the final triple."
        ),
        "proof": (
            "The identity is a translated clamp. Addition translates all three "
            "parameters, while max and min clamp both endpoints. Induction over the "
            "operations proves the representation remains exact."
        ),
        "complexity": "O(N+Q) time and O(1) auxiliary memory.",
        "traps": "When a clamp crosses both bounds, both endpoints can collapse to one value.",
    },
    {
        "id": "abc204_e",
        "title": "Rush Hour 2",
        "rating": 1700,
        "bridge": "Section 19",
        "summary": (
            "An undirected edge entered at integer time t arrives at t+C+floor(D/(t+1)); "
            "waiting before entering is allowed. Find the earliest arrival from 1 to N."
        ),
        "idea": (
            "Use Dijkstra, but relax an edge by minimizing f(t)=t+C+D/(t+1) over "
            "integer t at least the current time. The unconstrained minimum lies near "
            "sqrt(D), so test the current time and a small neighborhood around sqrt(D)."
        ),
        "proof": (
            "The discrete function decreases before its square-root region and "
            "increases after it; the constrained minimum is therefore either the "
            "current time or an integer next to sqrt(D). Exact relaxation costs are "
            "nonnegative and FIFO, so Dijkstra remains valid."
        ),
        "complexity": "O((N+M) log N) time with a constant number of edge evaluations.",
        "traps": "Integer division and the t+1 denominator make off-by-one tests essential.",
    },
    {
        "id": "abc192_f",
        "title": "Potion",
        "rating": 1800,
        "bridge": "Sections 23 and 27",
        "summary": (
            "Choose a nonempty subset of the given positive values so that adding "
            "the same integer amount to every chosen value makes their sum equal X. "
            "Minimize that common added amount."
        ),
        "idea": (
            "Fix subset size k. The chosen sum S must satisfy S congruent to X modulo "
            "k and S<=X; maximize such S with a DP over item count and remainder. "
            "The candidate answer is (X-S)/k. Try every k."
        ),
        "proof": (
            "For fixed k, a feasible common increment exists exactly under the two "
            "conditions above, and maximizing S minimizes the increment. The DP "
            "enumerates every k-element subset by its remainder, while the outer loop "
            "covers every possible subset size."
        ),
        "complexity": "O(N^3) time and O(N^2) memory under N<=100.",
        "traps": "Store the maximum sum for a state, not the minimum, and reject sums above X.",
    },
    {
        "id": "abc061_d",
        "title": "Score Attack",
        "rating": 1800,
        "bridge": "Section 19",
        "summary": (
            "Find the maximum score of a directed path from vertex 1 to vertex N. "
            "If a positive cycle usable on such a path makes the score unbounded, "
            "print inf."
        ),
        "idea": (
            "Negate edge scores and run Bellman-Ford minimization. Mark vertices "
            "whose distance can still improve on later rounds, propagate that mark "
            "forward, and report infinity only if N is marked and reachable."
        ),
        "proof": (
            "A post-(N-1)-round improvement is possible exactly through a reachable "
            "negative cycle in the negated graph. Propagation identifies vertices "
            "reachable after using such a cycle, so N is marked exactly when the "
            "original maximum can grow without bound."
        ),
        "complexity": "O(NM) time and O(N+M) memory.",
        "traps": "A positive cycle irrelevant to every 1-to-N path must not cause inf.",
    },
    {
        "id": "abc172_e",
        "title": "NEQ",
        "rating": 1900,
        "bridge": "Sections 32 and 33",
        "summary": (
            "Count ordered pairs of length-N injective sequences A and B over "
            "1..M such that A_i differs from B_i at every position, modulo 1e9+7."
        ),
        "idea": (
            "Choose A in P(M,N) ways. For a fixed A, apply inclusion-exclusion "
            "over positions forced to satisfy B_i=A_i: choosing k such positions "
            "leaves P(M-k,N-k) injective completions for B."
        ),
        "proof": (
            "Each B with exactly t forbidden equalities appears in the alternating "
            "sum once for every subset of those t positions, with coefficient "
            "sum_k (-1)^k C(t,k), which is one when t=0 and zero otherwise."
        ),
        "complexity": "O(N) time after O(M) factorial preprocessing and O(M) memory.",
        "traps": "The forced values also consume k distinct symbols from B's available pool.",
    },
    {
        "id": "abc285_f",
        "title": "Substring of Sorted String",
        "rating": 1900,
        "bridge": "Sections 36, 37, and 44",
        "summary": (
            "Support point character updates and queries asking whether a substring "
            "could appear as one contiguous block in the globally sorted string."
        ),
        "idea": (
            "Maintain Fenwick counts for all 26 letters and another Fenwick marking "
            "descents S[i]>S[i+1]. A queried substring must have no descent. In "
            "addition, every globally present letter strictly between its endpoint "
            "letters must occur entirely inside the substring."
        ),
        "proof": (
            "A block of a sorted string is nondecreasing and cannot omit an "
            "occurrence of an intermediate letter, proving necessity. Those two "
            "conditions also place the substring's letter runs exactly where the "
            "corresponding global sorted runs occur, proving sufficiency."
        ),
        "complexity": "O(26 log N) per update or query and O(26N) memory.",
        "traps": "Only letters strictly between the first and last require full global counts.",
    },
    {
        "id": "abc223_f",
        "title": "Parenthesis Checking",
        "rating": 1900,
        "bridge": "Sections 4 and 37",
        "summary": (
            "Support swaps of two parentheses and queries asking whether an "
            "inclusive substring is a correct bracket sequence."
        ),
        "idea": (
            "Let pref[i] be the bracket balance through i. A substring [l,r] is "
            "valid when pref[r]=pref[l-1] and its minimum prefix on [l,r] is at "
            "least pref[l-1]. Swapping unequal endpoints is a range addition on "
            "the prefix array, handled by a lazy segment tree."
        ),
        "proof": (
            "The two conditions are exactly final balance zero and no relative "
            "prefix balance below zero. A swap changes contributions only between "
            "the two indices, so the stated range update keeps every pref value exact."
        ),
        "complexity": "O(log N) per operation and O(N) memory.",
        "traps": "The comparison baseline is pref[l-1], not zero in the global prefix array.",
    },
    {
        "id": "abc254_f",
        "title": "Rectangle GCD",
        "rating": 1900,
        "bridge": "Sections 13 and 35",
        "summary": (
            "For arrays A and B, the conceptual matrix has value A_i+B_j. Answer "
            "the gcd of every value in many queried row-column rectangles."
        ),
        "idea": (
            "Choose A_h1+B_w1 as a base. Every other value differs from it by a "
            "sum of adjacent differences from A and B. The rectangle gcd is the "
            "gcd of the base, gcd of A differences in its row interval, and gcd of "
            "B differences in its column interval."
        ),
        "proof": (
            "All matrix values are integer combinations of the three gcd inputs, "
            "so their gcd is a multiple of the computed value. Conversely each "
            "adjacent difference is a difference of two matrix cells, so the true "
            "rectangle gcd divides every input."
        ),
        "complexity": "O((N+Q) log N) time with segment trees and O(N) memory.",
        "traps": "A one-row or one-column difference range is empty and contributes zero.",
    },
    {
        "id": "abc253_f",
        "title": "Operations on a Matrix",
        "rating": 1900,
        "bridge": "Sections 36 and 42",
        "summary": (
            "An initially zero matrix supports adding x to every cell in a column "
            "interval, assigning every cell of one row to x, and point-value queries."
        ),
        "idea": (
            "Sweep operations offline with a Fenwick tree for column additions. "
            "For each point query, find the most recent assignment of its row. At "
            "that assignment time record and subtract the then-current column "
            "addition; at query time add the current one to the assigned base value."
        ),
        "proof": (
            "A row assignment erases exactly all column additions that occurred "
            "before it, while additions afterward remain effective. Subtracting the "
            "Fenwick value at the last assignment and adding its value at query time "
            "isolates precisely that suffix of additions."
        ),
        "complexity": "O((N+Q) log M) time and O(N+Q) memory.",
        "traps": "Online storage of every matrix cell is impossible; bind queries to row assignments offline.",
    },
    {
        "id": "abc199_f",
        "title": "Graph Smoothing",
        "rating": 2100,
        "bridge": "Sections 32 and 50",
        "summary": (
            "Repeat a random edge-based averaging operation K times on graph vertex "
            "values and print the expected final value at every vertex modulo a prime."
        ),
        "idea": (
            "Expectation is linear. Build an N by N transition matrix whose row "
            "describes one step's expected contribution to each vertex, including "
            "the probability that it is untouched. Raise the matrix to K and apply "
            "it to the initial-value vector."
        ),
        "proof": (
            "Conditioning on the random edge and endpoint makes each next expected "
            "value a linear combination of current expected values. Thus one step "
            "is exactly matrix multiplication, and induction makes K steps T^K."
        ),
        "complexity": "O(N^3 log K) time and O(N^2) memory.",
        "traps": "Convert division probabilities to modular inverses; do not simulate outcomes.",
    },
    {
        "id": "abc256_f",
        "title": "Cumulative Cumulative Cumulative Sum",
        "rating": 2100,
        "bridge": "Sections 4 and 36",
        "summary": (
            "Support point assignments in an array and queries for a third-order "
            "prefix sum, all modulo 998244353."
        ),
        "idea": (
            "Expand an element's contribution to query position x as a quadratic "
            "polynomial in x. Maintain three Fenwick trees for the coefficients "
            "involving A_i, i*A_i, and i^2*A_i; a point assignment updates all three."
        ),
        "proof": (
            "Counting how many times A_i appears through three cumulative sums gives "
            "a binomial coefficient in x-i, which expands into the maintained basis. "
            "Summing the three coefficient prefix queries reconstructs exactly every "
            "element's multiplicity."
        ),
        "complexity": "O(log N) per operation and O(N) memory.",
        "traps": "Derive the polynomial on paper; missing the modular inverse of 2 shifts every answer.",
    },
    {
        "id": "abc205_f",
        "title": "Grid and Tokens",
        "rating": 2100,
        "bridge": "Section 45",
        "summary": (
            "Each token may be placed in one cell of its allowed rectangle or not "
            "placed. No two placed tokens may share a row or a column; maximize the "
            "number placed."
        ),
        "idea": (
            "Build a unit-capacity flow network source -> rows -> tokens -> columns "
            "-> sink. Connect a row to a token when it lies in the token's row "
            "interval, and the token to every allowed column."
        ),
        "proof": (
            "An integral unit of flow chooses one row, one token, and one column, "
            "hence one legal cell. Unit capacities enforce distinct tokens, rows, "
            "and columns. Every legal placement maps back to edge-disjoint flow units."
        ),
        "complexity": "Polynomial max-flow time on O(H+W+N) vertices and O(N(H+W)) edges.",
        "traps": "The token itself needs capacity one; otherwise one rectangle could carry several units.",
    },
    {
        "id": "abc237_g",
        "title": "Range Sort Query",
        "rating": 2100,
        "bridge": "Sections 8 and 37",
        "summary": (
            "A permutation undergoes many operations sorting a subarray ascending "
            "or descending. Report the final position of a distinguished value X."
        ),
        "idea": (
            "For a candidate threshold v, replace each value by the bit [value>=v]. "
            "A range sort merely packs the range's zeroes and ones in a known order, "
            "which a lazy segment tree simulates. Binary-search the final value at "
            "each position, or compare thresholds X and X+1 to locate X."
        ),
        "proof": (
            "Sorting preserves the count of elements on each side of a threshold "
            "and makes their bits contiguous, so the binary simulation is exact. "
            "Threshold membership is monotone in v, enabling reconstruction of the "
            "distinguished value's final position."
        ),
        "complexity": "O((N+Q) log^2 N) time and O(N) memory.",
        "traps": "Ascending and descending operations pack the one-block on opposite sides.",
    },
    {
        "id": "abc339_g",
        "title": "Smaller Sum",
        "rating": 1800,
        "bridge": "Sections 13 and 42",
        "summary": (
            "For online-decoded queries, return the sum of array values no greater "
            "than X inside [L,R]. Each query's parameters are XORed with the previous answer."
        ),
        "idea": (
            "Build a merge-sort tree. At every node store its sorted values and "
            "their prefix sums. Decompose [L,R] into tree nodes; binary-search X in "
            "each node and add the corresponding prefix sum."
        ),
        "proof": (
            "The segment-tree decomposition partitions the query range. Within a "
            "node, upper_bound selects exactly values <=X, and its prefix sum counts "
            "each selected array element once. Online decoding happens before querying."
        ),
        "complexity": "O(log^2 N) per query and O(N log N) memory.",
        "traps": "Queries cannot be reordered because the previous answer decodes the next one.",
    },
    {
        "id": "abc132_f",
        "title": "Small Products",
        "rating": 2100,
        "bridge": "Sections 22 and 49",
        "summary": (
            "Count length-K positive integer sequences satisfying the problem's "
            "adjacent product bound, modulo 1e9+7, with N too large for one state per value."
        ),
        "idea": (
            "Transitions depend on floor(N/x), which takes only O(sqrt N) distinct "
            "values. Group equal quotients into intervals and run the DP on those "
            "blocks, using prefix sums to aggregate all predecessors of a block."
        ),
        "proof": (
            "All x in one quotient block have the same legal bound for the adjacent "
            "value and therefore identical transitions. Replacing individual states "
            "by block totals loses no information and prefix sums evaluate each "
            "transition exactly."
        ),
        "complexity": "O(K sqrt N) time and O(sqrt N) memory.",
        "traps": "Store each block's multiplicity; equal transition behavior does not mean one value.",
    },
    {
        "id": "abc296_g",
        "title": "Polygon and Points",
        "rating": 2200,
        "bridge": "Section 54",
        "summary": (
            "For many query points, classify each as strictly inside, on the "
            "boundary of, or outside a convex polygon listed in cyclic order."
        ),
        "idea": (
            "Normalize orientation and use one polygon vertex as a fan apex. Cross "
            "products first reject points outside the fan wedge; binary search finds "
            "the containing triangle, followed by an exact side and segment test."
        ),
        "proof": (
            "The rays from the apex partition a convex polygon into non-overlapping "
            "triangles in angular order. A point in the wedge belongs to exactly one "
            "candidate sector, and the final cross-product signs exactly characterize "
            "that triangle including its boundary."
        ),
        "complexity": "O((N+Q) log N) time and O(N) memory.",
        "traps": "Collinearity needs a bounding-box test; being on an infinite line is not enough.",
    },
    {
        "id": "abc238_g",
        "title": "Cubic?",
        "rating": 2300,
        "bridge": "Sections 33 and 42",
        "summary": (
            "For each array range, decide whether the product of its elements is a "
            "perfect cube."
        ),
        "idea": (
            "Factor every value and keep each prime exponent modulo 3. Process "
            "queries with Mo's algorithm, updating the current residue for affected "
            "primes and a counter of how many residues are nonzero."
        ),
        "proof": (
            "An integer is a cube exactly when every prime exponent is divisible by "
            "3. The moving window's residue table is the componentwise sum of the "
            "factorizations in that window, so the product is cubic exactly when the "
            "nonzero-residue counter is zero."
        ),
        "complexity": "About O((N+Q)sqrt(N) log A) time after factorization and O(A) memory.",
        "traps": "Removing a value subtracts exponents modulo 3; normalize negative residues.",
    },
    {
        "id": "abc265_g",
        "title": "012 Inversion",
        "rating": 2400,
        "bridge": "Section 37",
        "summary": (
            "An array over {0,1,2} supports range symbol permutations and queries "
            "for the inversion count of a range."
        ),
        "idea": (
            "A segment-tree node stores counts of each symbol and ordered-pair counts "
            "for all six unequal symbol pairs. Merging adds internal pairs and cross "
            "products. A lazy permutation simply relabels both dimensions."
        ),
        "proof": (
            "Every ordered pair in a merged segment is wholly left, wholly right, or "
            "crosses the midpoint, giving the merge formula. Relabeling is a bijection "
            "on symbols, so permuting table indices updates a node without inspecting "
            "individual elements."
        ),
        "complexity": "O(log N) per operation and O(N) memory.",
        "traps": "Store all ordered pairs, not only the three pairs currently counted as inversions.",
    },
    {
        "id": "abc338_g",
        "title": "evall",
        "rating": 2600,
        "bridge": "Sections 31 and 49",
        "summary": (
            "Sum the usual arithmetic value of every digit-bounded substring of a "
            "long expression containing digits, '+', and '*', modulo 998244353."
        ),
        "idea": (
            "Scan the expression while maintaining aggregate states for all valid "
            "substrings ending at the current digit: their completed additive terms, "
            "current multiplicative terms, and decimal-number contributions. Each "
            "digit, multiplication sign, and addition sign applies a fixed linear "
            "state transition."
        ),
        "proof": (
            "Every valid substring ending at a digit has a unique decomposition into "
            "completed plus-terms, the current product, and its current decimal token. "
            "The transitions reproduce ordinary precedence, and summing the state "
            "after each digit counts every endpoint pair once."
        ),
        "complexity": "O(|S|) time and O(1) aggregate state.",
        "traps": "Decimal concatenation and multiplication precedence require separate aggregates.",
    },
    {
        "id": "agc003_d",
        "title": "Anticube",
        "rating": 2600,
        "bridge": "Sections 33 and 35",
        "summary": (
            "Choose the largest subset of integers such that the product of no two "
            "chosen elements is a perfect cube."
        ),
        "idea": (
            "Reduce each value to a canonical cube-free signature of prime exponents "
            "modulo 3. Its unique complementary signature uses exponents 3-e. For "
            "each signature/complement pair keep the larger frequency; handle the "
            "self-complementary signature 1 once."
        ),
        "proof": (
            "Two values multiply to a cube exactly when their signatures are "
            "complements. No other signature pair conflicts, while within one "
            "nontrivial signature class values are compatible. Each independent "
            "pair therefore contributes its larger side."
        ),
        "complexity": "O(N sqrt(cuberoot(A))) expected factor work plus map operations.",
        "traps": "Large leftover factors may be a prime, a square of a prime, or a product of two primes.",
    },
    {
        "id": "abc354_g",
        "title": "Select Strings",
        "rating": 2700,
        "bridge": "Sections 44 and 45",
        "summary": (
            "Select a maximum-value compatible subset of weighted strings under the "
            "problem's substring-conflict rule."
        ),
        "idea": (
            "Discard dominated duplicates, find all relevant substring relations "
            "with string matching, and express the remaining choice as a maximum "
            "weight closure / bipartite minimum-cut instance. Positive weights attach "
            "to the source, penalties to the sink, and infinite edges enforce implications."
        ),
        "proof": (
            "A finite cut cannot separate a selected object from any choice forced "
            "by it, so source-side vertices encode exactly feasible selections. The "
            "cut capacity equals total positive weight minus selected profit, making "
            "minimum cut equivalent to maximum achievable value."
        ),
        "complexity": "Polynomial string preprocessing plus one max-flow on O(N) logical vertices.",
        "traps": "Equal strings and non-positive weights must be normalized before building implications.",
    },
    {
        "id": "abc239_g",
        "title": "Builder Takahashi",
        "rating": 2200,
        "bridge": "Section 45",
        "summary": (
            "Vertices other than 1 and N have destruction costs. Find the minimum "
            "cost of vertices whose removal disconnects 1 from N, and output one "
            "optimal set."
        ),
        "idea": (
            "Split every vertex v into v_in -> v_out with capacity cost[v]. Give "
            "original undirected adjacencies infinite-capacity directed edges between "
            "the appropriate halves. A minimum 1-to-N cut gives the cost; inspect "
            "residual reachability to recover split edges crossing the cut."
        ),
        "proof": (
            "Any finite cut can cross original adjacency edges only at prohibitive "
            "cost, so it pays through split edges and therefore names removed vertices. "
            "Conversely any disconnecting vertex set cuts those split edges. The two "
            "cost-preserving mappings make min-cut exact."
        ),
        "complexity": "One max-flow on O(N) vertices and O(N+M) edges.",
        "traps": "Vertices 1 and N need infinite split capacity and must never appear in the answer.",
    },
    {
        "id": "abc274_g",
        "title": "Security Camera 3",
        "rating": 2300,
        "bridge": "Section 45",
        "summary": (
            "Cover all open grid cells using the minimum number of axis-aligned "
            "camera segments, with walls breaking visibility."
        ),
        "idea": (
            "Compress every maximal horizontal open run and every maximal vertical "
            "open run. Each open cell is an edge between its two runs. Choosing camera "
            "runs to cover every cell is minimum vertex cover in a bipartite graph, "
            "whose size equals maximum matching by Konig's theorem."
        ),
        "proof": (
            "A camera placed along a run covers exactly all cell-edges incident to "
            "that run, so feasible camera sets and bipartite vertex covers coincide. "
            "Konig's theorem then equates the optimum with the computed matching."
        ),
        "complexity": "O(HW sqrt(HW)) time with Hopcroft-Karp and O(HW) memory.",
        "traps": "Walls create new run identifiers; rows and columns are separate bipartite sides.",
    },
    {
        "id": "agc026_e",
        "title": "Synchronized Subsequence",
        "rating": 3000,
        "bridge": "Sections 22 and 44",
        "summary": (
            "A length-2N string contains N 'a' and N 'b'. For every rank i, either "
            "select both the i-th 'a' and i-th 'b', or neither; maximize the selected "
            "subsequence lexicographically."
        ),
        "idea": (
            "Treat equal-rank occurrences as linked choices and scan candidate first "
            "'b' positions, because any nonempty optimum prefers 'b'. A suffix DP "
            "stores the best feasible continuation after each linked pair; compare "
            "candidate continuations by ranks/LCP information instead of copying "
            "quadratic-length strings at every transition."
        ),
        "proof": (
            "The first differing selected character decides lexicographic order. "
            "Conditioning on the first selected pair partitions all feasible answers, "
            "and the linked-pair DP considers every legal next pair while retaining "
            "only the greatest continuation for an identical suffix state."
        ),
        "complexity": "O(N^2) time and O(N^2) comparison/rank state.",
        "traps": "The pair is by occurrence rank, not by adjacent positions in S.",
    },
    {
        "id": "agc006_d",
        "title": "Median Pyramid Hard",
        "rating": 3100,
        "bridge": "Section 8",
        "summary": (
            "The bottom row is a permutation of 1..2N-1. Each upper block is the "
            "median of its three children; find the value at the pyramid's top."
        ),
        "idea": (
            "Binary-search a threshold X and replace each bottom value by whether it "
            "is at least X. Median becomes majority on bits. The top bit is determined "
            "by the closest equal adjacent bit-pair to the center; if none exists, "
            "the alternating pattern propagates a value from an edge. This yields an "
            "O(N) monotone predicate."
        ),
        "proof": (
            "Thresholding commutes with median: median(values)>=X exactly when at "
            "least two threshold bits are one. In a binary majority pyramid, the "
            "nearest stable equal pair dominates all levels above it; only a fully "
            "alternating corridor reaches an edge. Hence the predicate is exact and monotone."
        ),
        "complexity": "O(N log N) time and O(1) auxiliary memory.",
        "traps": "Prove which member of an alternating edge pattern reaches the top before coding indices.",
    },
    {
        "id": "arc108_e",
        "title": "Random IS",
        "rating": 3100,
        "bridge": "Sections 25 and 50",
        "summary": (
            "Repeatedly choose uniformly among currently addable chairs while keeping "
            "marked chair IDs increasing left-to-right. Find the expected final number marked."
        ),
        "idea": (
            "Add sentinel chairs and use interval DP between consecutive already "
            "chosen boundaries in both position and value. The first chair selected "
            "inside a valid rectangle splits it into independent left and right "
            "rectangles; average those contributions over all currently nice pivots."
        ),
        "proof": (
            "Once a pivot is selected, any future compatible chair lies wholly in "
            "one of the two induced position/value rectangles, and choices in the "
            "two rectangles do not constrain each other. Conditioning on the uniformly "
            "chosen first pivot therefore gives the interval expectation recurrence."
        ),
        "complexity": "O(N^2) optimized interval-DP time and O(N^2) memory.",
        "traps": "Uniformity is over currently nice chairs, so every recurrence divides by the pivot count.",
    },
    {
        "id": "agc023_f",
        "title": "01 on Tree",
        "rating": 3100,
        "bridge": "Sections 9, 26, and 39",
        "summary": (
            "Linearize a rooted tree so every ancestor precedes its descendants. "
            "Vertex labels are 0 or 1; minimize inversions in the resulting binary sequence."
        ),
        "idea": (
            "Represent a processed component by its counts (zero,one). When two "
            "available components are concatenated, their cross cost is ones_left "
            "times zeroes_right. The optimal order follows the ratio comparison "
            "one_A*zero_B <= one_B*zero_A. Repeatedly merge the best component into "
            "its parent using a priority queue and DSU."
        ),
        "proof": (
            "Swapping adjacent independent blocks changes only their cross inversions; "
            "the cross-product inequality gives exactly when A-before-B is no worse. "
            "This comparator is transitive. Contracting the chosen block into its "
            "mandatory parent preserves all remaining precedence constraints."
        ),
        "complexity": "O(N log N) time and O(N) memory.",
        "traps": "Add cross inversions before combining counts, and discard stale heap representatives.",
    },
    {
        "id": "agc023_d",
        "title": "Go Home",
        "rating": 3200,
        "bridge": "Sections 9 and 11",
        "summary": (
            "A bus starts at S carrying populations bound for apartments on a line. "
            "At every unit step, rational passengers vote for the direction that gets "
            "them home sooner; find when the final passenger exits."
        ),
        "idea": (
            "The still occupied destinations always form an interval. Compare total "
            "voting weight on the two sides using the problem's negative-direction "
            "tie rule, determine the extreme that must be served next, remove it, and "
            "recurse on the smaller interval while accumulating the necessary travel."
        ),
        "proof": (
            "For a passenger at an extreme, the two candidate first directions differ "
            "only by which surviving extreme is visited first. Backward induction on "
            "the number of occupied apartments turns every vote into the same side-weight "
            "comparison, making the chosen extreme forced and preserving the interval invariant."
        ),
        "complexity": "O(N) time after sorted input and O(N) prefix-weight memory.",
        "traps": "Ties go in the negative direction and can change the forced extreme.",
    },
    {
        "id": "arc069_d",
        "title": "Flags",
        "rating": 3200,
        "bridge": "Sections 8, 17, and 37",
        "summary": (
            "Flag i may be placed at either x_i or y_i. Maximize the minimum distance "
            "between every pair of placed flags."
        ),
        "idea": (
            "Binary-search distance D. Each of the 2N candidate placements is a "
            "Boolean literal; choosing one forbids every other candidate within D. "
            "After sorting coordinates, encode each forbidden coordinate interval "
            "with O(log N) implications through segment-tree nodes, then test 2-SAT."
        ),
        "proof": (
            "The clauses enforce exactly one placement per flag and prohibit exactly "
            "the pairs whose distance is below D. Thus satisfiability is equivalent "
            "to a placement with minimum distance at least D. Feasibility is monotone."
        ),
        "complexity": "O(N log N log C) time and O(N log N) implication-graph memory.",
        "traps": "Exclude the literal itself from its forbidden interval and use strict distance <D.",
    },
    {
        "id": "agc017_f",
        "title": "Zigzag",
        "rating": 3400,
        "bridge": "Sections 27 and 37",
        "summary": (
            "Count ordered noncrossing down-left/down-right paths through a triangular "
            "grid, subject to fixed direction choices on selected path-step pairs."
        ),
        "idea": (
            "Encode each step of every path as a bit. Process triangle levels with a "
            "frontier DP whose mask records which neighboring paths have a strict "
            "horizontal gap; this is precisely the information needed to decide which "
            "next-step bit patterns preserve noncrossing order. Apply fixed-bit constraints "
            "while transferring masks."
        ),
        "proof": (
            "Given current path positions, future legality depends only on equalities "
            "between adjacent positions, represented by the frontier mask. Every legal "
            "column of step bits produces one next mask, and every noncrossing drawing "
            "produces one such transition sequence."
        ),
        "complexity": "O(NM 2^min(N,M) poly(min(N,M))) time and exponential frontier memory.",
        "traps": "Transpose the DP dimensions when useful; the exponential side must be at most 20.",
    },
    {
        "id": "agc032_e",
        "title": "Modulo Pairing",
        "rating": 3400,
        "bridge": "Sections 8 and 9",
        "summary": (
            "Pair 2N residues modulo M to minimize the maximum value of (x+y) mod M "
            "among the N pairs."
        ),
        "idea": (
            "Sort the values. An uncrossing exchange proves an optimum with one "
            "boundary: pairs before it have sums below M and pairs after it wrap "
            "around, with opposite ends paired in each region. Binary-search the "
            "leftmost feasible boundary and evaluate its maximum residue."
        ),
        "proof": (
            "For two crossing pairs, reconnecting endpoints into the canonical nested "
            "form does not increase their larger modular sum. Repeating uncrossing "
            "produces the boundary structure. Its feasibility changes monotonically "
            "as the boundary moves, justifying binary search."
        ),
        "complexity": "O(N log N) time and O(N) memory.",
        "traps": "Compare raw sums to M before applying modulo; wrap and non-wrap pairs obey different orders.",
    },
    {
        "id": "agc005_f",
        "title": "Many Easy Problems",
        "rating": 3400,
        "bridge": "Sections 26, 32, and 51",
        "summary": (
            "For every K=1..N, sum over all K-vertex sets the number of vertices in "
            "their minimum containing subtree, modulo 924844033."
        ),
        "idea": (
            "A vertex is absent from a chosen set's Steiner subtree exactly when all "
            "chosen vertices lie in one component formed after removing it. Summing "
            "over vertices yields N*C(N,K) minus, for every directed edge side of size "
            "s, C(s,K). Count side sizes, then evaluate all K simultaneously as a "
            "factorial-scaled convolution with NTT."
        ),
        "proof": (
            "For a fixed vertex, each set excluding it lies outside the Steiner tree "
            "in exactly one removal component, so no set is double-counted. Summing "
            "that identity gives the binomial formula; convolution is only an algebraic "
            "batch evaluation of the same terms."
        ),
        "complexity": "O(N log N) time and O(N) memory.",
        "traps": "Each undirected edge contributes both side sizes s and N-s.",
    },
    {
        "id": "agc024_f",
        "title": "Simple Subsequence Problem",
        "rating": 3500,
        "bridge": "Sections 27 and 44",
        "summary": (
            "A compact bit-table describes a set of binary strings of length at most "
            "N. Find the longest, then lexicographically smallest, string that is a "
            "subsequence of at least K members of the set."
        ),
        "idea": (
            "For every binary string state, compute how many present strings contain "
            "it as a subsequence. Propagate counts through the DAG formed by deleting "
            "a character, carefully deduplicating the two deletion paths that can "
            "reach the same subsequence. Scan lengths downward and masks upward to "
            "select the required longest lexicographically smallest state."
        ),
        "proof": (
            "Reachability in the deletion DAG is exactly the subsequence relation. "
            "The canonical/deduplicated propagation counts each containing source "
            "string once per target rather than once per embedding. The final scan "
            "applies the problem's two-level ordering directly."
        ),
        "complexity": "O(N 2^N) time and O(2^N) memory.",
        "traps": "Counting embeddings instead of distinct source strings gives a larger but wrong support count.",
    },
    {
        "id": "agc016_f",
        "title": "Games on DAG",
        "rating": 3800,
        "bridge": "Sections 27, 29, and 33",
        "summary": (
            "From a forward-edge DAG, choose any subset of edges. Two impartial-game "
            "tokens start at vertices 1 and 2; count edge subsets for which the first "
            "player wins."
        ),
        "idea": (
            "For a fixed graph, the position is winning exactly when Grundy(1) differs "
            "from Grundy(2). Count graphs by constructing the vertex sets with Grundy "
            "numbers 0,1,... in order. A subset DP state is the union already assigned; "
            "a transition chooses the next nonempty class and counts edge choices that "
            "hit every lower class, avoid the equal class, and are free toward higher classes."
        ),
        "proof": (
            "The mex definition gives exactly those three edge conditions for each "
            "vertex. Grouping vertices by Grundy number makes every compatible graph "
            "belong to one ordered partition. The subset transition counts its edge "
            "choices once, while forbidding vertices 1 and 2 from the same class "
            "selects exactly winning graphs."
        ),
        "complexity": "O(N 3^N) time and O(2^N) memory for N<=15.",
        "traps": "The game has two tokens, so the losing condition is equality of their Grundy numbers.",
    },
]

# Python's sort is stable, so equal-rated tasks keep the deliberate pedagogical
# order above while the published ladder remains nondecreasing by difficulty.
TASKS.sort(key=lambda task: task["rating"])

assert len(TASKS) == 50
assert len({task["id"] for task in TASKS}) == 50
