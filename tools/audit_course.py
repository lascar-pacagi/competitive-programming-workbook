"""Audit the course's local teaching artifacts and editorial specificity.

This is deliberately a content-review aid, not a gate that pretends a heading
proves a lesson is good.  It catches missing course artifacts as errors and
reports repeated generic editorial text as review debt.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
REQUIRED_SECTION_FILES = ("README.md", "PRACTICE.md", "lesson.qmd", "editorial.qmd", "check.py")
REQUIRED_PROBLEM_FILES = ("README.md", "manifest.json", "solve.cpp", "solve.py", "solution.cpp", "solution.py")
GENERIC_EDITORIAL_MARKERS = (
    "Correctness follows from the invariant proved in the detailed guide",
    "Correctness follows from the problem-specific argument in the detailed guide",
    "The complexity follows from the concrete loops and data structures",
    "The running time is the one derived in the detailed guide",
)


@dataclass
class Audit:
    errors: list[str]
    notices: list[str]

    def error(self, message: str) -> None:
        self.errors.append(message)

    def notice(self, message: str) -> None:
        self.notices.append(message)


def section_dirs() -> list[Path]:
    return sorted(path for path in SECTIONS.glob("[0-9][0-9]_*") if path.is_dir())


def audit_problem(problem: Path, report: Audit) -> None:
    for name in REQUIRED_PROBLEM_FILES:
        if not (problem / name).is_file():
            report.error(f"{problem.relative_to(ROOT)}: missing {name}")

    manifest = problem / "manifest.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.error(f"{manifest.relative_to(ROOT)}: invalid JSON ({exc.msg})")
        else:
            if "title" not in data:
                report.error(f"{manifest.relative_to(ROOT)}: missing title")

    tests = problem / "tests"
    inputs = sorted(tests.glob("*.in")) if tests.is_dir() else []
    if not inputs:
        report.error(f"{problem.relative_to(ROOT)}: no fixed input test")
    for input_path in inputs:
        if not input_path.with_suffix(".out").is_file():
            report.error(f"{input_path.relative_to(ROOT)}: missing matching .out")


def audit_section(section: Path, report: Audit) -> None:
    relative = section.relative_to(ROOT)
    for name in REQUIRED_SECTION_FILES:
        if not (section / name).is_file():
            report.error(f"{relative}: missing {name}")

    # A curated external-problem ladder has no local submissions to judge. Its
    # marker makes that exception explicit instead of weakening the usual
    # three-local-problem rule for ordinary teaching sections.
    external_only = (section / "EXTERNAL_ONLY.md").is_file()
    problems_dir = section / "problems"
    problems = sorted(path for path in problems_dir.iterdir() if path.is_dir()) if problems_dir.is_dir() else []
    if len(problems) < 3 and not external_only:
        report.error(f"{relative}: expected at least 3 local problems, found {len(problems)}")
    for problem in problems:
        audit_problem(problem, report)

    lesson = section / "lesson.qmd"
    if lesson.exists():
        text = lesson.read_text(encoding="utf-8")
        if "# Exercises" not in text:
            report.notice(f"{lesson.relative_to(ROOT)}: missing '# Exercises'")

    editorial = section / "editorial.qmd"
    if editorial.exists():
        text = editorial.read_text(encoding="utf-8")
        generic_count = sum(text.count(marker) for marker in GENERIC_EDITORIAL_MARKERS)
        if generic_count:
            report.notice(
                f"{editorial.relative_to(ROOT)}: {generic_count} generic proof/complexity marker(s); "
                "replace with problem-specific derivations"
            )
        headings = re.findall(r"^# (?:Problem )?[A-Z](?:\.|:)", text, flags=re.MULTILINE)
        if len(headings) < min(3, len(problems)):
            report.notice(
                f"{editorial.relative_to(ROOT)}: fewer than one top-level editorial block per local problem"
            )


def main() -> int:
    report = Audit(errors=[], notices=[])
    sections = section_dirs()
    if not sections:
        print("ERROR: no course sections found")
        return 1

    for section in sections:
        audit_section(section, report)

    print(f"Audited {len(sections)} section(s).")
    if report.errors:
        print(f"\nStructural errors ({len(report.errors)}):")
        print("\n".join(f"- {message}" for message in report.errors))
    if report.notices:
        grouped: dict[str, list[str]] = {}
        for notice in report.notices:
            kind = notice.split(": ", 1)[1]
            if "generic proof/complexity" in kind:
                group = "generic editorial proof/complexity text"
            elif "missing '# Exercises'" in kind:
                group = "lesson missing an exercises heading"
            elif "fewer than one top-level" in kind:
                group = "editorial problem blocks not detected"
            else:
                group = kind
            grouped.setdefault(group, []).append(notice)
        print(f"\nPedagogical review notices ({len(report.notices)}):")
        for group, notices in grouped.items():
            examples = ", ".join(item.split(":", 1)[0] for item in notices[:3])
            suffix = "" if len(notices) <= 3 else f", and {len(notices) - 3} more"
            print(f"- {group}: {len(notices)} ({examples}{suffix})")
    if not report.errors and not report.notices:
        print("No structural or editorial-specificity issues found.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
