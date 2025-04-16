"""
LeetCode Problem: 283 - Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Problem Description:
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Examples:
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
*   1 <= nums.length <= 10^4
*   -2^31 <= nums[i] <= 2^31 - 1

Follow up: Minimize the total number of operations.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Approach: Two Pointers (In-place)
        Uses two pointers: `i` (the current element being examined) and
        `non_zero_index` (the position where the next non-zero element should
        be placed).

        Iterate through the array with `i`. If `nums[i]` is not zero, it means
        we've found a non-zero element that should be placed at the
        `non_zero_index`. We swap `nums[i]` and `nums[non_zero_index]`.
        Crucially, we only increment `non_zero_index` *after* placing a
        non-zero element there.

        If `nums[i]` is zero, we simply continue iterating with `i`, leaving
        `non_zero_index` unchanged, as we are still looking for the next
        position to place a non-zero element.

        This ensures that all non-zero elements are moved to the front of the
        array in their original relative order, and all zeros are effectively
        moved to the end. The swap `nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]`
        handles both cases: moving a non-zero element forward and swapping a zero
        into the position `i`.

        Time Complexity: O(N) - We iterate through the array once.
        Space Complexity: O(1) - We modify the array in-place using only pointers.

        Args:
            nums (List[int]): The list of integers to modify.

        Returns:
            None: The function modifies the input list `nums` directly.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            # If the current element is non-zero...
            if nums[i] != 0:
                # ...swap it with the element at non_zero_index
                # If i and non_zero_index are the same, this swap does nothing,
                # which is correct.
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Increment non_zero_index to mark the next spot for a non-zero element
                non_zero_index += 1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output_nums_after_modification)
test_data = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),  # Example 1
    ([0], [0]),  # Example 2
    ([1, 2, 3, 4], [1, 2, 3, 4]),  # No zeroes
    ([0, 0, 0, 0], [0, 0, 0, 0]),  # All zeroes
    ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),  # Interspersed zeroes
    ([1, 0], [1, 0]),  # Simple case
    ([0, 1], [1, 0]),  # Simple case swap
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    # Copy the input list for modification, as pytest might reuse it otherwise
    nums_to_modify = list(nums_input)
    solution.moveZeroes(nums_to_modify)
    assert nums_to_modify == expected
