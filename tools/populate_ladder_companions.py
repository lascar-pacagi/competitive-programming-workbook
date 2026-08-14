#!/usr/bin/env python3
"""Populate the offline companion packages for Sections 61 and 62.

The linked Kattis and Codeforces problems are external judge problems.  This
script deliberately copies original course exercises instead of copying those
statements.  It gives every ladder rung a local, runnable exercise with the
same package contract: neutral skeletons, two reference implementations, and
deterministic plus randomized tests.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# (destination directory name, source package relative to repository root,
#  external task title and URL)
ICPC = [
    ("01_acm_contest_scoring", "sections/61_icpc_contest_readiness/problems/a_scoreboard_replay", "ACM Contest Scoring", "https://open.kattis.com/problems/acm"),
    ("02_booking_a_room", "sections/14_core_patterns_mixed_contest/problems/d_first_free_slot", "Booking a Room", "https://open.kattis.com/problems/bookingaroom"),
    ("03_sort_of_sorting", "sections/05_sorting_as_tool/problems/d_compact_team", "Sort of Sorting", "https://open.kattis.com/problems/sortofsorting"),
    ("04_icpc_team_selection", "sections/09_greedy_exchange/problems/d_workshop_badges", "ICPC Team Selection", "https://open.kattis.com/problems/icpcteamselection"),
    ("05_guess_data_structure", "sections/12_stacks_queues_deques/problems/d_bounded_spread_subarrays", "Guess the Data Structure", "https://open.kattis.com/problems/guessthedatastructure"),
    ("06_assigning_workstations", "sections/39_heaps_priority_queues/problems/d_merge_costs", "Assigning Workstations", "https://open.kattis.com/problems/workstations"),
    ("07_teque", "sections/40_data_structures_mixed_contest/problems/d_salary_queries", "Teque", "https://open.kattis.com/problems/teque"),
    ("08_almost_union_find", "sections/18_dsu_minimum_spanning_trees/problems/d_cable_savings", "Almost Union-Find", "https://open.kattis.com/problems/almostunionfind"),
    ("09_single_source_shortest_path", "sections/19_dijkstra_weighted_modeling/problems/d_even_hop_route", "Single Source Shortest Path", "https://open.kattis.com/problems/shortestpath1"),
    ("10_get_shorty", "sections/20_zero_one_bfs_variants/problems/d_letter_portals", "Get Shorty", "https://open.kattis.com/problems/getshorty"),
    ("11_coast_length", "sections/15_bfs_unweighted_shortest_paths/problems/d_nearest_station", "Coast Length", "https://open.kattis.com/problems/coast"),
    ("12_all_pairs_shortest_path", "sections/21_graphs_i_mixed_contest/problems/d_reliable_link", "All Pairs Shortest Path", "https://open.kattis.com/problems/allpairspath"),
    ("13_arbitrage", "sections/29_modular_arithmetic/problems/d_nested_power_queries", "Arbitrage", "https://open.kattis.com/problems/arbitrage"),
    ("14_knapsack", "sections/23_knapsack_subset_dp/problems/d_balanced_split", "Knapsack", "https://open.kattis.com/problems/knapsack"),
    ("15_clock_pictures", "sections/43_string_algorithms_i/problems/d_prefix_frequency", "Clock Pictures", "https://open.kattis.com/problems/clockpictures"),
    ("16_string_matching", "sections/44_string_algorithms_ii/problems/d_unique_prefix_lengths", "String Matching", "https://open.kattis.com/problems/stringmatching"),
    ("17_max_flow", "sections/45_flows_and_matchings/problems/d_project_selection", "Max Flow", "https://open.kattis.com/problems/maxflow"),
    ("18_min_cut", "sections/45_flows_and_matchings/problems/d_project_selection", "Min Cut", "https://open.kattis.com/problems/mincut"),
    ("19_distributing_ballot_boxes", "sections/08_binary_search_answer/problems/d_factory_deadline", "Distributing Ballot Boxes", "https://open.kattis.com/problems/distributingballotboxes"),
    ("20_catering", "sections/60_final_capstone/problems/d_coupon_route", "Catering", "https://open.kattis.com/problems/catering"),
]

CF_NAMES = [
    "01_way_too_long_words", "02_registration_system", "03_fence", "04_books", "05_taxi",
    "06_interesting_drink", "07_two_buttons", "08_boredom", "09_beautiful_numbers", "10_polygons",
    "11_dijkstra_path", "12_distance_in_tree", "13_kefa_and_dishes", "14_power_grid", "15_good_substrings",
    "16_enemy_is_weak", "17_powerful_array", "18_array_and_operations", "19_kalila_and_dimna", "20_legacy",
    "21_fools_and_roads", "22_blood_cousins", "23_tree_and_queries", "24_lomsat_gelral", "25_danil_part_time_job",
    "26_xor_on_segment", "27_time_to_raid_cowavans", "28_one_occurrence", "29_torcoder", "30_water_tree",
    "31_rotate_columns", "32_xor_inverse", "33_holes", "34_xenia_and_tree", "35_square_subsets",
    "36_yet_another_minimization", "37_xenons_attack", "38_kingdom_cities", "39_nearest_leaf", "40_duff_in_the_army",
    "41_till_i_collapse", "42_multidimensional_queries", "43_ciel_and_gondolas", "44_willem_chtholly", "45_bakery",
    "46_cats_transport", "47_beautiful_numbers_divisibility", "48_destiny", "49_mass_change_queries", "50_ivan_and_burgers",
]


def course_source(number: int) -> str:
    prefix = f"sections/{number:02d}_"
    section = next(ROOT.glob(prefix + "*"))
    package = next((section / "problems").glob("d_*"))
    return str(package.relative_to(ROOT))


def copy_package(destination: Path, source: Path, title: str, url: str) -> None:
    if not destination.exists():
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        readme = destination / "README.md"
        original = readme.read_text()
        preface = (
            f"# Offline companion: {title}\n\n"
            f"This is an original, locally judgeable companion for [{title}]({url}). "
            "It is **not** a copied contest statement. Solve this package offline "
            "to practise the course technique, then solve the linked official task "
            "on its judge.\n\n"
        )
        # The source exercise remains the complete local contract below the
        # provenance note. Remove its old H1 to keep the package title unambiguous.
        if original.startswith("# "):
            original = original.split("\n", 1)[1]
        readme.write_text(preface + original)

        manifest = destination / "manifest.json"
        payload = json.loads(manifest.read_text())
        payload["title"] = f"Offline companion: {title}"
        manifest.write_text(json.dumps(payload, indent=2) + "\n")

    # Source sections can contain a learner's partial attempt. A companion
    # must start blind, so it always receives the standard neutral skeleton.
    (destination / "solve.cpp").write_text(
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n\n"
        "int main() {\n"
        "    ios::sync_with_stdio(false);\n"
        "    cin.tie(nullptr);\n\n"
        "    // TODO: implement your solution.\n"
        "    return 0;\n"
        "}\n"
    )
    (destination / "solve.py").write_text(
        "import sys\n\n\n"
        "def main() -> None:\n"
        "    # TODO: implement your solution.\n"
        "    data = sys.stdin.buffer.read().split()\n"
        "    if not data:\n"
        "        return\n"
        "    raise NotImplementedError(\"solve.py is for your solution\")\n\n\n"
        "if __name__ == \"__main__\":\n"
        "    main()\n"
    )


def write_index(section: Path, tasks: list[tuple[str, str, str, str]]) -> None:
    lines = [
        "# Offline Companion Index",
        "",
        "Every package below is an original course exercise. It has a neutral "
        "C++/Python skeleton, C++/Python reference solution, fixed tests, and "
        "a randomized test generator. The external link is the corresponding "
        "submission target; the local exercise is intentionally not a copied "
        "statement.",
        "",
        "| # | External task | Local companion |",
        "|---:|---|---|",
    ]
    for index, (slug, _source, title, url) in enumerate(tasks, 1):
        lines.append(f"| {index} | [{title}]({url}) | [package](problems/{slug}/README.md) |")
    (section / "OFFLINE_COMPANIONS.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    icpc_section = ROOT / "sections/61_icpc_contest_readiness"
    icpc_tasks = ICPC
    for slug, source, title, url in icpc_tasks:
        copy_package(icpc_section / "problems" / slug, ROOT / source, title, url)
    write_index(icpc_section, icpc_tasks)

    cf_section = ROOT / "sections/62_codeforces_course_ladder"
    sheet = (cf_section / "problem_sheet.qmd").read_text()
    urls = re.findall(r"Official: <(https://codeforces\.com/problemset/problem/[^>]+)>", sheet)
    headings = re.findall(r"^## \d+\. (.+)$", sheet, flags=re.MULTILINE)
    if len(urls) != 50 or len(headings) != 50:
        raise RuntimeError("Section 62 sheet must contain exactly 50 official task headings and URLs")
    cf_tasks = []
    for number, slug in enumerate(CF_NAMES, 1):
        source = course_source(number)
        title = headings[number - 1]
        url = urls[number - 1]
        cf_tasks.append((slug, source, title, url))
        copy_package(cf_section / "problems" / slug, ROOT / source, title, url)
    write_index(cf_section, cf_tasks)


if __name__ == "__main__":
    main()
