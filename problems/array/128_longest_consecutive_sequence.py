"""
LeetCode Problem: 128 - Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium

Problem Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Examples:
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
* 0 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest sequence of consecutive elements
        in an unsorted array.

        Approach:
        [Explain your approach here - likely using a hash set]

        Args:
            nums: A list of integers.

        Returns:
            int: The length of the longest consecutive sequence.
        """
        # --- Implement your solution here ---
        visited = set()
        longest = 0
        for i in nums:
            visited.add(i)
        for i in visited:
            if i - 1 not in visited:
                next = i + 1
                while next in visited:
                    next += 1
                if next - i > longest:
                    longest = next - i
        return longest


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_length)
test_data = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1, 2, 0, 1], 3),  # Contains duplicates
    ([5, 4, 3, 2, 1], 5),  # Reverse sorted
    (
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        7,
    ),  # Example with negative and skipped numbers
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.longestConsecutive(nums)
    assert result == expected


# You can add more specific test functions if needed
