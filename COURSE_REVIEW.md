# Course Review

This review was run against all 61 sections using the local artifact audit and
the reference-solution checker. It separates runnable-course health from
teaching quality: passing a reference implementation is necessary, but does
not prove that a learner can derive it.

## What is working

- The course has a consistent local problem layout: lesson, editorial, stubs,
  reference solutions, fixed tests, and generated tests.
- Sections 1--14 generally give a reader the observation, worked trace,
  proof shape, and common wrong turns expected from an instructional course.
- The new final section, Section 61, adds the missing transition from
  individual-algorithm practice to ICPC contest execution.
- The full reference suite passed after this review pass.

## Curriculum correction

The old plan listed lazy propagation at Section 38, but the actual Section 38
teaches static range queries and binary lifting. The plan now names the
material that exists. Do not tell learners that lazy propagation has been
covered until it has a dedicated lesson, exercises, and editorial.

## Structural remediation

The initial audit found three structural course-quality gaps. This pass
resolves them, but structural completeness is not the same as pedagogical
depth:

| Scope | Remediation |
|---|---|
| Sections 15--40 | Every lesson now ends with an exercise map that names the recognition signal and deliberate edge tests for its local problems. |
| Advanced editorials | Each previously flagged editorial now begins with a problem-specific proof map; the repeated generic proof and complexity claims were replaced. |
| Range-update structures | `appendices/lazy_propagation` is a standalone lazy-propagation lesson and editorial, with range-add, assignment, and bit-flip exercises. |

## Remaining substantive rewrite

Sections 29--60 still need a content rewrite before they meet the course's
"very pedagogical" bar. Many lessons are too short to establish recognition,
worked examples, proof habits, and implementation decisions; many editorials
do not yet give every problem a complete derivation, trace, and adversarial
test plan. The rewrite must deepen the documents themselves, not merely add
headings or proof summaries.

## Editorial rewrite bar

For an advanced local problem, a satisfactory editorial must answer all of
these without referring the reader to a vague overview:

1. What exact state or structure is maintained?
2. Why does one transition or operation preserve its invariant?
3. Why does that invariant imply the requested answer?
4. What are the precise time and memory bounds in the problem's variables?
5. Which small counterexample breaks each tempting wrong approach?

The audit now passes without structural or editorial-specificity notices. Run
it with:

```bash
python3 tools/audit_course.py
```

## This review pass

- Added Section 61: **ICPC Contest Readiness**, including a lesson, detailed
  editorial, rendered PDFs, an external queue, a five-hour simulation protocol,
  and three locally judged drills.
- Added independent small-instance random oracles for the scheduling and
  matching drills; the scoreboard generator computes its result directly from
  the stated event rules.
- Added `tools/audit_course.py` and `make audit` to review every section in one
  command.
- Fixed the local judge's temporary-directory cleanup so concurrent checks no
  longer delete another checker's C++ build output.
- Corrected the published Phase 5 map to match the sections that actually
  exist and added the missing lazy-propagation appendix.
