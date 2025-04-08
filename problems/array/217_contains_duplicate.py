"""
LeetCode Problem: 217 - Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if any value appears at least twice in the array.

        Approach:
        use hash map to keep track of the count
        compare the count with the sum of values

        Time Complexity: O(N)
        Space Complexity: O(N)

        Args:
            nums: A list of integers.

        Returns:
            bool: True if a duplicate exists, False otherwise.
        """
        # --- Implement your solution here ---
        seen = set()
        for num in nums:
            if num in seen:  # Check if we've seen this number before O(1) avg
                return True
            seen.add(num)  # Add the number to the set O(1) avg
        return False  # If loop finishes, no duplicates were found


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output)
test_data = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([], False),  # Empty list has no duplicates
    ([5], False),  # Single element list has no duplicates
    ([-1, 5, 2, -1], True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.containsDuplicate(nums)
    assert result == expected


# You can add more specific test functions if needed
