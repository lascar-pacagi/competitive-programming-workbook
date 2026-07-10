"""Local online-judge runner for course problems.

The runner expects a problem directory with this shape:

    manifest.json
    solve.py
    solve.cpp
    solution.py
    solution.cpp
    tests/
      sample1.in
      sample1.out
      ...
      random_cases.py    # optional

Set CP_TARGET=solution to run reference solutions instead of student stubs.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMP_DIRS: list[Path] = []


@dataclass(frozen=True)
class Case:
    name: str
    input_path: Path
    output_path: Path


def load_manifest(problem: Path) -> dict:
    manifest_path = problem / "manifest.json"
    if not manifest_path.exists():
        return {}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def source_for(problem: Path, lang: str, target: str) -> Path:
    if target not in {"student", "solution"}:
        raise ValueError(f"unknown target: {target}")
    if lang == "py":
        name = "solve.py" if target == "student" else "solution.py"
    elif lang == "cpp":
        name = "solve.cpp" if target == "student" else "solution.cpp"
    else:
        raise ValueError(f"unknown language: {lang}")
    source = problem / name
    if not source.exists():
        raise FileNotFoundError(f"missing {source}")
    return source


def discover_fixed_cases(problem: Path) -> list[Case]:
    tests = problem / "tests"
    cases: list[Case] = []
    for input_path in sorted(tests.glob("*.in")):
        output_path = input_path.with_suffix(".out")
        if not output_path.exists():
            raise FileNotFoundError(f"missing expected output for {input_path}")
        cases.append(Case(input_path.stem, input_path, output_path))
    return cases


def generate_random_cases(problem: Path, count: int, seed: int) -> list[Case]:
    generator = problem / "tests" / "random_cases.py"
    if count <= 0 or not generator.exists():
        return []

    tmp = Path(tempfile.mkdtemp(prefix="cp-course-random-"))
    TEMP_DIRS.append(tmp)
    cmd = [
        sys.executable,
        str(generator),
        "--count",
        str(count),
        "--seed",
        str(seed),
        "--out-dir",
        str(tmp),
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)

    cases: list[Case] = []
    for input_path in sorted(tmp.glob("*.in")):
        output_path = input_path.with_suffix(".out")
        if not output_path.exists():
            raise FileNotFoundError(f"generator did not create {output_path}")
        cases.append(Case(f"random/{input_path.stem}", input_path, output_path))
    return cases


def compile_cpp(source: Path) -> Path:
    build_dir = Path(tempfile.mkdtemp(prefix="cp-course-cpp-"))
    TEMP_DIRS.append(build_dir)
    binary = build_dir / "main"
    cmd = [
        "g++",
        "-std=c++17",
        "-O2",
        "-pipe",
        "-Wall",
        "-Wextra",
        str(source),
        "-o",
        str(binary),
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)
    return binary


def command_for(source: Path, lang: str) -> list[str]:
    if lang == "py":
        return [sys.executable, str(source)]
    if lang == "cpp":
        return [str(compile_cpp(source))]
    raise ValueError(f"unknown language: {lang}")


def normalize_tokens(text: str) -> list[str]:
    return text.split()


def outputs_match(actual: str, expected: str, checker: str, input_data: str) -> bool:
    if checker == "exact":
        return actual.rstrip("\n") == expected.rstrip("\n")
    if checker == "tokens":
        return normalize_tokens(actual) == normalize_tokens(expected)
    if checker == "diophantine":
        values = list(map(int, input_data.split()))
        if not values:
            return not actual.split()
        queries = values[0]
        tokens = actual.splitlines()
        if len(tokens) != queries:
            return False
        index = 1
        for line in tokens:
            a, b, c = values[index:index + 3]
            index += 3
            possible = math.gcd(a, b) != 0 and c % math.gcd(a, b) == 0
            fields = line.split()
            if not possible:
                if fields != ["IMPOSSIBLE"]:
                    return False
            elif len(fields) != 2:
                return False
            else:
                try:
                    x, y = map(int, fields)
                except ValueError:
                    return False
                if a * x + b * y != c:
                    return False
        return True
    raise ValueError(f"unknown checker: {checker}")


def short(text: str, limit: int = 500) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...<truncated>"


def run_case(command: list[str], case: Case, timeout: float, checker: str) -> tuple[bool, str]:
    input_data = case.input_path.read_text(encoding="utf-8")
    expected = case.output_path.read_text(encoding="utf-8")
    try:
        result = subprocess.run(
            command,
            input=input_data,
            text=True,
            capture_output=True,
            timeout=timeout,
            cwd=ROOT,
        )
    except subprocess.TimeoutExpired:
        return False, f"{case.name}: time limit exceeded after {timeout:.2f}s"

    if result.returncode != 0:
        return (
            False,
            f"{case.name}: runtime error {result.returncode}\n"
            f"stderr:\n{short(result.stderr)}",
        )

    if not outputs_match(result.stdout, expected, checker, input_data):
        return (
            False,
            f"{case.name}: wrong answer\n"
            f"expected:\n{short(expected)}\n"
            f"actual:\n{short(result.stdout)}",
        )

    return True, f"{case.name}: ok"


def judge(problem: Path, lang: str, target: str, random_count: int, seed: int, verbose: bool) -> int:
    problem = problem.resolve()
    manifest = load_manifest(problem)
    checker = manifest.get("checker", "tokens")
    timeout = float(manifest.get("time_limit_seconds", 2.0))
    title = manifest.get("title", problem.name)

    source = source_for(problem, lang, target)
    cases = discover_fixed_cases(problem) + generate_random_cases(problem, random_count, seed)
    if not cases:
        print(f"{problem}: no tests found")
        return 1

    try:
        command = command_for(source, lang)
    except subprocess.CalledProcessError as exc:
        print(f"{title} [{lang}]: compilation failed with exit code {exc.returncode}")
        return exc.returncode or 1

    print(f"{title} [{lang}, {target}]: {len(cases)} case(s)")
    for case in cases:
        ok, message = run_case(command, case, timeout, checker)
        if verbose or not ok:
            print(message)
        if not ok:
            return 1

    print("accepted")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem", type=Path)
    parser.add_argument("--lang", choices=["cpp", "py"], required=True)
    parser.add_argument(
        "--target",
        choices=["student", "solution"],
        default=os.environ.get("CP_TARGET", "student"),
    )
    parser.add_argument("--random-count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    try:
        return judge(
            args.problem,
            args.lang,
            args.target,
            args.random_count,
            args.seed,
            args.verbose,
        )
    finally:
        for path in TEMP_DIRS:
            if path.is_dir():
                shutil.rmtree(path, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
