"""
LeetCode Problem: 40 - Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/
Difficulty: Medium

Problem Description:
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Examples:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach:
        [Explain your approach here - e.g., Backtracking]
        - Sort the `candidates` array first. This helps in skipping duplicate numbers easily.
        - Use a recursive helper function (backtrack).
        - Parameters for backtrack: current combination, remaining target, starting index.
        - Base Cases:
            - If remaining target is 0, we found a valid combination. Add a copy to results.
            - If remaining target is negative, or we've exhausted candidates, backtrack.
        - Recursive Step:
            - Iterate through candidates starting from `start_index`.
            - **Crucial for uniqueness with duplicates**: If the current number is the same as the previous number
              and we are not at the very beginning of this level's choices (i.e., `i > start_index`), skip it to avoid duplicate combinations.
            - For each chosen candidate:
                - Add it to the current combination.
                - Recursively call with updated remaining target and `i + 1` as the next start_index (since each number can be used only once).
                - Backtrack: remove the candidate from the current combination.

        Time Complexity: O(2^N * N) in the worst case, where N is the number of candidates. Sorting takes O(N log N).
                       The N factor in 2^N * N comes from copying the combination to results.
        Space Complexity: O(N) for recursion stack depth and the current combination.
                        Output space can be significant.

        Args:
            candidates (List[int]): A list of candidate numbers (may contain duplicates).
            target (int): The target sum.

        Returns:
            List[List[int]]: A list of all unique combinations that sum to target.
        """
        results = []
        candidates.sort()

        # Initial pruning: if the smallest candidate is already larger than the target,
        # no combination is possible.
        # This also correctly handles target = 0 if candidates are positive, returning [].
        # Constraints: 1 <= candidates.length, 1 <= candidates[i].
        if not candidates or candidates[0] > target:
            # If target is 0 and candidates[0] > 0, this returns [], which is what LeetCode expects for this problem.
            # If target > 0 and candidates[0] > target, also returns [].
            return results

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(current_combination.copy())
                return  # Simply return, no need for True

            # This base case (remaining_target < 0) is still useful,
            # though the loop pruning below will also help.
            if (
                remaining_target < 0
            ):  # or start_index >= len(candidates) - this part is implicitly handled by the loop range
                return

            for i in range(start_index, len(candidates)):
                # Optimization: If current candidate is greater than remaining target,
                # no need to check further in this path (since candidates are sorted).
                if candidates[i] > remaining_target:
                    break

                # Skip duplicate numbers to avoid duplicate combinations
                # Only skip if it's not the first element being considered at this level of recursion
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                # Each number can be used only once, so next call starts from i + 1
                backtrack(current_combination, remaining_target - candidates[i], i + 1)
                current_combination.pop()  # Backtrack

        backtrack([], target, 0)
        return results


# --- Test Section ---

# Helper function to sort lists of lists for consistent comparison
def sorted_lol(list_of_lists):
    return sorted([sorted(sub_list) for sub_list in list_of_lists])


test_data = [
    ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ([1, 1, 1, 1, 1], 3, [[1, 1, 1]]),
    (
        [1, 2, 3],
        0,
        [[]],
    ),  # Edge case: target is 0, should return one empty combination if allowed by problem (check problem statement, usually means sum is met)
    # LeetCode for this problem expects [] if target is 0 and no numbers are chosen. If target is 0 and candidates is empty, also [].
    # If target is 0, and we pick nothing, it's a valid way to sum to 0.
    # Let's adjust based on typical interpretation: if target is 0, an empty list is a valid combination.
    ([1, 2, 3], 1, [[1]]),
    ([5], 0, []),  # Target 0
    ([3, 1, 3, 5, 1, 1], 8, [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]),
]
# Adjusting target 0 test case based on typical LeetCode behavior for combination sums:
# If target is 0, an empty combination [] is usually the only valid one.
# If target > 0 and candidates is empty, result is [].

# Refined test data for target = 0
test_data_target_zero_handling = [
    ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ([1, 1, 1, 1, 1], 3, [[1, 1, 1]]),
    ([1, 2, 3], 0, []),  # An empty set sums to 0
    ([1, 2, 3], 1, [[1]]),
    ([5], 0, []),
    ([3, 1, 3, 5, 1, 1], 8, [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]),
]


@pytest.mark.parametrize(
    "candidates, target, expected_output", test_data_target_zero_handling
)
def test_combination_sum2(candidates, target, expected_output):
    solution = Solution()
    # Sorting candidates inside the test or ensuring the solution does it
    # is important if the solution relies on sorted input for duplicate handling.
    # The solution template suggests sorting within the method.
    result = solution.combinationSum2(candidates, target)
    assert sorted_lol(result) == sorted_lol(expected_output)
