"""
LeetCode Problem: 35 - Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy

Problem Description:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Examples:
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order
- -10^4 <= target <= 10^4
"""
from utils.test_runner import run_tests


class Solution:
    def searchInsert(self, nums, target):
        """
        Approach:
        Use binary search to find the insertion position:
        1. If target is found, return its index
        2. If target is not found, return the position where it should be inserted

        Time Complexity: O(log n) - Binary search through the array
        Space Complexity: O(1) - Constant extra space

        Args:
            nums: A sorted array of distinct integers
            target: The target value to search for or insert

        Returns:
            int: The index of target if found, otherwise the index where it would be inserted
        """
        # Your solution here
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
        # Returning left index as insertion point
        return left


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # Format: ((nums, target), expected_output)
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4),
        (([1, 3, 5, 6], 0), 0),
        (([1], 0), 0),
        (([1], 2), 1),
    ]

    run_tests(solution.searchInsert, test_cases)
