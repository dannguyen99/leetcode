"""
LeetCode Problem: 53 - Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium (Often considered Easy/Medium boundary)

Problem Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Examples:
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
"""
import pytest
from typing import List
import math  # For potentially initializing max_sum

# Solution Class - Implement the logic here
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray within the given array.

        Approach:
        Kadane's Algorithm (derived from DP).
        Iterate through the array, maintaining the maximum possible subarray sum
        *ending* at the current index `i`. This sum is either the element `nums[i]`
        itself (if starting a new subarray here is better) or `nums[i]` added
        to the maximum subarray sum ending at the previous index `i-1` (if extending
        the previous subarray is better). Keep track of the overall maximum sum
        encountered across all ending positions. This implementation uses the
        input array for O(1) space DP optimization.

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            nums: A list of integers.

        Returns:
            int: The maximum sum of any contiguous subarray.
        """
        # --- Implement your solution here ---
        max_sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            max_sum = max(nums[i], max_sum)

        return max_sum


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_max_sum)
test_data = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1], -1),
    ([-2, -1], -1),  # Max sum is just the largest single element
    ([1, 2, 3], 6),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.maxSubArray(nums)
    assert result == expected


# You can add more specific test functions if needed
