"""
LeetCode Problem: 11 - Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. (Lines at index 1 and 8, height = min(8, 7) = 7, width = 8-1 = 7, area = 7*7 = 49).

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
* n == height.length
* 2 <= n <= 10^5
* 0 <= height[i] <= 10^4
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum water that can be contained between two vertical lines.

        Approach:
        Two pointers, move inwards
        The idea is we can find the max area based on the width + lenght
        As we moving, we will try to keep track of the max area, based on the lower height to ensure not overflow
        The intuition is when we moving inwards,we are guarantee to reduce the width, therfore we only consider bigger height.

        Args:
            height: A list of integers representing the heights of vertical lines.

        Returns:
            int: The maximum area of water that can be contained.
        """
        # --- Implement your solution here ---
        right = len(height) - 1
        left = 0
        max_area = 0
        while left < right:
            width = right - left
            h = min([height[right], height[left]])
            if width * h > max_area:
                max_area = width * h
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_height, expected_max_area)
test_data = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),  # Lines at index 0 and 4
    ([1, 2, 1], 2),  # Lines at index 0 and 1, or 1 and 2
    (
        [1, 3, 2, 5, 25, 24, 5],
        24,
    ),  # Lines at index 1 (3) and 6 (5) -> 5*min(3,5)=15; Lines at index 4 (25) and 5 (24) -> 1*min(25,24)=24
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("height, expected", test_data)
def test_solution(height, expected):
    solution = Solution()
    result = solution.maxArea(height)
    assert result == expected


# You can add more specific test functions if needed
