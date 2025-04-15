"""
LeetCode Problem: 300 - Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Difficulty: Medium

Problem Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Examples:
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from bisect import bisect_left
import pytest
from typing import List, Optional  #


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Approach:
        [Explain your approach here - What does the DP state `dp[i]` represent?
         How can you calculate `dp[i]` based on previous values `dp[j]` where j < i?]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            int: The length of the longest strictly increasing subsequence.
        """
        # Your solution here
        dp = [1] * len(nums)
        for i in range(len(nums)):
            # Check all previous elements j
            for j in range(i):
                # If nums[i] can extend the subsequence ending at j...
                if nums[j] < nums[i]:
                    # ...update dp[i] if this path is longer than the current best for dp[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) if nums else 0  # Handle empty input edge case

    def lengthOfLISBiSearch(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output)
test_data = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([1], 1),
    ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),  # Example: [1, 3, 6, 7, 9, 10]
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums: List[int], expected: int):
    solution = Solution()
    result = solution.lengthOfLISBiSearch(nums)
    assert result == expected
