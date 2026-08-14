#!/usr/bin/env python3
"""Build Section 63's AtCoder ladder and offline companion packages."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from atcoder_ladder_data import TASKS
from build_ladder_editorials import extract_problem_d


ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "sections/63_atcoder_difficulty_ladder"

QMD_HEADER = """---
title: "Competitive Programming"
subtitle: "{subtitle}"
author: "Competitive Programming Course"
date: last-modified
format:
  pdf:
    pdf-engine: xelatex
    documentclass: scrreprt
    papersize: a4
    toc: true
    toc-depth: 2
    number-sections: true
    colorlinks: true
    geometry:
      - margin={margin}
    include-in-header:
      text: |
        \\usepackage{{microtype}}
        \\usepackage{{amsmath}}
        \\usepackage{{booktabs}}
execute:
  enabled: false
---
"""

CPP_SKELETON = """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: implement your solution.
    return 0;
}
"""

PY_SKELETON = """import sys


def main() -> None:
    # TODO: implement your solution.
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    raise NotImplementedError("solve.py is for your solution")


if __name__ == "__main__":
    main()
"""


def official_url(task: dict[str, object]) -> str:
    contest = str(task["id"]).rsplit("_", 1)[0]
    return f"https://atcoder.jp/contests/{contest}/tasks/{task['id']}?lang=en"


def slug(index: int, task: dict[str, object]) -> str:
    name = re.sub(r"[^a-z0-9]+", "_", str(task["title"]).lower()).strip("_")
    return f"{index:02d}_{name}"


def source_package(index: int) -> Path:
    section_number = index + 10
    source_section = next(ROOT.glob(f"sections/{section_number:02d}_*"))
    packages = sorted((source_section / "problems").glob("d_*"))
    if len(packages) != 1:
        raise RuntimeError(f"expected one D package in {source_section}, found {packages}")
    return packages[0]


def gate(index: int) -> tuple[int, str]:
    if index <= 5:
        return 1, "short entry ramp"
    if index <= 15:
        return 2, "core intermediate"
    if index <= 30:
        return 3, "strong intermediate"
    if index <= 39:
        return 4, "advanced"
    if index <= 45:
        return 5, "orange"
    return 6, "red"


def copy_companion(index: int, task: dict[str, object]) -> Path:
    destination = SECTION / "problems" / slug(index, task)
    source = source_package(index)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

    readme = destination / "README.md"
    original = readme.read_text()
    if original.startswith("# "):
        original = original.split("\n", 1)[1]
    title = f"{task['id'].upper()} -- {task['title']}"
    preface = (
        f"# Offline companion: {title}\n\n"
        f"This is an original, locally judgeable companion for "
        f"[{title}]({official_url(task)}). It is **not** a copied AtCoder "
        "statement. Solve this package offline to practise a nearby course "
        "technique, then solve the linked official task on AtCoder.\n\n"
    )
    readme.write_text(preface + original)

    manifest = destination / "manifest.json"
    payload = json.loads(manifest.read_text())
    payload["title"] = f"Offline companion: {title}"
    manifest.write_text(json.dumps(payload, indent=2) + "\n")
    (destination / "solve.cpp").write_text(CPP_SKELETON)
    (destination / "solve.py").write_text(PY_SKELETON)
    return destination


def build_readme() -> None:
    text = """# Section 63: AtCoder Difficulty Ladder

This is a 50-problem AtCoder progression with a deliberately short novice
ramp and most of its work in the intermediate, advanced, orange, and red
ranges. Start with the offline [problem sheet](problem_sheet.pdf), record a
real attempt, and open [editorial.pdf](editorial.pdf) only when upsolving.

AtCoder does not publish problem colors. The rounded ratings in this section
are approximate AtCoder Problems estimates captured when the ladder was
authored; they are ordering guideposts, not official labels.

Every rung has an original local package in
[OFFLINE_COMPANIONS.md](OFFLINE_COMPANIONS.md), with neutral C++/Python
skeletons, references, fixed tests, and randomized tests. The local companion
is not a copy of the linked task.

```bash
python3 sections/63_atcoder_difficulty_ladder/check.py
```
"""
    (SECTION / "README.md").write_text(text)
    (SECTION / "EXTERNAL_ONLY.md").write_text(
        "# External submission targets\n\n"
        "The 50 AtCoder tasks remain external judge problems. This section stores "
        "original concise briefs, original analyses, and separate local companions; "
        "it does not mirror AtCoder statements or judge data.\n"
    )


def build_practice() -> None:
    lines = [
        "# AtCoder Difficulty Ladder Queue",
        "",
        "Solve in order. Ratings are rounded community estimates, not official",
        "AtCoder labels. Keep an attempt record before opening the editorial.",
        "",
        "| # | Gate | Task | Approx. rating | Course bridge | Status |",
        "|---:|---:|---|---:|---|---|",
    ]
    for index, task in enumerate(TASKS, 1):
        gate_number, _ = gate(index)
        link = f"[{task['id'].upper()} -- {task['title']}]({official_url(task)})"
        lines.append(
            f"| {index} | {gate_number} | {link} | {task['rating']} | "
            f"{task['bridge']} | pending |"
        )
    lines.extend([
        "",
        "## Attempt record",
        "",
        "```text",
        "task | first model | counterexample or obstruction",
        "final invariant | proof route | complexity | regression test",
        "```",
    ])
    (SECTION / "PRACTICE.md").write_text("\n".join(lines) + "\n")


def build_problem_sheet() -> None:
    lines = [
        QMD_HEADER.format(
            subtitle="Section 63: AtCoder Difficulty Ladder -- Offline Problem Sheet",
            margin="20mm",
        ).rstrip(),
        "",
        "# Offline use",
        "",
        "This sheet contains original concise briefs, not copied AtCoder statements.",
        "Each visible URL is the authoritative statement and submission page. Read it",
        "before submitting whenever you are online. Approximate ratings come from",
        "AtCoder Problems and are not official AtCoder labels.",
        "",
    ]
    current_gate = 0
    for index, task in enumerate(TASKS, 1):
        gate_number, gate_name = gate(index)
        if gate_number != current_gate:
            lines.extend([f"# Gate {gate_number}: {gate_name}", ""])
            current_gate = gate_number
        lines.extend([
            f"## {index}. {task['id'].upper()} -- {task['title']} "
            f"(approximately {task['rating']})",
            "",
            f"Official: <{official_url(task)}>",
            "",
            str(task["summary"]),
            "",
            f"Constraints and exact input/output syntax: see the official link. "
            f"Course bridge: {task['bridge']}.",
            "",
        ])
    (SECTION / "problem_sheet.qmd").write_text("\n".join(lines).rstrip() + "\n")


def build_lesson() -> None:
    lines = [
        QMD_HEADER.format(
            subtitle="Section 63: AtCoder Difficulty Ladder",
            margin="25mm",
        ).rstrip(),
        "",
        "# Why this ladder is weighted toward hard tasks",
        "",
        "The first five tasks establish AtCoder conventions; they are not the center",
        "of the section. Rungs 6--30 demand reliable recognition and implementation,",
        "31--39 combine several course tools, and 40--50 move through orange into",
        "red-level reductions. Difficulty is nondecreasing by rounded community rating.",
        "",
        "# Attempt protocol",
        "",
        "Before reading an editorial, write:",
        "",
        "```text",
        "slow exact model",
        "state or invariant",
        "first complexity bottleneck",
        "small hostile example",
        "```",
        "",
        "At the orange/red gates, a template name is not a model. Derive what every",
        "state, edge, coefficient, or implication means in the original problem.",
        "",
        "# Gate map",
        "",
        "| Gate | Rungs | Main pressure |",
        "|---:|---:|---|",
        "| 1 | 1--5 | exact loops, windows, functional graphs, tree propagation |",
        "| 2 | 6--15 | graph basics, subset DP, heap greedy, offline queries |",
        "| 3 | 16--30 | compressed DP, algebraic transforms, flow, range structures |",
        "| 4 | 31--39 | quotient compression, geometry, Mo, lazy composition, cuts |",
        "| 5 | 40--45 | proof-heavy string/expectation/tree reductions |",
        "| 6 | 46--50 | frontier DP, 2-SAT compression, NTT, subset transforms |",
        "",
        "# How to upsolve",
        "",
        "Read only through the first missing observation. Close the editorial and",
        "reconstruct the algorithm, proof, and complexity from memory. Then preserve",
        "the smallest test that disproved your original model. For red tasks, also",
        "implement a slow oracle on tiny inputs before the optimized version.",
        "",
        "# Rating and language caveats",
        "",
        "AtCoder task colors are community conventions derived from estimated",
        "difficulty. Estimates move as more submissions are observed. The official",
        "English task page controls the contract; the offline sheet is a compact",
        "practice brief rather than a replacement.",
        "",
        "# Exercises",
        "",
        "## A. Intermediate checkpoint",
        "",
        "Complete rungs 6--15. For each task, record one tempting wrong model and",
        "the smallest input that disproves it.",
        "",
        "## B. Reduction checkpoint",
        "",
        "For rungs 28, 33, 35, and 39, draw the graph, range structure, or state",
        "space used by the solution and label what every object means in the",
        "original statement.",
        "",
        "## C. Red checkpoint",
        "",
        "For each of rungs 46--50, first implement or specify a tiny exact oracle.",
        "Use it to test the optimized reduction on exhaustive small instances.",
        "",
        "# Submission checklist",
        "",
        "```text",
        "[ ] I read the official contract before submitting.",
        "[ ] I can state the invariant without the story.",
        "[ ] I proved the reduction used by my data structure.",
        "[ ] My complexity fits the constrained quantity.",
        "[ ] I kept one hostile regression test.",
        "```",
    ]
    (SECTION / "lesson.qmd").write_text("\n".join(lines) + "\n")


def build_companion_index(packages: list[Path]) -> None:
    lines = [
        "# Offline Companion Index",
        "",
        "Every package is an original course exercise with neutral C++/Python",
        "skeletons, two reference solutions, fixed tests, and randomized tests.",
        "It is separate from, and does not copy, the linked AtCoder task.",
        "",
        "| # | AtCoder task | Local companion |",
        "|---:|---|---|",
    ]
    for index, (task, package) in enumerate(zip(TASKS, packages), 1):
        lines.append(
            f"| {index} | [{task['id'].upper()} -- {task['title']}]"
            f"({official_url(task)}) | "
            f"[package](problems/{package.name}/README.md) |"
        )
    (SECTION / "OFFLINE_COMPANIONS.md").write_text("\n".join(lines) + "\n")


def build_editorial(packages: list[Path]) -> None:
    lines = [
        QMD_HEADER.format(
            subtitle="Section 63 Editorial: AtCoder Difficulty Ladder",
            margin="20mm",
        ).rstrip(),
        "",
        "# How to use this editorial",
        "",
        "For each task, stop after the first block that repairs your attempt. The",
        "proof is part of the solution: at the advanced gates, recognizing a data",
        "structure without proving the reduction is not enough.",
        "",
    ]
    for index, task in enumerate(TASKS, 1):
        lines.extend([
            f"# {index}. {task['id'].upper()} -- {task['title']} "
            f"(approximately {task['rating']})",
            "",
            f"Official task: <{official_url(task)}>",
            "",
            "## Restatement",
            "",
            str(task["summary"]),
            "",
            "## Recognition and derivation",
            "",
            str(task["idea"]),
            "",
            "Before implementing, write the slow literal model and identify exactly",
            "which repeated work the stated representation removes.",
            "",
            "## Correctness argument",
            "",
            str(task["proof"]),
            "",
            "## Complexity and implementation traps",
            "",
            f"{task['complexity']} {task['traps']}",
            "",
            "## Tests that matter",
            "",
            "Test the smallest legal instance, every equality boundary mentioned",
            "above, a case where the tempting literal algorithm chooses the wrong",
            "state, and a maximum-shaped case that exercises the complexity bound.",
            "",
        ])

    lines.extend([
        "# Offline Companion Editorials",
        "",
        "The entries below are full editorials for the original local companions.",
        "Each companion includes complete C++ and Python references, a proof,",
        "complexity analysis, and hostile-test guidance. It rehearses a nearby",
        "course skill but is not the AtCoder task itself.",
        "",
    ])
    for index, (task, package) in enumerate(zip(TASKS, packages), 1):
        source = source_package(index)
        lines.extend([
            f"## {index}. {task['id'].upper()} -- {task['title']}: local companion",
            "",
            f"Official AtCoder task: <{official_url(task)}>",
            f"Local package: [problems/{package.name}](problems/{package.name}/README.md)",
            "",
            extract_problem_d(str(source.relative_to(ROOT))).rstrip(),
            "",
        ])
    (SECTION / "editorial.qmd").write_text("\n".join(lines).rstrip() + "\n")


def build_check() -> None:
    text = """#!/usr/bin/env python3
\"\"\"Validate Section 63's 50 AtCoder companion packages.\"\"\"

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SECTION = Path(__file__).resolve().parent
PACKAGE_FILES = (
    "README.md", "manifest.json", "solve.cpp", "solve.py",
    "solution.cpp", "solution.py", "tests/sample1.in", "tests/sample1.out",
    "tests/edge1.in", "tests/edge1.out", "tests/random_cases.py",
)


def main() -> int:
    packages = sorted((SECTION / "problems").glob("[0-9][0-9]_*"))
    if len(packages) != 50:
        raise SystemExit(f"Section 63: expected 50 packages, found {len(packages)}")
    missing = [
        str((package / name).relative_to(SECTION))
        for package in packages
        for name in PACKAGE_FILES
        if not (package / name).is_file()
    ]
    if missing:
        raise SystemExit("Section 63: missing " + ", ".join(missing))
    if os.environ.get("CP_TARGET") != "solution":
        print("Section 63: 50 offline companion package contracts are complete.")
        print("Run with CP_TARGET=solution to verify all references.")
        return 0
    for package in packages:
        for language in ("cpp", "py"):
            result = subprocess.run(
                [sys.executable, "tools/judge.py", str(package),
                 "--lang", language, "--random-count", "6"],
                cwd=ROOT,
            )
            if result.returncode:
                return result.returncode
    print("Section 63 complete: all local reference solutions were accepted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""
    path = SECTION / "check.py"
    path.write_text(text)
    path.chmod(0o755)


def main() -> None:
    SECTION.mkdir(parents=True, exist_ok=True)
    packages = [copy_companion(index, task) for index, task in enumerate(TASKS, 1)]
    build_readme()
    build_practice()
    build_problem_sheet()
    build_lesson()
    build_companion_index(packages)
    build_editorial(packages)
    build_check()


if __name__ == "__main__":
    main()
