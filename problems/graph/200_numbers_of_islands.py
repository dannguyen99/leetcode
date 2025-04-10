"""
LeetCode Problem: 200 - Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium

Problem Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 300
* grid[i][j] is '0' or '1'.
"""
import pytest
from typing import List
from collections import deque  # Useful for BFS

# Solution Class - Implement the logic here
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a grid.

        Approach:
        [Explain your approach here - e.g., Iterate grid, use BFS/DFS for connected components, mark visited]

        Time Complexity: O(M*N)
        Space Complexity: O(M*N)

        Args:
            grid: A 2D list of strings representing the map ('1'=land, '0'=water).

        Returns:
            int: The number of distinct islands.
        """
        # --- Implement your solution here ---
        # Often involves:
        # - Getting grid dimensions (rows, cols)
        # - A way to track visited cells (e.g., modify grid, use a set)
        # - Looping through each cell (r, c)
        # - If cell is land ('1') and not visited:
        #    - Increment island count
        #    - Start a traversal (BFS or DFS) from (r, c)
        #    - Mark all reachable land cells from (r, c) as visited during traversal
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited_nodes = set()
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited_nodes:
                    print("new island")
                    island_count += 1
                    visited_nodes.add((r, c))
                    self.bfs(r, c, grid, visited_nodes)
        return island_count

    # --- Helper for traversal (BFS or DFS) ---
    def bfs(self, r, c, grid, visited):
        """Performs BFS to find all connected land cells from (r, c)"""
        rows, cols = len(grid), len(grid[0])
        # Initialize a queue with the starting cell
        queue = deque([(r, c)])
        # Mark the starting cell as visited
        visited.add((r, c))

        while queue:
            # Dequeue the next cell to process (FIFO order)
            cur_r, cur_c = queue.popleft()

            # Define the 4 possible directions (Right, Left, Down, Up)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc

                # Check if the neighbor is valid:
                # 1. Within grid boundaries
                # 2. Is land ('1')
                # 3. Has not been visited yet
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == "1"
                    and (nr, nc) not in visited
                ):

                    # Mark the valid neighbor as visited
                    visited.add((nr, nc))
                    # Enqueue the valid neighbor to explore its neighbors later
                    queue.append((nr, nc))

    def dfs(self, r, c, grid, visited):
        rows, cols = len(grid), len(grid[0])
        stack = [(r, c)]
        # Add initial node to visited HERE if not done before calling
        # visited.add((r, c))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        while stack:
            cur_r, cur_c = stack.pop()

            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc

                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Check if land and not visited
                    if grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_grid, expected_count)
test_data = [
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    ),
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    ),
    ([["1"]], 1),
    ([["0"]], 0),
    ([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]], 5),
    ([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]], 1),
    ([["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]], 1),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("grid, expected", test_data)
def test_solution(grid, expected):
    # Need deep copy if the solution modifies the grid and we want to reuse the original test data structure
    import copy

    grid_copy = copy.deepcopy(grid)
    solution = Solution()
    result = solution.numIslands(grid_copy)
    assert result == expected


# You can add more specific test functions if needed
