"""
Script to create GitHub issues for all 75 LeetCode 75 problems.

Usage:
    python scripts/create_issues.py

Requires:
    - GITHUB_TOKEN environment variable set with repo scope
    - GITHUB_REPOSITORY environment variable (e.g., "cd155/leetcode-75-python-template")
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error


def extract_problems(src_dir="src"):
    """Extract problem details from all solution files."""
    problems = []

    for category in sorted(os.listdir(src_dir)):
        cat_path = os.path.join(src_dir, category)
        if not os.path.isdir(cat_path) or category.startswith("_"):
            continue
        for filename in sorted(os.listdir(cat_path)):
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(cat_path, filename)
                with open(filepath, "r") as f:
                    content = f.read()

                match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                if not match:
                    continue

                docstring = match.group(1).strip()
                lines = docstring.split("\n")
                title_match = re.match(r"LeetCode\s+(\d+):\s+(.*)", lines[0])
                if not title_match:
                    continue

                lc_num = int(title_match.group(1))
                title = title_match.group(2).strip()
                description = "\n".join(lines[1:]).strip()

                problems.append(
                    {
                        "number": lc_num,
                        "title": title,
                        "category": category,
                        "filename": filename,
                        "filepath": filepath,
                        "description": description,
                    }
                )

    problems.sort(key=lambda x: x["number"])
    return problems


CATEGORY_DISPLAY_NAMES = {
    "array_string": "Array / String",
    "two_pointers": "Two Pointers",
    "sliding_window": "Sliding Window",
    "prefix_sum": "Prefix Sum",
    "hash_map_set": "Hash Map / Set",
    "stack": "Stack",
    "queue": "Queue",
    "linked_list": "Linked List",
    "binary_tree_dfs": "Binary Tree - DFS",
    "binary_tree_bfs": "Binary Tree - BFS",
    "binary_search_tree": "Binary Search Tree",
    "graphs_dfs": "Graphs - DFS",
    "graphs_bfs": "Graphs - BFS",
    "heap_priority_queue": "Heap / Priority Queue",
    "binary_search": "Binary Search",
    "backtracking": "Backtracking",
    "dp_1d": "DP - 1D",
    "dp_multidimensional": "DP - Multidimensional",
    "bit_manipulation": "Bit Manipulation",
    "trie": "Trie",
    "intervals": "Intervals",
    "monotonic_stack": "Monotonic Stack",
}


def get_category_display(category):
    """Get the human-readable LeetCode 75 category name for a src/ directory."""
    return CATEGORY_DISPLAY_NAMES.get(category, category.replace("_", " ").title())


LEETCODE_SLUG_OVERRIDES = {
    "maximum_number_of_vowels_in_a_given_substring.py": "maximum-number-of-vowels-in-a-substring-of-given-length",
    "reorder_routes_to_make_all_paths_lead_to_city_zero.py": "reorder-routes-to-make-all-paths-lead-to-the-city-zero",
    "nth_tribonacci_number.py": "n-th-tribonacci-number",
}


def get_leetcode_slug(filename):
    """Get the LeetCode problem URL slug from the filename."""
    if filename in LEETCODE_SLUG_OVERRIDES:
        return LEETCODE_SLUG_OVERRIDES[filename]
    return filename.replace(".py", "").replace("_", "-")


def build_issue_body(problem):
    """Build the issue body markdown for a problem."""
    category_display = get_category_display(problem["category"])
    filepath = problem["filepath"]
    slug = get_leetcode_slug(problem["filename"])

    body = f"""## LeetCode {problem['number']}: {problem['title']}

**Category:** {category_display}
**Difficulty:** See [LeetCode](https://leetcode.com/problems/{slug}/)
**Solution File:** `{filepath}`
**Test File:** `tests/test_{problem['filename']}`

### Problem Description

{problem['description']}

### Tasks

- [ ] Implement the solution in `{filepath}`
- [ ] Ensure all test cases pass
- [ ] Analyze time complexity
- [ ] Analyze space complexity
"""
    return body


def create_github_issue(token, repo, title, body, labels):
    """Create a GitHub issue using the REST API."""
    url = f"https://api.github.com/repos/{repo}/issues"
    data = json.dumps({"title": title, "body": body, "labels": labels}).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["number"], result["html_url"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  Error creating issue: {e.code} - {error_body}")
        return None, None


def ensure_labels_exist(token, repo, labels):
    """Ensure all required labels exist in the repository."""
    label_colors = {
        "array string": "7057ff",
        "two pointers": "008672",
        "sliding window": "d73a4a",
        "prefix sum": "5319e7",
        "hash map set": "fef2c0",
        "stack": "0075ca",
        "queue": "c5def5",
        "linked list": "e4e669",
        "binary tree dfs": "0e8a16",
        "binary tree bfs": "bfdadc",
        "binary search tree": "d4c5f9",
        "graphs dfs": "1d76db",
        "graphs bfs": "0052cc",
        "heap priority queue": "a2eeef",
        "binary search": "cfd3d7",
        "backtracking": "d876e3",
        "dp 1d": "b60205",
        "dp multidimensional": "e99695",
        "bit manipulation": "006b75",
        "trie": "f9d0c4",
        "intervals": "bfd4f2",
        "monotonic stack": "c2e0c6",
        "leetcode-75": "fbca04",
    }

    for label, color in label_colors.items():
        if label not in labels:
            continue
        url = f"https://api.github.com/repos/{repo}/labels"
        data = json.dumps(
            {
                "name": label,
                "color": color,
                "description": f"LeetCode 75 - {get_category_display(label.replace(' ', '_'))} problems",
            }
        ).encode("utf-8")

        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            urllib.request.urlopen(req)
            print(f"  Created label: {label}")
        except urllib.error.HTTPError as e:
            if e.code == 422:
                pass  # Label already exists
            else:
                print(f"  Warning: Could not create label '{label}': {e.code}")


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token:
        print("Error: GITHUB_TOKEN environment variable is required")
        sys.exit(1)
    if not repo:
        print("Error: GITHUB_REPOSITORY environment variable is required")
        sys.exit(1)

    print(f"Repository: {repo}")
    print("Extracting problems from source files...")

    problems = extract_problems()
    print(f"Found {len(problems)} problems\n")

    if len(problems) != 75:
        print(f"Error: Expected 75 problems, found {len(problems)}")
        sys.exit(1)

    # Collect all unique labels
    all_labels = {"leetcode-75"}
    for p in problems:
        all_labels.add(p["category"].replace("_", " "))

    print("Ensuring labels exist...")
    ensure_labels_exist(token, repo, all_labels)
    print()

    # Create issues
    created = 0
    for i, problem in enumerate(problems, 1):
        category_label = problem["category"].replace("_", " ")
        title = f"LeetCode {problem['number']}: {problem['title']}"
        body = build_issue_body(problem)
        labels = ["leetcode-75", category_label]

        print(f"[{i}/75] Creating issue: {title}")
        issue_num, issue_url = create_github_issue(token, repo, title, body, labels)

        if issue_num:
            print(f"  Created: #{issue_num} - {issue_url}")
            created += 1
        else:
            print(f"  Failed to create issue")

        # Rate limiting - GitHub allows 30 requests per minute for issue creation
        if i % 25 == 0:
            print("  Pausing for rate limiting...")
            time.sleep(10)
        else:
            time.sleep(1)

    print(f"\nDone! Created {created}/75 issues.")


if __name__ == "__main__":
    main()
