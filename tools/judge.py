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

Personal submissions may live in a mirrored directory outside the public
course tree. Set CP_SUBMISSIONS_DIR to that directory, or use the default
local `.submissions/` directory when it exists.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import shlex
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


def submissions_root() -> Path | None:
    """Return the configured personal-submissions root, if one is active."""

    configured = os.environ.get("CP_SUBMISSIONS_DIR")
    if configured:
        root = Path(configured).expanduser()
        if not root.is_absolute():
            root = ROOT / root
        return root.resolve()

    local = ROOT / ".submissions"
    return local.resolve() if local.is_dir() else None


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
    if target == "student":
        overlay = submissions_root()
        if overlay is not None:
            try:
                relative_problem = problem.resolve().relative_to(ROOT)
            except ValueError:
                pass
            else:
                personal_source = overlay / relative_problem / name
                if personal_source.is_file():
                    source = personal_source
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


def compile_cpp(source: Path, debug: bool = False) -> Path:
    build_dir = Path(tempfile.mkdtemp(prefix="cp-course-cpp-"))
    TEMP_DIRS.append(build_dir)
    binary = build_dir / "main"
    flags = (
        [
            "-Og",
            "-g3",
            "-fno-omit-frame-pointer",
            "-D_GLIBCXX_DEBUG",
            "-D_GLIBCXX_ASSERTIONS",
        ]
        if debug
        else ["-O2", "-pipe"]
    )
    cmd = ["g++", "-std=c++23", *flags, "-Wall", "-Wextra",
           str(source), "-o", str(binary)]
    subprocess.run(cmd, cwd=ROOT, check=True)
    return binary


def command_for(source: Path, lang: str) -> list[str]:
    if lang == "py":
        return [sys.executable, str(source)]
    if lang == "cpp":
        return [str(compile_cpp(source))]
    raise ValueError(f"unknown language: {lang}")


def resolve_debug_input(
    problem: Path,
    cases: list[Case],
    selector: str,
) -> Path:
    """Resolve a fixed/random case name or an explicit input-file path."""

    explicit = Path(selector)
    if explicit.is_file():
        return explicit.resolve()

    test_candidate = problem / "tests" / selector
    if test_candidate.suffix != ".in":
        test_candidate = test_candidate.with_suffix(".in")
    if test_candidate.is_file():
        return test_candidate.resolve()

    normalized = selector.removesuffix(".in")
    matches = [
        case.input_path
        for case in cases
        if case.name == normalized or case.input_path.stem == normalized
    ]
    if len(matches) == 1:
        return matches[0].resolve()
    if len(matches) > 1:
        names = ", ".join(str(path) for path in matches)
        raise ValueError(f"ambiguous debug case {selector!r}: {names}")

    available = ", ".join(case.name for case in cases)
    raise ValueError(
        f"unknown debug case {selector!r}; available cases: {available}"
    )


def debug_cpp(
    problem: Path,
    target: str,
    random_count: int,
    seed: int,
    case_selector: str,
    stop_at_main: bool,
) -> int:
    """Compile a C++ submission with debug symbols and open it in GDB."""

    if shutil.which("gdb") is None:
        print("gdb was not found; install it before using --gdb", file=sys.stderr)
        return 1

    problem = problem.resolve()
    source = source_for(problem, "cpp", target)
    cases = discover_fixed_cases(problem)
    try:
        input_path = resolve_debug_input(problem, cases, case_selector)
    except ValueError:
        # Fixed cases and explicit paths do not need the random generator.
        cases += generate_random_cases(problem, random_count, seed)
        input_path = resolve_debug_input(problem, cases, case_selector)

    try:
        binary = compile_cpp(source, debug=True)
    except subprocess.CalledProcessError as exc:
        print(
            f"Debug compilation failed with exit code {exc.returncode}",
            file=sys.stderr,
        )
        return exc.returncode or 1

    command = [
        "gdb",
        "--quiet",
        str(binary),
        "-ex",
        "set pagination off",
        "-ex",
        "set print pretty on",
    ]
    if stop_at_main:
        command.extend(["-ex", "break main"])
    command.extend(["-ex", f"run < {shlex.quote(str(input_path))}"])

    print(f"Debug source: {source}")
    print(f"Input case:   {input_path}")
    if stop_at_main:
        print("Stopped at main. Useful commands: next, step, print, display, continue.")
    else:
        print("Running until exit or failure. At a crash, use: bt, frame, list, print.")
    return subprocess.run(command, cwd=ROOT).returncode


def normalize_tokens(text: str) -> list[str]:
    return text.split()


def outputs_match(actual: str, expected: str, checker: str, input_data: str) -> bool:
    if checker == "exact":
        return actual.rstrip("\n") == expected.rstrip("\n")
    if checker == "tokens":
        return normalize_tokens(actual) == normalize_tokens(expected)
    if checker == "float":
        actual_tokens = normalize_tokens(actual)
        expected_tokens = normalize_tokens(expected)
        if len(actual_tokens) != len(expected_tokens):
            return False
        try:
            pairs = zip(map(float, actual_tokens), map(float, expected_tokens))
            return all(
                math.isfinite(got)
                and math.isfinite(want)
                and abs(got - want) <= 1e-7 + 1e-7 * abs(want)
                for got, want in pairs
            )
        except ValueError:
            return False
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
    if checker == "ticket_split":
        values = list(map(int, input_data.split()))
        if not values:
            return not actual.split()
        queries = values[0]
        lines = actual.splitlines()
        if len(lines) != queries:
            return False
        index = 1
        for line in lines:
            n, total, cost_a, cost_b, cost_c = values[index:index + 5]
            index += 5
            fields = line.split()
            possible = False
            for x in range(n + 1):
                for y in range(n - x + 1):
                    z = n - x - y
                    if cost_a * x + cost_b * y + cost_c * z == total:
                        possible = True
                        break
                if possible:
                    break
            if fields == ["-1"]:
                if possible:
                    return False
                continue
            if len(fields) != 3:
                return False
            try:
                x, y, z = map(int, fields)
            except ValueError:
                return False
            if (
                x < 0
                or y < 0
                or z < 0
                or x + y + z != n
                or cost_a * x + cost_b * y + cost_c * z != total
            ):
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
        stderr = result.stderr.rstrip()
        if not stderr:
            stderr = "<no stderr output>"
        return (
            False,
            f"{case.name}: runtime error {result.returncode}\n"
            f"stderr:\n{stderr}",
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

    location = ""
    if target == "student" and source.parent != problem:
        location = ", personal overlay"
    print(f"{title} [{lang}, {target}{location}]: {len(cases)} case(s)")
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
    parser.add_argument(
        "--gdb",
        action="store_true",
        help="compile C++ with debug symbols and open the selected case in GDB",
    )
    parser.add_argument(
        "--case",
        metavar="NAME_OR_PATH",
        help="case name reported by the judge, or a path to an input file",
    )
    parser.add_argument(
        "--step",
        action="store_true",
        help="with --gdb, stop at main instead of immediately running to failure",
    )
    args = parser.parse_args(argv)

    if args.gdb and args.lang != "cpp":
        parser.error("--gdb requires --lang cpp")
    if args.gdb and not args.case:
        parser.error("--gdb requires --case NAME_OR_PATH")
    if args.step and not args.gdb:
        parser.error("--step requires --gdb")

    try:
        try:
            if args.gdb:
                return debug_cpp(
                    args.problem,
                    args.target,
                    args.random_count,
                    args.seed,
                    args.case,
                    args.step,
                )
            return judge(
                args.problem,
                args.lang,
                args.target,
                args.random_count,
                args.seed,
                args.verbose,
            )
        except (FileNotFoundError, ValueError) as exc:
            parser.error(str(exc))
    finally:
        for path in TEMP_DIRS:
            if path.is_dir():
                shutil.rmtree(path, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
