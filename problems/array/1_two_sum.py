"""
LeetCode Problem: 1 - Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Examples:
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""
import pytest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach:
        Use a hash map to store numbers encountered and their indices {num: index}.
        Iterate through nums. For each number, check if its complement (target - num)
        is already in the map. If yes, return the indices. If no, add the current
        number and index to the map.

        Time Complexity: O(N) - Single pass. Avg. O(1) map operations.
        Space Complexity: O(N) - Worst case stores N elements in map.

        Args:
            nums: List[int] - Input array of integers.
            target: int - The target sum.

        Returns:
            List[int] - Indices of the two numbers summing to target.
        """
        # Maps number to its index for fast complement lookup.
        num_to_index_map = {}

        for current_index, current_num in enumerate(nums):
            complement = target - current_num

            # Check if the complement needed has been seen before.
            if complement in num_to_index_map:
                # Found the pair.
                complement_index = num_to_index_map[complement]
                return [complement_index, current_index]
            else:
                # Store the current number's index for future checks.
                num_to_index_map[current_num] = current_index

        # Per problem constraints, a solution always exists, so this is unreachable.
        # Return empty list for type consistency if constraints change.
        return []


test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 4, 3, 0], 0, [0, 3]),
]


@pytest.mark.parametrize("nums, target, expected_output", test_cases)
def test_twoSum(nums: List[int], target: int, expected_output: List[int]):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected_output
