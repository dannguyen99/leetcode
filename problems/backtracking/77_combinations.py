"""
LeetCode Problem: 77 - Combinations
Link: https://leetcode.com/problems/combinations/
Difficulty: Medium

Problem Description:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Examples:
Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 combinations.

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
* 1 <= n <= 20
* 1 <= k <= n
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Finds all possible combinations of k numbers from the range [1, n]
        using standard backtracking.

        Approach:
        Recursively build combinations. At each step, decide which number
        to add next, ensuring numbers are chosen in increasing order to
        avoid duplicate combinations. Stop when a combination reaches size k.

        Time Complexity: O(k * C(n, k)) where C(n,k) is "n choose k"
                       (Number of combinations * time to copy each)
        Space Complexity: O(k * C(n, k)) (for output) + O(k) (recursion depth)

        Args:
            n: The upper bound of the range [1, n].
            k: The size of combinations to generate.

        Returns:
            List[List[int]]: A list containing all combinations of size k.
        """
        result = []

        def backtrack(start_num, current_combination):
            # Base Case: If the combination has reached the desired size k
            if len(current_combination) == k:
                # Add a *copy* of the valid combination to the result list
                result.append(current_combination.copy())
                # Stop exploring further down this path (no need to add more numbers)
                return

            # --- Explore adding the next number ---
            # Iterate through possible numbers to add, starting from start_num
            # The upper bound ensures we don't pick numbers > n
            for i in range(start_num, n + 1):
                # --- Optional Pruning (Can improve performance slightly) ---
                # If the number of elements still needed is greater than the
                # number of elements remaining, we can't possibly form a valid
                # combination, so prune this path.
                elements_needed = k - len(current_combination)
                elements_remaining = n - i + 1
                if elements_remaining < elements_needed:
                    break  # No point checking further numbers in this loop either

                # Choose: Add the current number 'i' to the combination
                current_combination.append(i)

                # Explore: Recursively call to find the next element,
                # starting from i + 1 to ensure increasing order and avoid duplicates.
                backtrack(i + 1, current_combination)

                # Backtrack: Remove the number 'i' before the next iteration
                # of the for loop, effectively undoing the choice.
                current_combination.pop()

        # Start the backtracking process:
        # Begin searching for numbers from 1, with an initially empty combination.
        backtrack(1, [])

        return result


# --- Test Section ---

# Helper function to sort lists within lists for comparison, as order doesn't matter
def sort_list_of_lists_deep(list_of_lists):
    for inner_list in list_of_lists:
        inner_list.sort()
    list_of_lists.sort(key=lambda x: tuple(x))
    return list_of_lists


# Define test cases as a list of tuples
# Format: (n, k, expected_combinations)
test_data = [
    (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    (1, 1, [[1]]),
    (
        5,
        3,
        [
            [1, 2, 3],
            [1, 2, 4],
            [1, 2, 5],
            [1, 3, 4],
            [1, 3, 5],
            [1, 4, 5],
            [2, 3, 4],
            [2, 3, 5],
            [2, 4, 5],
            [3, 4, 5],
        ],
    ),
    (3, 1, [[1], [2], [3]]),
    (2, 1, [[1], [2]]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("n, k, expected", test_data)
def test_solution(n, k, expected):
    solution = Solution()
    result = solution.combine(n, k)
    sorted_result = sort_list_of_lists_deep(result)
    sorted_expected = sort_list_of_lists_deep(expected)
    assert sorted_result == sorted_expected


# You can add more specific test functions if needed
