"""
LeetCode Problem: 733 - Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy

Problem Description:
Given an m x n image grid, a starting pixel (sr, sc), and a new color, perform a
flood fill. Replace the color of the starting pixel and all connected (4-directionally)
pixels of the same original color with the new color.

Examples: See LeetCode page.

Constraints: See LeetCode page.
"""

import pytest
from collections import deque
from typing import List


# Solution Class - Implement the logic here
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return image

        original_color = image[sr][sc]
        # If the starting pixel already has the target color, no work needed.
        if original_color == color:
            return image

        rows = len(image)
        cols = len(image[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(sr, sc)])

        # Color the starting pixel first
        image[sr][sc] = color

        while queue:
            row, column = queue.popleft()

            for dr, dc in direction:
                target_row, target_column = row + dr, column + dc

                # Check boundaries and if the neighbor has the original color
                if (
                    0 <= target_row < rows
                    and 0 <= target_column < cols
                    and image[target_row][target_column] == original_color
                ):
                    # Color the valid neighbor (marking it visited)
                    image[target_row][target_column] = color
                    # Add it to the queue to process its neighbors
                    queue.append((target_row, target_column))

        return image


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_image, sr, sc, new_color, expected_output_image)
test_data = [
    (
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        1,
        1,
        2,
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),  # Example 1
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),  # Example 2 (No change)
    ([[0, 0, 0], [0, 1, 1]], 1, 1, 1, [[0, 0, 0], [0, 1, 1]]),  # Start on new color
    (
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        0,
        0,
        2,
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),  # Start at corner
    ([[0, 0, 0], [0, 0, 0]], 1, 0, 2, [[2, 2, 2], [2, 2, 2]]),  # Fill all
    ([[1]], 0, 0, 5, [[5]]),  # Single pixel
]


@pytest.mark.parametrize(
    "image_input, sr_input, sc_input, color_input, expected", test_data
)
def test_solution(image_input, sr_input, sc_input, color_input, expected):
    solution = Solution()
    # Make a deep copy if the function modifies the input list in place
    # For this problem, modifying in place is typical and expected.
    # If using BFS/DFS, ensure you handle visited/modified cells correctly.
    result = solution.floodFill(image_input, sr_input, sc_input, color_input)
    assert result == expected
