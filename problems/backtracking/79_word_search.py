"""
LeetCode Problem: 79 - Word Search
Link: https://leetcode.com/problems/word-search/
Difficulty: Medium

Problem Description:
Given an m x n grid of characters `board` and a string `word`, return true if `word`
exists in the grid. The word can be formed from sequentially adjacent cells (horizontally
or vertically). The same cell cannot be used more than once in the word.

Examples: See LeetCode page.

Constraints: See LeetCode page.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, k):
            # 1. Check if current cell is valid for word[k]
            #    - Check boundaries
            #    - Check if cell matches word[k]
            #    - Check if cell has already been visited (marked with '#')
            if not (0 <= r < height and 0 <= c < width and board[r][c] == word[k]):
                return False

            # 2. Base Case: Found the entire word
            if k == len(word) - 1:
                return True

            # 3. Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"  # Use a special character for clarity

            # 4. Explore neighbors for the next character (word[k+1])
            found = False
            for dr, dc in directions:
                target_r, target_c = r + dr, c + dc
                # Recursively call for the next character index (k+1)
                if dfs(target_r, target_c, k + 1):
                    found = True
                    break  # Found the word, no need to explore other neighbors

            # 5. Backtrack: Unmark current cell
            board[r][c] = temp

            return found

        # Iterate through each cell as a potential starting point
        for i in range(height):
            for j in range(width):
                # Start DFS if the first character matches
                if dfs(i, j, 0):
                    return True

        return False


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_board, input_word, expected_output)
test_data = [
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED",
        True,
    ),  # Example 1
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "SEE",
        True,
    ),  # Example 2
    (
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCB",
        False,
    ),  # Example 3
    ([["a"]], "a", True),
    ([["a", "b"], ["c", "d"]], "abcd", False),  # Not adjacent
    ([["a", "a"]], "aaa", False),  # Cannot reuse cell
    (
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        "ABCESEEEFS",
        True,
    ),  # Longer path
]


@pytest.mark.parametrize("board_input, word_input, expected", test_data)
def test_solution(board_input, word_input, expected):
    solution = Solution()
    # Create a deep copy if the solution modifies the board (e.g., marking visited)
    import copy

    board_copy = copy.deepcopy(board_input)
    result = solution.exist(board_copy, word_input)
    assert result == expected
