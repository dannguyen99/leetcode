"""
LeetCode Problem: 977 - Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy

Problem Description:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Examples:
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""
from utils.test_runner import run_tests


class Solution:
    def sortedSquares(self, nums):
        """
        Approach:
        [Your approach description here]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            nums: A sorted array of integers

        Returns:
            A sorted array of the squares of each number
        """
        # Your solution here
        n = len(nums)
        result = [0] * n  # Pre-allocate the result array
        left, right = 0, n - 1

        # Fill the result array from the end (largest values) to start (smallest values)
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # Format: ((nums,), expected_output)
        (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
        (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
        (([0, 2, 4, 6, 8],), [0, 4, 16, 36, 64]),
        (([-5, -3, -2, -1],), [1, 4, 9, 25]),
        (([1],), [1]),
    ]

    run_tests(solution.sortedSquares, test_cases)
