#!/usr/bin/env python3
"""Append full original-companion editorials to the two ladder documents."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKER = "# Offline Companion Editorials"


def load_population_module():
    path = ROOT / "tools/populate_ladder_companions.py"
    spec = importlib.util.spec_from_file_location("population", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load companion mapping")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_problem_d(source_package: str) -> str:
    source = ROOT / source_package
    editorial = source.parents[1] / "editorial.qmd"
    text = editorial.read_text()
    starts = list(re.finditer(r"^# (?:Problem )?D(?:[.:].*)?$", text, flags=re.MULTILINE))
    if not starts:
        raise RuntimeError(f"cannot find Problem D editorial in {editorial}")
    content = text[starts[-1].end():].lstrip("\n")
    # Source editorials may include their local code through Quarto's include
    # shortcode. Once copied into a ladder editorial that relative path would
    # point at the ladder package, so embed the source code instead.
    def replace_include(match: re.Match[str]) -> str:
        included = source.parents[1] / match.group(1)
        if not included.is_file():
            raise RuntimeError(f"missing included source file {included}")
        return included.read_text().rstrip()

    content = re.sub(r"\{\{< include (problems/[^ >]+) >\}\}", replace_include, content)
    if "```cpp" not in content or "```python" not in content:
        return add_missing_reference(source, content)
    return content


def add_missing_reference(source: Path, content: str) -> str:
    """Complete two historical D editorials that predate reference-code blocks."""
    cpp = (source / "solution.cpp").read_text().rstrip()
    python = (source / "solution.py").read_text().rstrip()
    if source.name == "d_equal_index_pairs":
        explanation = """
## Observation

Scan the array from left to right. Before processing position `j`, let
`freq[x]` be the number of earlier positions with value `x`. Exactly those
`freq[a[j]]` positions form a valid pair ending at `j`; add that number before
increasing the frequency. This counts every valid pair once, at its later
endpoint, and no invalid pair is counted because only equal values contribute.

## Correctness and complexity

The invariant is that `answer` equals the number of valid pairs entirely in
the processed prefix. Adding `freq[a[j]]` accounts for all and only pairs
`(i,j)` with `i<j` and equal values, then updating the map restores the
invariant. By induction the final answer is correct. Expected time is `O(n)`;
the map stores at most one entry per distinct value. Use 64-bit storage: an
all-equal array has `n(n-1)/2` pairs.

## Tests that matter

Test all values equal, all values distinct, negative values, and several test
cases whose lengths sum to the stated limit.
""".strip()
    elif source.name == "d_workshop_badges":
        explanation = """
## Reference implementations

The proof, trace, and hostile cases immediately above establish the greedy
choice. The missing part of the older source editorial was the concrete
implementation. `last_day` is deliberately represented by a separate boolean
or `None` state rather than a numeric sentinel because pickup days may be
negative. The comparison is strict: `last_day == left` still covers an
inclusive interval.
""".strip()
    else:
        raise RuntimeError(f"missing a complete C++ or Python reference in {source}")
    return "\n\n".join([
        content.rstrip(), explanation,
        "## Full C++ solution\n\n```cpp\n" + cpp + "\n```",
        "## Full Python solution\n\n```python\n" + python + "\n```",
    ])


def add_companion_appendix(section: Path, tasks: list[tuple[str, str, str, str]], label: str) -> None:
    editorial = section / "editorial.qmd"
    base = editorial.read_text().split(MARKER, 1)[0].rstrip() + "\n\n"
    lines = [
        MARKER,
        "",
        "The linked contest tasks above are external judge problems. The following",
        "entries are the full editorials for their original local companions. Each",
        "contains a complete C++ and Python reference implementation, a correctness",
        "argument, complexity analysis, and hostile-test guidance. The mapping is",
        "deliberate: use the companion to rehearse the course skill offline, then",
        "return to the linked contest task without treating the companion as a",
        "replacement for its statement.",
        "",
    ]
    for number, (slug, source, title, url) in enumerate(tasks, 1):
        lines.extend([
            f"## {number}. {title}: local companion",
            "",
            f"External {label} task: <{url}>",
            f"Local package: [problems/{slug}](problems/{slug}/README.md)",
            "",
        ])
        if source.endswith("a_scoreboard_replay"):
            # Its detailed derivation already appears before this appendix.
            package = section / "problems" / slug
            lines.extend([
                "The detailed scoreboard derivation appears earlier in this editorial.",
                "The two references below are repeated here so every companion entry",
                "is independently usable from the offline PDF.",
                "",
                "### Full C++ solution",
                "",
                "```cpp",
                (package / "solution.cpp").read_text().rstrip(),
                "```",
                "",
                "### Full Python solution",
                "",
                "```python",
                (package / "solution.py").read_text().rstrip(),
                "```",
                "",
            ])
        else:
            lines.append(extract_problem_d(source))
            lines.append("")
    editorial.write_text(base + "\n".join(lines).rstrip() + "\n")


def main() -> None:
    population = load_population_module()
    add_companion_appendix(ROOT / "sections/61_icpc_contest_readiness", population.ICPC, "Kattis")

    section = ROOT / "sections/62_codeforces_course_ladder"
    sheet = (section / "problem_sheet.qmd").read_text()
    urls = re.findall(r"Official: <(https://codeforces\.com/problemset/problem/[^>]+)>", sheet)
    headings = re.findall(r"^## \d+\. (.+)$", sheet, flags=re.MULTILINE)
    tasks = [
        (slug, population.course_source(number), headings[number - 1], urls[number - 1])
        for number, slug in enumerate(population.CF_NAMES, 1)
    ]
    add_companion_appendix(section, tasks, "Codeforces")


if __name__ == "__main__":
    main()
