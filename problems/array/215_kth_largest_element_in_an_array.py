"""
LeetCode Problem: 215 - Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium

Problem Description:
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) average time complexity [Note: This hints at QuickSelect, but O(n log k) with heap is also commonly accepted/expected].

Examples:
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
* 1 <= k <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
"""
import pytest
import heapq  # Import the heapq module for heap operations
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in an unsorted array.

        Approach:
        Use min-heap to manage k largest element
        In the end just return the root of the min-heap which will be the kth largest element.
        This is because the root of the min-heap will always be the smallest element in the heap, and since we are maintaining k elements, it will be the kth largest in the original array.

        Time Complexity: O(N logk)
        Space Complexity: O(k)

        Args:
            nums: List of integers.
            k: The rank of the desired largest element.

        Returns:
            int: The value of the kth largest element.
        """
        # --- Implement your solution here ---
        top_k = []
        for num in nums:
            if len(top_k) < k:
                heapq.heappush(top_k, num)
            elif num > top_k[0]:
                heapq.heappushpop(top_k, num)
        return top_k[0]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, k, expected_output)
test_data = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1], 1, 1),
    ([7, 6, 5, 4, 3, 2, 1], 1, 7),
    ([7, 6, 5, 4, 3, 2, 1], 7, 1),
    ([3, 1, 2, 4], 2, 3),  # Example where sorting helps visualize
    ([-1, -1], 1, -1),  # Negative numbers
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("nums, k, expected", test_data)
def test_solution(nums, k, expected):
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    assert result == expected


# You can add more specific test functions if needed
