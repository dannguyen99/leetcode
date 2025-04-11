"""
LeetCode Problem: 136 - Single Number
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy

Problem Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
* 1 <= nums.length <= 3 * 10^4
* -3 * 10^4 <= nums[i] <= 3 * 10^4
* Each element in the array appears twice except for one element which appears only once.
"""
import pytest
from typing import List

# from collections import Counter # Could be used for non-constant space approach

# Solution Class - Implement the logic here
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the single element that appears only once in an array where
        all other elements appear twice.

        Approach:
        XOR operation. Insight:
        x ^ x = 0
        x ^ 0 = x

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            nums: A list of integers where one element is unique and others appear twice.

        Returns:
            int: The unique element.
        """
        result = 0
        for i in nums:
            result ^= i
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_single_number)
test_data = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
    ([-1, -1, -2], -2),  # Negative numbers
    ([0, 0, 5], 5),  # Zero
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.singleNumber(nums)
    assert result == expected


# You can add more specific test functions if needed
