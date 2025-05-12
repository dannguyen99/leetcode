"""
LeetCode Problem: 39 - Combination Sum
Link: https://leetcode.com/problems/combination-sum/
Difficulty: Medium

Problem Description:
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

Examples:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach:
        [Explain your approach here - e.g., Backtracking]
        - We can use a recursive helper function (backtrack).
        - Parameters for backtrack: current combination, remaining target, starting index (to avoid duplicate combinations).
        - Base Cases:
            - If remaining target is 0, we found a valid combination.
            - If remaining target is negative, or we've exhausted candidates, backtrack.
        - Recursive Step (for candidate at `start_index`):
            1. Explore including `candidates[start_index]`:
               - Add `candidates[start_index]` to the current combination.
               - Recursively call `backtrack` with `remaining_target - candidates[start_index]` and the *same* `start_index` (to allow reuse).
               - Backtrack: remove `candidates[start_index]`.
            2. Explore excluding `candidates[start_index]` (by moving to the next distinct candidate):
               - Recursively call `backtrack` with the same `remaining_target` and `start_index + 1`.

        Time Complexity: O(N^(T/M + 1)), where N is number of candidates, T is target, M is min value in candidates.
                       More loosely, it can be exponential. The number of combinations can be large.
        Space Complexity: O(T/M) for recursion stack depth in worst case (using smallest candidate repeatedly).
                        Output space can be significant.

        Args:
            candidates (List[int]): A list of distinct integers.
            target (int): The target sum.

        Returns:
            List[List[int]]: A list of all unique combinations that sum to target.
        """
        results = []

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(current_combination.copy())
                return
            if remaining_target < 2:
                return
            current_combination.append(candidates[start_index])
            backtrack(
                current_combination,
                remaining_target - candidates[start_index],
                start_index,
            )
            current_combination.pop()
            if start_index + 1 < len(candidates):
                backtrack(current_combination, remaining_target, start_index + 1)

        # Initial call to backtrack, e.g.,
        backtrack([], target, 0)
        return results


# --- Test Section ---

# Helper function to sort lists of lists for consistent comparison
def sorted_lol(list_of_lists):
    return sorted([sorted(sub_list) for sub_list in list_of_lists])


test_data = [
    ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
    ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ([2], 1, []),
    (
        [2, 3, 7],
        18,
        [
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 3, 3],
            [2, 2, 2, 2, 3, 7],
            [2, 2, 2, 3, 3, 3, 3],
            [2, 2, 7, 7],
            [2, 3, 3, 3, 7],
            [3, 3, 3, 3, 3, 3],
        ],
    ),  # Example from a similar problem, adjusted
]


@pytest.mark.parametrize("candidates, target, expected_output", test_data)
def test_combination_sum(candidates, target, expected_output):
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    assert sorted_lol(result) == sorted_lol(expected_output)
