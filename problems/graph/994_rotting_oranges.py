"""
LeetCode Problem: 994 - Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium

Problem Description:
You are given an m x n grid where each cell can have one of three values:
* 0 representing an empty cell,
* 1 representing a fresh orange, or
* 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Examples:
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 10
* grid[i][j] is 0, 1, or 2.
"""
import pytest
from typing import List
from collections import deque  # Useful for BFS

# Solution Class - Implement the logic here
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum time for all fresh oranges to rot.

        Approach:
        # 1. Initialize queue, count fresh oranges, find initial rotten oranges.
        # 2. Perform BFS, keeping track of minutes/levels.
        # 3. In BFS, rot adjacent fresh oranges and add them to the queue.
        # 4. After BFS, check if any fresh oranges remain.

        Time Complexity: O(M*N)
        Space Complexity: O(M*N)

        Args:
            grid: A 2D list representing the grid of oranges.

        Returns:
            int: The minimum minutes, or -1 if impossible.
        """
        # --- Implement your solution here ---

        # initalize the dimension
        rows = len(grid)
        columns = len(grid[0])

        # find the rotten oranges, number of fresh oranges, number of empty cell
        queue = deque([])
        fresh = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if not fresh:
            return 0

        # initialize the time
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        # simulate the timestep
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in directions:
                    r1, c1 = r + d[0], c + d[1]
                    if 0 <= r1 < rows and 0 <= c1 < columns and grid[r1][c1] == 1:
                        fresh -= 1
                        if fresh == 0:
                            return minutes
                        grid[r1][c1] = 2
                        queue.append((r1, c1))

        return -1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_grid, expected_minutes)
test_data = [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
    ([[0]], 0),
    ([[1]], -1),
    ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 2]], 4),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("grid, expected", test_data)
def test_solution(grid, expected):
    # Need deep copy if the solution modifies the grid
    import copy

    grid_copy = copy.deepcopy(grid)
    solution = Solution()
    result = solution.orangesRotting(grid_copy)
    assert result == expected


# You can add more specific test functions if needed
