"""
LeetCode Problem: 46 - Permutations
Link: https://leetcode.com/problems/permutations/
Difficulty: Medium

Problem Description:
Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

Examples:
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
*   1 <= nums.length <= 6
*   -10 <= nums[i] <= 10
*   All the integers of `nums` are **unique**.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the input list using backtracking.

        Approach:
        Uses a recursive backtracking helper function.
        - Maintains a `current_path` list representing the permutation being built.
        - Uses a `used_numbers` boolean-like array (0 or 1) to track which numbers
          from the original `nums` array have been included in the `current_path`.
        - The base case for the recursion is when the number of used numbers equals
          the total number of elements (`len(nums)`), indicating a complete
          permutation has been formed. A copy of `current_path` is added to the result.
        - In the recursive step, iterate through all numbers in `nums`. If a number
          at index `i` hasn't been used (`used_numbers[i] == 0`), add it to
          `current_path`, mark it as used (`used_numbers[i] = 1`), and make a
          recursive call.
        - After the recursive call returns (backtracking), undo the choice: mark the
          number as unused (`used_numbers[i] = 0`) and remove it from `current_path`
          (`current_path.pop()`) to explore other possibilities.

        Time Complexity: O(N * N!) - There are N! permutations, and it takes O(N)
                       time to build and copy each permutation.
        Space Complexity: O(N) - Excluding the output list. This accounts for the
                        recursion stack depth, the `used_numbers` array, and the
                        `current_path` list, all of which are proportional to N.
                        (O(N * N!) if including the space for the output).

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list containing all possible permutations of nums.
        """
        result = []
        n = len(nums)  # Store length for efficiency

        def backtrack(current_path, used_numbers):
            # Alternative/Slightly more direct base case:
            # if len(current_path) == n:
            if sum(used_numbers) == n:  # Your original base case
                result.append(current_path.copy())
                return

            for i in range(n):  # Iterate using n
                if used_numbers[i] == 0:
                    current_path.append(nums[i])
                    used_numbers[i] = 1
                    backtrack(current_path, used_numbers)
                    # Backtrack
                    used_numbers[i] = 0
                    current_path.pop()

        backtrack([], [0] * n)  # Initialize used_numbers based on n
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_nums, expected_output_permutations)
# Note: Order of permutations in expected output doesn't matter for validation if checked correctly.
test_data = [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]]),
    (
        [],
        [[]],
    ),  # Edge case: empty input (though constraints say length >= 1) - good to consider
    ([1, 2], [[1, 2], [2, 1]]),
]

# Helper function to compare lists of lists irrespective of order
def assert_lists_equal_unordered(list1, list2):
    assert len(list1) == len(list2)
    # Convert inner lists to tuples to make them hashable for set comparison
    set1 = set(map(tuple, list1))
    set2 = set(map(tuple, list2))
    assert set1 == set2


@pytest.mark.parametrize("nums_input, expected", test_data)
def test_solution(nums_input, expected):
    solution = Solution()
    result = solution.permute(list(nums_input))  # Pass a copy if needed

    # Handle the empty list case specifically if necessary based on implementation
    if not nums_input and not expected:
        assert result == [[]] or result == []  # Depending on how empty case is handled
    elif not nums_input:
        assert result == [[]] or result == []
    else:
        assert_lists_equal_unordered(result, expected)
