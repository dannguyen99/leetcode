"""
LeetCode Problem: 169 - Majority Element
Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy

Problem Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Examples:
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
* n == nums.length
* 1 <= n <= 5 * 10^4
* -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
import pytest
from typing import List
from collections import Counter  # Counter is very useful here

# Solution Class - Implement the logic here
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in an array.

        Approach:
        Maintain a candidate element and a counter. Iterate through the array.
        If the counter is 0, set the current element as the candidate and reset count to 1.
        If the current element matches the candidate, increment count.
        If the current element differs from the candidate, decrement count.
        The candidate remaining at the end is the majority element (guaranteed by problem statement).

        Time Complexity: O(N) - Single pass through the array.
        Space Complexity: O(1) - Only uses candidate and count variables.

        Args:
            nums: A list of integers where a majority element is guaranteed to exist.

        Returns:
            int: The majority element.
        """
        # --- Implement your solution here ---
        candidate = nums[0]
        count = 1
        for i in nums[1:]:
            if i == candidate:
                count += 1
            else:
                count -= 1
            if count > len(nums) // 2:
                return candidate
            if count == 0:
                candidate = i
                count = 1
        return candidate


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_majority_element)
test_data = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1], 1),
    ([6, 5, 5], 5),
    ([-1, -1, 2], -1),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.majorityElement(nums)
    assert result == expected


# You can add more specific test functions if needed
