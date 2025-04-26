"""
LeetCode Problem: 33 - Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium

Problem Description:
Given a rotated sorted array `nums` (distinct values) and a `target`, return the index
of `target` if it exists, otherwise return -1. Must be O(log n).

Examples:
Example 1: Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
Example 2: Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
Example 3: Input: nums = [1], target = 0 Output: -1

Constraints:
*   1 <= nums.length <= 5000
*   -10^4 <= nums[i] <= 10^4
*   All values of `nums` are unique.
*   `nums` is possibly rotated.
*   -10^4 <= target <= 10^4
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Check if left half [left...mid] is sorted
            if nums[left] <= nums[mid]:
                # Target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  # Target is not in the sorted left half, must be in right
                    left = mid + 1
            # Otherwise, the right half [mid...right] must be sorted
            else:
                # Target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:  # Target is not in the sorted right half, must be in left
                    right = mid - 1
        return -1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, input_target, expected_output_index)
test_data = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),  # Example 1
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),  # Example 2
    ([1], 0, -1),  # Example 3
    ([1], 1, 0),  # Single element, target found
    ([5, 1, 3], 5, 0),  # Target is first element
    ([5, 1, 3], 3, 2),  # Target is last element
    ([5, 1, 3], 1, 1),  # Target is middle element
    ([3, 5, 1], 3, 0),
    ([3, 5, 1], 1, 2),
    ([3, 1], 1, 1),
    ([3, 1], 3, 0),
    ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),  # Larger example
    ([4, 5, 6, 7, 8, 1, 2, 3], 5, 1),
    ([4, 5, 6, 7, 8, 1, 2, 3], 2, 6),
    ([1, 2, 3, 4, 5, 6], 4, 3),  # Not rotated
    ([1, 2, 3, 4, 5, 6], 0, -1),  # Not rotated, target not found
]


@pytest.mark.parametrize("nums_input, target_input, expected", test_data)
def test_solution(nums_input, target_input, expected):
    solution = Solution()
    result = solution.search(nums_input, target_input)
    assert result == expected
