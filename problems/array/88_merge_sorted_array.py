"""
LeetCode Problem: 88 - Merge Sorted Array

Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy

**Problem Description:**
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Examples:**
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].
Note that the output array is not returned.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, nums1 has no valid elements for the merge. You can assume it is an empty array (conceptually).

**Constraints:**
*   `nums1.length == m + n`
*   `nums2.length == n`
*   `0 <= m, n <= 200`
*   `1 <= m + n <= 200`
*   `-10^9 <= nums1[i], nums2[j] <= 10^9`
*   `nums1` and `nums2` are sorted in non-decreasing order.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Approach:
        [Explain your approach here]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            nums1: The first array, which will store the merged result. Has length m + n.
            m: The number of valid elements in nums1.
            nums2: The second array to be merged. Has length n.
            n: The number of elements in nums2.

        Returns:
            None (the merge is done in-place on nums1)
        """
        # Your solution here
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        i = m - 1
        j = n - 1
        index = m + n - 1
        while index >= 0:
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (nums1_initial, m, nums2, n, expected_nums1_after_merge)
test_data = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    (
        [4, 5, 6, 0, 0, 0],
        3,
        [1, 2, 3],
        3,
        [1, 2, 3, 4, 5, 6],
    ),  # Test with nums2 elements smaller
    ([1, 2, 3, 4, 5, 6], 6, [], 0, [1, 2, 3, 4, 5, 6]),  # Test with empty nums2
    ([0, 0], 0, [1, 2], 2, [1, 2]),  # Test with empty nums1
    ([1, 0], 1, [2], 1, [1, 2]),  # Small case
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize(
    "nums1_initial, m, nums2, n, expected_nums1_after_merge", test_data
)
def test_solution(nums1_initial, m, nums2, n, expected_nums1_after_merge):
    solution = Solution()
    # Create a copy of nums1_initial because the merge method modifies it in-place
    nums1_copy = list(nums1_initial)
    solution.merge(nums1_copy, m, nums2, n)
    assert nums1_copy == expected_nums1_after_merge
