"""
LeetCode Problem: 704 - Binary Search
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy

Problem Description:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, return its index. Otherwise, return -1.

Examples:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- nums is sorted in ascending order.
"""
import pytest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach:
        Use binary search to find the target:
        1. Set left = 0, right = len(nums) - 1
        2. While left <= right:
           - Compute mid = (left + right) // 2
           - If nums[mid] == target, return mid
           - If nums[mid] < target, left = mid + 1
           - Else, right = mid - 1
        3. Return -1 if not found

        Time Complexity: O(log n) - Halves the search space each step
        Space Complexity: O(1) - Constant extra space
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([5], 5, 0),
]


@pytest.mark.parametrize("nums, target, expected_output", test_cases)
def test_search(nums: List[int], target: int, expected_output: int):
    solution = Solution()
    assert solution.search(nums, target) == expected_output
