"""
LeetCode Problem: 198 - House Robber
Link: https://leetcode.com/problems/house-robber/
Difficulty: Medium

Problem Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Examples:
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 400
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Calculates the maximum amount of money that can be robbed from non-adjacent houses.

        Approach:
        Intuition:
        the choice at i is affected by the choice at i-1 and i-2.
        - if choose i, we have the total sum is i + i-2
        - else we have the total sum is i-1 and continue
        choose the maximum value

        Time Complexity: O(N) - loop through each element once
        Space Complexity: O(1) - Only use the array from input

        Args:
            nums: A list representing the money in each house.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        return nums[-1]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_max_amount)
test_data = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([0], 0),
    ([1], 1),
    ([2, 1], 2),  # Rob only the first house
    ([1, 2], 2),  # Rob only the second house
    ([2, 1, 1, 2], 4),  # Rob 2 + 2
    ([6, 7, 1, 30, 8, 2, 4], 41),  # 7 + 30 + 4
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.rob(nums)
    assert result == expected


# You can add more specific test functions if needed
