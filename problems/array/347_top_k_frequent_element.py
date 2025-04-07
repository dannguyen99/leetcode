"""
LeetCode Problem: 347 - Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium

Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Examples:
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import pytest
from typing import List
import collections
import heapq  # <-- Useful import!

# Solution Class - Implement the logic here
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the array.

        Approach:
        Use a hashmap to track the count of each element
        Use a min-heap to track the top k element efficiently.

        Time complexity: O(n log k): Assign the element to hashmap, heap operation
        Space complexity O(n + k?): Hashmap and heap

        Args:
            nums: The input list of integers.
            k: The number of most frequent elements to return.


        Returns:
            List[int]: The k most frequent elements.
        """
        if len(nums) == k:
            return nums
        count = collections.Counter(nums)
        topk = []
        for num in count.keys():
            if len(topk) < k:
                heapq.heappush(topk, (count[num], num))
            elif count[num] > topk[0][0]:
                heapq.heappushpop(topk, (count[num], num))
        return [c[1] for c in topk]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, k, expected_output)
test_data = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2], 2, [1, 2]),  # k equals number of unique elements
    ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ([-1, -1], 1, [-1]),
    ([5, 3, 1, 1, 1, 3, 73, 1], 1, [1]),
]

# Use pytest.mark.parametrize to create tests for each case
# Need to sort expected and result lists because order doesn't matter
@pytest.mark.parametrize("nums, k, expected", test_data)
def test_solution(nums, k, expected):
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)


# You can add more specific test functions if needed
