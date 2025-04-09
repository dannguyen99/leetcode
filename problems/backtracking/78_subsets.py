"""
LeetCode Problem: 78 - Subsets
Link: https://leetcode.com/problems/subsets/
Difficulty: Medium

Problem Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. You can return the solution in any order.

Examples:
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of nums are unique.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all possible subsets of a given set of unique integers.

        Approach:
        [Explain your approach here - likely using backtracking/recursion]

        Time Complexity: O(n * 2^n)
        Space Complexity: O(n * 2^n)

        Args:
            nums: A list of unique integers.

        Returns:
            List[List[int]]: A list containing all possible subsets.
        """
        # --- Implement your solution here ---
        # Often involves a result list and a helper/backtracking function
        result = []

        def backtrack(index, current_subset):
            # Base Case: If we've considered all elements (index reaches the end)
            if index == len(nums):
                # We have formed a complete subset. Add a *copy* to the result.
                result.append(current_subset.copy())
                return

            # --- Recursive Calls (Decisions for nums[index]) ---

            # 1. Explore the path where nums[index] is EXCLUDED
            #    Pass the current_subset *unchanged* to the next level.
            backtrack(index + 1, current_subset)

            # 2. Explore the path where nums[index] is INCLUDED
            #    a. Add the element to the current_subset
            current_subset.append(nums[index])
            #    b. Recursively call for the next index with the *modified* subset
            backtrack(index + 1, current_subset)
            #    c. BACKTRACK: Remove the element to restore the state for the
            #       previous call level (specifically, for the "exclude" path
            #       that was called *before* this "include" path).
            current_subset.pop()

        # Start the process from index 0 with an empty subset
        backtrack(0, [])
        return result


# --- Test Section ---

# Helper function to sort lists within lists for comparison, as order doesn't matter
def sort_list_of_lists_deep(list_of_lists):
    # Sort elements within each inner list
    for inner_list in list_of_lists:
        inner_list.sort()
    # Sort the outer list based on the tuple representation of inner lists
    list_of_lists.sort(key=lambda x: tuple(x))
    return list_of_lists


# Define test cases as a list of tuples
# Format: (input_nums, expected_subsets)
test_data = [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),
    ([], [[]]),  # Empty input -> list containing only the empty set
    ([1, 2], [[], [1], [2], [1, 2]]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, expected", test_data)
def test_solution(nums, expected):
    solution = Solution()
    result = solution.subsets(nums)
    # Sort both lists for comparison as subset order doesn't matter
    sorted_result = sort_list_of_lists_deep(result)
    sorted_expected = sort_list_of_lists_deep(expected)
    assert sorted_result == sorted_expected


# You can add more specific test functions if needed
