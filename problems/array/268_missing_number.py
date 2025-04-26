"""
LeetCode Problem: 268 - Missing Number
Link: https://leetcode.com/problems/missing-number/
Difficulty: Easy

Problem Description:
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return
the only number in the range that is missing from the array.

Examples:
Example 1: Input: nums = [3,0,1] Output: 2
Example 2: Input: nums = [0,1] Output: 2
Example 3: Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8

Constraints:
*   n == nums.length
*   1 <= n <= 10^4
*   0 <= nums[i] <= n
*   All numbers in nums are unique.

Follow up: O(1) extra space and O(n) runtime?
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach:
        [Explain your approach here - e.g., Set Difference, Summation, XOR]
        Compare the sum with the full array, and deduce the missing number based on the difference

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            nums (List[int]): Array of n distinct numbers in range [0, n].

        Returns:
            int: The missing number in the range [0, n].
        """
        # Your solution here
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output_missing_number)
test_data = [
    ([3, 0, 1], 2),  # Example 1
    ([0, 1], 2),  # Example 2
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),  # Example 3
    ([0], 1),  # Single element 0
    ([1], 0),  # Single element 1
    ([1, 2, 3], 0),  # Missing 0
    ([0, 1, 2, 4], 3),  # Missing middle
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10),  # Missing n
]


@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    result = solution.missingNumber(nums_input)
    assert result == expected
