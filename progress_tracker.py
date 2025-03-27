"""
LeetCode progress tracker script
Updates the README.md with current progress stats
"""

import os
import re
from collections import defaultdict
from datetime import date
import pandas as pd  # Using pandas can simplify CSV/Markdown table parsing/writing


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

    log_file = "REVIEW_LOG.md"
    existing_problems_in_log = get_existing_log_problems(log_file)

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
            problem_name = parse_problem_filename(filename)  # Get a canonical name

            # Update summary stats (as before)
            if difficulty in difficulties:
                stats[category][difficulty] += 1
                total_by_difficulty[difficulty] += 1

            # Check if problem needs to be added to the detailed log
            if problem_name not in existing_problems_in_log:
                category_name = category.replace("_", " ").title()
                problem_details = {
                    "name": problem_name,
                    "category_name": category_name,
                    "difficulty": difficulty
                    or "N/A",  # Handle if difficulty wasn't parsed
                    "file_path": file_path,
                }
                append_to_log(log_file, problem_details)
                # Add to set immediately to prevent duplicates if script runs twice before commit
                existing_problems_in_log.add(problem_name)

    # Calculate totals by category
    category_totals = {
        category: sum(stats[category].values()) for category in categories
    }
    grand_total = sum(category_totals.values())

    # Update README.md summary table (rename your original update_readme function)
    update_readme_summary_table(
        stats, category_totals, total_by_difficulty, grand_total
    )

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


def update_readme_summary_table(
    stats, category_totals, total_by_difficulty, grand_total
):
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


def get_existing_log_problems(log_file="REVIEW_LOG.md"):
    # Simplified: assumes markdown table, needs robust parsing
    # Using pandas read_markdown might be better if format is consistent
    # Or use regex to find lines starting with '|' and extract first column
    problems = set()
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                if (
                    line.startswith("|")
                    and not line.startswith("|--")
                    and not line.startswith("| Category")
                ):
                    # Very basic parsing - assumes ' | ' delimiter
                    parts = line.split("|")
                    if len(parts) > 1:
                        problem_name = parts[1].strip()
                        # Extract number/title if needed more precisely
                        if problem_name:
                            problems.add(problem_name)  # Or add a canonical ID
    except FileNotFoundError:
        pass  # Log file doesn't exist yet
    return problems


def parse_problem_filename(filename):
    # Basic parsing, adapt as needed
    match = re.match(r"(\d+)_?(.*)\.py", filename)
    if match:
        num = match.group(1)
        # Convert snake_case to Title Case for title
        title = match.group(2).replace("_", " ").title()
        return f"{num}. {title}"  # Or return num/title separately
    return filename.replace(".py", "")


def append_to_log(log_file, problem_details):
    today = date.today().isoformat()
    # Format a new markdown table row
    # Ensure consistent column order with your log file!
    new_row = f"| {problem_details['name']} | {problem_details['category_name']} | {problem_details['difficulty']} | {today} | {today} | |"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            # Ensure header exists if file is new/empty
            if os.path.getsize(log_file) == 0:
                f.write("# REVIEW_LOG.md\n\n## Problem Review Status\n\n")
                f.write(
                    "| Problem | Category | Difficulty | Date Solved | Last Reviewed | Notes / Confidence |\n"
                )
                f.write(
                    "|---------|----------|------------|-------------|---------------|--------------------|\n"
                )
            f.write(new_row + "\n")
        print(f"Added '{problem_details['name']}' to {log_file}")
    except Exception as e:
        print(f"Error appending to {log_file}: {e}")


if __name__ == "__main__":
    update_progress()
