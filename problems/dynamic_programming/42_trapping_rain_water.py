"""
LeetCode Problem: 42 - Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/
Difficulty: Hard

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Examples:
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

import pytest
from typing import List, Optional  # Add other necessary types

# --- Visualization Helper Function ---
def visualize_trapped_water(height: List[int]):
    n = len(height)
    if n == 0:
        print("Empty height array.")
        return

    # Calculate left_max array (max height to the left including current)
    left_max = [0] * n
    current_max_left = 0
    for i in range(n):
        current_max_left = max(current_max_left, height[i])
        left_max[i] = current_max_left

    # Calculate right_max array (max height to the right including current)
    right_max = [0] * n
    current_max_right = 0
    for i in range(n - 1, -1, -1):
        current_max_right = max(current_max_right, height[i])
        right_max[i] = current_max_right

    # Determine max height for drawing canvas
    max_h = max(max(height), max(left_max), max(right_max)) if n > 0 else 0
    if (
        max_h == 0 and n > 0
    ):  # Ensure at least 1 unit height for non-empty all-zero arrays
        max_h = 1

    print(f"\n--- Visualization for height: {height} ---")
    print(f"Left Max:  {left_max}")
    print(f"Right Max: {right_max}")
    print("-" * (n * 4))  # Separator

    # Print the visualization from top to bottom
    # Iterate from the highest possible level down to 1 (ground level)
    for level in range(max_h, 0, -1):
        row_str = ""
        for i in range(n):
            # If the current bar reaches or exceeds this 'level', it's part of the bar
            if height[i] >= level:
                row_str += " #  "  # Represents a solid block of the bar
            # If the current bar is below this 'level', but water *could* fill up to this level
            elif min(left_max[i], right_max[i]) >= level:
                row_str += " ~  "  # Represents trapped water
            # Otherwise, it's just empty space above the bars/water
            else:
                row_str += "    "  # Represents air
        print(row_str)

    # Print the ground/base of the bars
    ground_line = ""
    for _ in range(n):
        ground_line += "----"
    print(ground_line)

    # Print the actual height values for reference below the visual
    height_values_str = ""
    for h in height:
        height_values_str += f"{h:<3} "  # Left align height numbers
    print(height_values_str)

    # Calculate and print total trapped water for verification
    total_water = 0
    for i in range(n):
        water_at_i = max(0, min(left_max[i], right_max[i]) - height[i])
        total_water += water_at_i
    print(f"Total trapped water (calculated): {total_water}")
    print("-" * (n * 4))  # End separator


# Solution Class - Implement the logic here
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach: Two Pointers (O(1) Space)

        This approach uses two pointers, `left` and `right`, starting at the ends of the array.
        It also maintains `max_left` and `max_right`, which are the maximum heights
        encountered so far from the left and right, respectively.

        The key insight is that if `max_left <= max_right`, then the water level
        at `height[left]` is determined by `max_left`. This is because we know
        there's a wall on the right (`max_right`) that is at least as tall as `max_left`,
        so `max_left` is the limiting factor for `height[left]`. We then move `left` forward.

        Conversely, if `max_right < max_left`, then the water level at `height[right]`
        is determined by `max_right`. We know there's a wall on the left (`max_left`)
        that is taller than `max_right`, so `max_right` is the limiting factor for `height[right]`.
        We then move `right` backward.

        This allows us to calculate trapped water on the fly without storing full max arrays.

        Time Complexity: O(N) - We iterate through the array once with two pointers.
        Space Complexity: O(1) - Only a few variables are used.

        Args:
            height: An array of non-negative integers representing the elevation map.

        Returns:
            The total amount of water that can be trapped.
        """
        if not height or len(height) < 3:  # Need at least 3 bars to trap water
            return 0

        total_water = 0
        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0

        while left <= right:
            if max_left <= max_right:
                # The potential water level is limited by max_left.
                # If current height[left] is greater than max_left, it becomes the new max_left.
                # Otherwise, water can be trapped.
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    total_water += max_left - height[left]
                left += 1
            else:  # max_right < max_left
                # The potential water level is limited by max_right.
                # If current height[right] is greater than max_right, it becomes the new max_right.
                # Otherwise, water can be trapped.
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += max_right - height[right]
                right -= 1

        return total_water


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_height_list, expected_output)
test_data = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([0], 0),  # Edge case: single bar
    ([1, 2, 3], 0),  # Edge case: monotonically increasing
    ([3, 2, 1], 0),  # Edge case: monotonically decreasing
    ([2, 1, 2], 1),
    ([5, 5, 1, 7, 1, 1, 5], 12),
    ([0, 0, 0, 0], 0),  # All zeros
    ([1, 1, 1, 1], 0),  # All same height
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("height, expected", test_data)
def test_solution(height, expected):
    # Visualize each test case before running the actual solution
    visualize_trapped_water(height)

    solution = Solution()
    result = solution.trap(height)
    assert result == expected
