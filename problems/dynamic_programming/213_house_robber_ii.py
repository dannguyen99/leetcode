"""
LeetCode Problem: 213 - House Robber II
Link: https://leetcode.com/problems/house-robber-ii/
Difficulty: Medium

Problem Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

Examples:
Example 1:
Input: nums = [2,3,2]
Output: 3

Example 2:
Input: nums = [1,2,3,1]
Output: 4

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
*   1 <= nums.length <= 100
*   0 <= nums[i] <= 1000
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Approach:
        Break down the problem into 2 sub problem similar to house robber I.
        - If we rob decide to rob the first house, we can not rob the final house.
        - If we decide not to rob the first house,
          which effectively mean the best possible of the first 2 hosue is the second house, we can rob the final house.

        Time Complexity: O(N) - goes through N element
        Space Complexity: O(N) - store 2 copy of the array nums

        Args:
            nums (List[int]): Amount of money in each house arranged in a circle.

        Returns:
            int: Maximum amount of money that can be robbed.
        """
        # Your solution here
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))

    def _rob_linear(self, sub_array):
        result_i = max(sub_array[0], sub_array[1])
        result_i_minus = sub_array[0]
        for i in range(2, len(sub_array)):
            result_i, result_i_minus = (
                max(sub_array[i] + result_i_minus, result_i),
                result_i,
            )
        return result_i


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output)
test_data = [
    ([2, 3, 2], 3),  # Example 1
    ([1, 2, 3, 1], 4),  # Example 2
    ([1, 2, 3], 3),  # Example 3
    ([1], 1),  # Single house
    ([2, 7, 9, 3, 1], 11),  # Rob 2 + 9 = 11 (cannot rob 2 and 1)
    ([2, 1, 1, 2], 3),  # Rob 2 + 1 = 3 or 1 + 2 = 3
    ([0], 0),  # Zero money
    ([1, 3, 1, 3, 100], 103),
    ([0, 0], 0),
]


@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    result = solution.rob(list(nums_input))  # Pass a copy
    assert result == expected
