"""
LeetCode Problem: 695 - Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/
Difficulty: Medium

Problem Description:
Given an m x n binary grid, find the maximum area of an island (a group of connected 1s).
An island is connected 4-directionally. If no island exists, return 0.

Examples: See LeetCode page.

Constraints: See LeetCode page.
"""

import pytest
from typing import List
from collections import deque


# Solution Class - Implement the logic here
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Approach: Grid Traversal (DFS or BFS)
        [Explain your approach here - How do you find islands and calculate their area?]

        Time Complexity: O(M * N) - Visit each cell at most once.
        Space Complexity: O(M * N) - Worst case for recursion stack (DFS) or queue (BFS).

        Args:
            grid (List[List[int]]): The grid representing islands (1) and water (0).

        Returns:
            int: The maximum area found among all islands.
        """
        # Your solution here
        height = len(grid)
        width = len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(height):
            for column in range(width):
                if grid[row][column] == 1:
                    queue = deque([(row, column)])
                    grid[row][column] = 2
                    cur_area = 1
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        for dr, dc in directions:
                            target_r, target_c = cur_r + dr, cur_c + dc
                            if (
                                0 <= target_r < height
                                and 0 <= target_c < width
                                and grid[target_r][target_c] == 1
                            ):
                                grid[target_r][target_c] = 2
                                cur_area += 1
                                queue.append((target_r, target_c))
                    max_area = max(cur_area, max_area)
        return max_area


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_grid, expected_max_area)
test_data = [
    (
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        6,
    ),  # Example 1
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),  # Example 2
    ([[1]], 1),
    ([[1, 1], [1, 0]], 3),
    ([[1, 0, 1], [1, 1, 1], [0, 0, 1]], 6),
    ([[0, 1], [1, 1]], 3),
    ([[0]], 0),
    ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 4),
]


@pytest.mark.parametrize("grid_input, expected", test_data)
def test_solution(grid_input, expected):
    solution = Solution()
    # Create a deep copy to avoid modifying the original test case grid
    # if the solution modifies the grid in place (which is common).
    import copy

    grid_copy = copy.deepcopy(grid_input)
    result = solution.maxAreaOfIsland(grid_copy)
    assert result == expected
