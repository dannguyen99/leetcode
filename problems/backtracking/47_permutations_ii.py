"""
LeetCode Problem: 47 - Permutations II
Link: https://leetcode.com/problems/permutations-ii/
Difficulty: Medium

Problem Description:
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.

Examples:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        [Explain your approach here - e.g., Backtracking with duplicate handling]
        - Sort the `nums` array first. This helps in grouping identical numbers together,
          making it easier to skip generating duplicate permutations.
        - Use a recursive helper function (backtrack).
        - Parameters for backtrack: current permutation being built, and a way to track used elements (e.g., a boolean `used` array or frequency map).
        - Base Case:
            - If the length of the current permutation equals the length of `nums`, a complete permutation is found. Add a copy to results.
        - Recursive Step:
            - Iterate through the `nums` array.
            - If the current number `nums[i]` has already been used in the current permutation, skip it.
            - **Crucial for uniqueness with duplicates**: If `nums[i]` is the same as `nums[i-1]` (and `i > 0`)
              AND `nums[i-1]` was *not* used (i.e., `used[i-1]` is false), then skip `nums[i]`.
              This ensures that for a sequence of identical numbers, we only pick them in the order they appear
              in the sorted array for a given "slot" in the permutation, thus avoiding duplicates like [1a, 1b, 2] and [1b, 1a, 2]
              if 1a and 1b are identical.
            - Add `nums[i]` to the current permutation. Mark `nums[i]` as used.
            - Recursively call backtrack.
            - Backtrack: remove `nums[i]` from the current permutation and mark it as unused.

        Time Complexity: O(N * N!), where N is the number of elements in nums.
                       In the worst case (all unique elements), there are N! permutations, and each takes O(N) to copy.
                       Sorting takes O(N log N).
        Space Complexity: O(N) for the recursion stack, the `used` array, and the current permutation being built.
                        Output space can be O(N * N!).

        Args:
            nums (List[int]): A list of numbers, possibly with duplicates.

        Returns:
            List[List[int]]: A list of all unique permutations.
        """
        results = []
        nums.sort()  # Sorting is highly recommended
        used = [False] * len(nums)  # To keep track of used elements at current path

        def backtrack(current_permutation):
            if len(current_permutation) == len(nums):
                results.append(current_permutation.copy())
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    current_permutation.append(nums[i])
                    used[i] = True
                    backtrack(current_permutation)
                    current_permutation.pop()
                    used[i] = False

        # Initial call to backtrack, e.g.,
        backtrack([])
        return results


# --- Test Section ---

# Helper function to sort lists of lists for consistent comparison
# Permutations' internal order matters, but the order of permutations in the result list doesn't.
def sorted_lol_for_permutations(list_of_lists):
    # Sort each sublist (permutation) then sort the list of permutations
    return sorted([sorted(p) for p in list_of_lists])


# For permutations, the exact order of elements within each permutation matters,
# but the order of permutations in the final list does not.
# So, we sort the list of lists to compare.
# It's often easier to convert to tuples for set comparison if order within sublist matters.
def compare_list_of_lists_of_perms(l1, l2):
    # Convert each inner list to a tuple to make them hashable for set comparison
    # Then sort the outer list of tuples for consistent ordering.
    s1 = sorted([tuple(p) for p in l1])
    s2 = sorted([tuple(p) for p in l2])
    return s1 == s2


test_data = [
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
    ([1, 1, 1], [[1, 1, 1]]),
    (
        [1, -1, 1, 2, -1, 2, 2],  # A more complex case
        # Expected output for [1,-1,1,2,-1,2,2] would be large, let's use a simpler one or verify count
        # For testing, it's better to use smaller, verifiable cases.
    ),
]
# Simpler test data for now
test_data_simple = [
    ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
    ([1, 1, 1], [[1, 1, 1]]),
    (
        [2, 2, 1, 1],
        [
            [1, 1, 2, 2],
            [1, 2, 1, 2],
            [1, 2, 2, 1],
            [2, 1, 1, 2],
            [2, 1, 2, 1],
            [2, 2, 1, 1],
        ],
    ),
]


@pytest.mark.parametrize("nums, expected_output", test_data_simple)
def test_permute_unique(nums, expected_output):
    solution = Solution()
    result = solution.permuteUnique(nums)
    assert compare_list_of_lists_of_perms(result, expected_output)
