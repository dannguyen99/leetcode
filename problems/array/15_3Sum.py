"""
LeetCode Problem: 15 - 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium

Problem Description:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]`
such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

Examples:
Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]
Example 2: Input: nums = [0,1,1] Output: []
Example 3: Input: nums = [0,0,0] Output: [[0,0,0]]

Constraints:
*   3 <= nums.length <= 3000
*   -10^5 <= nums[i] <= 10^5
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        [Explain your approach here - e.g., Sorting + Two Pointers]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            List[List[int]]: A list of unique triplets that sum to zero.
        """
        # Your solution here
        nums = sorted(nums)
        n = len(nums)
        result = set()
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
                elif cur_sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(result)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output_triplets)
# Note: Expected output should be sorted internally and the list of triplets sorted for consistent comparison.
test_data = [
    ([-1, 0, 1, 2, -1, -4], sorted([[-1, -1, 2], [-1, 0, 1]])),  # Example 1
    ([0, 1, 1], []),  # Example 2
    ([0, 0, 0], [[0, 0, 0]]),  # Example 3
    ([], []),  # Empty input
    ([1, 2, -3], [[-3, 1, 2]]),  # Simple case
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),  # Duplicates in input and output
    ([-1, 0, 1, 0], [[-1, 0, 1]]),  # Duplicate zero
    ([1, 1, -2], [[-2, 1, 1]]),
    (
        [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
        sorted(
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
        ),
    ),  # Complex case
]

# Helper to sort lists of lists for comparison
def sort_list_of_lists(list_of_lists: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(inner_list) for inner_list in list_of_lists])


@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    result = solution.threeSum(list(nums_input))  # Pass a copy
    # Sort the result for consistent comparison
    sorted_result = sort_list_of_lists(result)
    assert sorted_result == expected
