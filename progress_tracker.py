"""
LeetCode progress tracker script
Updates the README.md with current progress stats
"""

import os
import re
from collections import defaultdict


def update_progress():
    """Scan problem directories and update README with progress statistics"""
    categories = [
        "array",
        "binary_search",
        "dynamic_programming",
        "graph",
        "linked_list",
        "string",
        "tree",
    ]
    difficulties = ["Easy", "Medium", "Hard"]

    # Initialize counters
    stats = {
        category: {difficulty: 0 for difficulty in difficulties}
        for category in categories
    }
    total_by_difficulty = {difficulty: 0 for difficulty in difficulties}

    # Scan problem directories
    problems_dir = "problems"
    for category in categories:
        category_dir = os.path.join(problems_dir, category)
        if not os.path.exists(category_dir):
            continue

        for filename in os.listdir(category_dir):
            if not filename.endswith(".py"):
                continue

            file_path = os.path.join(category_dir, filename)
            difficulty = extract_difficulty(file_path)

            if difficulty in difficulties:
                stats[category][difficulty] += 1
                total_by_difficulty[difficulty] += 1

    # Calculate totals by category
    category_totals = {
        category: sum(stats[category].values()) for category in categories
    }
    grand_total = sum(category_totals.values())

    # Update README.md
    update_readme(stats, category_totals, total_by_difficulty, grand_total)

    print(f"Progress updated: {grand_total} total problems solved")


def extract_difficulty(file_path):
    """Extract problem difficulty from file content"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            match = re.search(r"Difficulty:\s*(Easy|Medium|Hard)", content)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return None


def update_readme(stats, category_totals, total_by_difficulty, grand_total):
    """Update the README.md file with progress statistics"""
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()

        # Find the progress tracking table
        table_pattern = r"## Progress Tracking\s*\n\s*\|\s*Category\s*\|.*?\|\s*\*\*Total\*\*\s*\|\s*\*\*\d+\*\*\s*\|\s*\*\*\d+\*\*\s*\|\s*\*\*\d+\*\*\s*\|\s*\*\*\d+\*\*\s*\|"
        table_match = re.search(table_pattern, content, re.DOTALL)

        if not table_match:
            print("Progress tracking table not found in README.md")
            return

        # Create new table
        new_table = "## Progress Tracking\n\n"
        new_table += "| Category | Easy | Medium | Hard | Total |\n"
        new_table += "|----------|------|--------|------|-------|\n"

        categories = [
            "array",
            "binary_search",
            "dynamic_programming",
            "graph",
            "linked_list",
            "string",
            "tree",
        ]

        for category in categories:
            category_name = category.replace("_", " ").title()
            easy = stats[category]["Easy"]
            medium = stats[category]["Medium"]
            hard = stats[category]["Hard"]
            total = category_totals[category]

            new_table += f"| {category_name} | {easy} | {medium} | {hard} | {total} |\n"

        # Add totals row
        new_table += f"| **Total** | **{total_by_difficulty['Easy']}** | **{total_by_difficulty['Medium']}** | **{total_by_difficulty['Hard']}** | **{grand_total}** |"

        # Replace old table with new table
        updated_content = (
            content[: table_match.start()] + new_table + content[table_match.end() :]
        )

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)

    except Exception as e:
        print(f"Error updating README.md: {e}")


if __name__ == "__main__":
    update_progress()
