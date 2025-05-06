"""
LeetCode Problem: 26 - Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy

Problem Description:
Given a sorted array `nums`, remove duplicates in-place such that each unique element
appears once. Return the number of unique elements (k). The first k elements of `nums`
should hold the unique elements.

Examples:
Example 1: nums = [1,1,2] -> Output: 2, nums = [1,2,_]
Example 2: nums = [0,0,1,1,1,2,2,3,3,4] -> Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
*   1 <= nums.length <= 3 * 10^4
*   -100 <= nums[i] <= 100
*   nums is sorted non-decreasingly.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Approach: Two Pointers
        This solution uses a two-pointer technique to modify the array in-place.
        - The `left` pointer tracks the index of the last unique element found and placed.
          It essentially marks the end of the processed unique elements subarray.
        - The `right` pointer iterates through the array from left to right, examining each element.

        The algorithm proceeds as follows:
        1. Initialize `left` and `right` pointers to 0.
        2. While the `right` pointer is within the bounds of the array:
           a. If `nums[left]` is the same as `nums[right]`, it means `nums[right]` is a duplicate
              of the last unique element found. In this case, we simply increment `right` to
              check the next element.
           b. If `nums[left]` is different from `nums[right]`, it means `nums[right]` is a new
              unique element. We then:
              i. Increment `left` to point to the next position where this unique element
                 should be stored.
              ii. Assign `nums[right]` to `nums[left]`.
        3. An optimization is used: if the element just placed at `nums[left]` is the largest
           element in the original array, we can break early as no more unique elements will follow.
        4. The number of unique elements `k` is `left + 1`.

        Time Complexity: O(N) - Each pointer traverses the array at most once.
        Space Complexity: O(1) - In-place modification.

        Args:
            nums (List[int]): The sorted array with potential duplicates.

        Returns:
            int: The number of unique elements (k).
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_k, expected_nums_prefix)
test_data = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([1, 1, 1, 1, 1], 1, [1]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1], 1, [1]),  # Edge case: single element
]


@pytest.mark.parametrize("nums_input, expected_k, expected_prefix", test_data)
def test_solution(nums_input, expected_k, expected_prefix):
    solution = Solution()
    # Make a copy for the assertion, as the function modifies nums_input in-place
    nums_copy = list(nums_input)
    k = solution.removeDuplicates(nums_copy)
    assert k == expected_k
    for i in range(k):
        assert nums_copy[i] == expected_prefix[i]
