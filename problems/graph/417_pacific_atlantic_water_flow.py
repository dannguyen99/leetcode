"""
LeetCode Problem: 417 - Pacific Atlantic Water Flow
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Difficulty: Medium

Problem Description:
Given an m x n matrix `heights` representing cell heights on an island, find all cells
from which water can flow to both the Pacific (top/left edges) and Atlantic (bottom/right edges)
oceans. Water flows to neighbors if neighbor_height <= current_height.

Examples: See LeetCode page.

Constraints:
*   1 <= m, n <= 200
*   0 <= heights[r][c] <= 10^5
"""

import pytest
from typing import List
from collections import deque


# Solution Class - Implement the logic here
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(queue, reachable_set):
            q = deque(queue)
            for r_init, c_init in q:  # Add initial border cells to reachable set
                reachable_set.add((r_init, c_init))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[nr][nc] >= heights[r][c]
                        and (nr, nc) not in reachable_set
                    ):
                        reachable_set.add((nr, nc))
                        q.append((nr, nc))

        # Pacific BFS
        pacific_q_init = []
        for r in range(rows):
            pacific_q_init.append((r, 0))
        for c in range(1, cols):  # Avoid double-adding (0,0)
            pacific_q_init.append((0, c))
        bfs(pacific_q_init, pacific_reachable)

        # Atlantic BFS
        atlantic_q_init = []
        for r in range(rows):
            atlantic_q_init.append((r, cols - 1))
        for c in range(cols - 1):  # Avoid double-adding (rows-1, cols-1)
            atlantic_q_init.append((rows - 1, c))
        bfs(atlantic_q_init, atlantic_reachable)

        # Find intersection
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        return result


# --- Test Section ---


# Define test cases as a list of tuples
# Format: (input_heights, expected_coordinates_list)
# Note: Order of coordinates in expected_list doesn't matter, nor order of pairs.
def sort_coordinates(coord_list: List[List[int]]) -> List[List[int]]:
    return sorted(coord_list)


test_data = [
    (
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    ),  # Example 1
    ([[1]], [[0, 0]]),  # Example 2
    (
        [[1, 1], [1, 1], [1, 1]],
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]],
    ),  # All cells can reach both
    (
        [[10, 10, 10], [10, 1, 10], [10, 10, 10]],
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
    ),  # Center cannot
    (
        [[3, 3, 3], [3, 0, 3], [3, 3, 3]],
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
    ),
    (
        [
            [13],
            [4],
            [19],
            [10],
            [1],
            [11],
            [5],
            [17],
            [3],
            [10],
            [1],
            [0],
            [1],
            [4],
            [1],
            [3],
            [6],
            [13],
            [2],
            [16],
            [7],
            [6],
            [3],
            [1],
            [9],
            [9],
            [13],
            [10],
            [9],
            [10],
            [6],
            [2],
            [11],
            [17],
            [13],
            [0],
            [19],
            [7],
            [13],
            [3],
            [9],
            [2],
        ],
        [
            [0, 0],
            [1, 0],
            [2, 0],
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 0],
            [7, 0],
            [8, 0],
            [9, 0],
            [10, 0],
            [11, 0],
            [12, 0],
            [13, 0],
            [14, 0],
            [15, 0],
            [16, 0],
            [17, 0],
            [18, 0],
            [19, 0],
            [20, 0],
            [21, 0],
            [22, 0],
            [23, 0],
            [24, 0],
            [25, 0],
            [26, 0],
            [27, 0],
            [28, 0],
            [29, 0],
            [30, 0],
            [31, 0],
            [32, 0],
            [33, 0],
            [34, 0],
            [35, 0],
            [36, 0],
            [37, 0],
            [38, 0],
            [39, 0],
            [40, 0],
            [41, 0],
        ],
    ),
]


@pytest.mark.parametrize("heights_input, expected_raw", test_data)
def test_solution(heights_input, expected_raw):
    solution = Solution()
    result_raw = solution.pacificAtlantic(heights_input)
    # Sort for comparison as order doesn't matter
    assert sort_coordinates(result_raw) == sort_coordinates(expected_raw)
