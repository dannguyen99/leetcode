"""
LeetCode Problem: 153 - Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium

Problem Description:
Given a sorted array of unique elements that has been rotated, find the minimum element.
The algorithm must run in O(log n) time.

Examples:
Example 1: nums = [3,4,5,1,2] -> Output: 1
Example 2: nums = [4,5,6,7,0,1,2] -> Output: 0
Example 3: nums = [11,13,15,17] -> Output: 11

Constraints:
*   1 <= nums.length <= 5000
*   -5000 <= nums[i] <= 5000
*   All integers are unique.
*   nums is sorted and rotated.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Modified Binary Search
        The algorithm uses a binary search approach to find the minimum element,
        which is the pivot point in a rotated sorted array.

        1. Initialize `left` to 0 and `right` to `len(nums) - 1`.
        2. Loop while `left <= right`:
           a. Calculate `mid = (left + right) // 2`.
           b. If `nums[mid] > nums[right]`:
              This indicates the pivot (minimum element) is in the right
              half of the current search space (`mid + 1` to `right`),
              because the segment `nums[mid...right]` is not sorted if this holds.
              So, update `left = mid + 1`.
           c. Else (`nums[mid] <= nums[right]`):
              This implies the segment `nums[mid...right]` is sorted.
              The minimum element is either `nums[mid]` or in the left half.
              i. Check if `nums[mid]` is the pivot: If `mid == 0` (i.e., `nums[mid-1]` would be `nums[-1]`)
                 or if `nums[mid-1] >= nums[mid]`, then `nums[mid]` is the minimum. Return `nums[mid]`.
              ii. Otherwise (`nums[mid-1] < nums[mid]`), `nums[mid]` is not the pivot relative
                  to its left neighbor. The minimum must be in the left half.
                  Update `right = mid - 1`.
        The loop is expected to find and return the minimum. The final return statement
        outside the loop acts as a fallback, though ideally, the internal returns cover all cases.
        (Note: For this specific implementation, the internal returns are effective.)

        Time Complexity: O(log N) - Due to the binary search halving the input size.
        Space Complexity: O(1) - Constant extra space is used.

        Args:
            nums (List[int]): The rotated sorted array of unique elements.

        Returns:
            int: The minimum element in the array.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            #  if nums[mid] > num[right], the smallest value must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # else it could be the middle value, or in the left half
            else:
                if nums[mid - 1] < nums[mid]:
                    right = mid - 1
                else:
                    return nums[mid]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_minimum)
test_data = [
    ([3, 4, 5, 1, 2], 1),  # Example 1
    ([4, 5, 6, 7, 0, 1, 2], 0),  # Example 2
    ([11, 13, 15, 17], 11),  # Example 3 (already sorted or fully rotated)
    ([1], 1),  # Single element
    ([2, 1], 1),  # Two elements, rotated
    ([5, 1, 2, 3, 4], 1),
    ([1, 2, 3, 4, 5], 1),  # Not rotated (or rotated n times)
    ([3, 1, 2], 1),
]


@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    result = solution.findMin(nums_input)
    assert result == expected
