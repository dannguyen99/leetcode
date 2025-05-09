"""
LeetCode Problem: 22 - Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium

Problem Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach:
        The problem asks us to generate all combinations of well-formed parentheses given n pairs.
        This is a classic backtracking problem. We can build the string of parentheses character by character.
        At each step, we have two choices: add an open parenthesis '(' or a close parenthesis ')'.

        To ensure the parentheses are well-formed, we need to follow two rules:
        1. We can only add an open parenthesis if we haven't used up all `n` open parentheses.
        2. We can only add a close parenthesis if the number of close parentheses used so far is strictly less than the number of open parentheses used so far. This ensures we don't close a parenthesis that wasn't opened.
        3. The process stops and a valid combination is found when the length of the current string is `2 * n`.

        We use a helper function `backtrack(current_string, open_count, close_count)`:
        - `current_string`: The string built so far.
        - `open_count`: Number of '(' used.
        - `close_count`: Number of ')' used.

        Base Case:
        - If `len(current_string) == 2 * n`, we have a complete combination. Add it to the results and return.

        Recursive Steps:
        1. If `open_count < n`:
           - Add '(' to `current_string`.
           - Recursively call `backtrack` with `open_count + 1`.
           - Backtrack: Remove '(' from `current_string` (or pass new strings to avoid explicit removal).
        2. If `close_count < open_count`:
           - Add ')' to `current_string`.
           - Recursively call `backtrack` with `close_count + 1`.
           - Backtrack: Remove ')' from `current_string`.

        The initial call will be `backtrack("", 0, 0)`.

        Time Complexity: O((4^n) / (n * sqrt(n))) or O(n * C_n) where C_n is the n-th Catalan number.
                       Each valid sequence has length 2n. The number of valid sequences is C_n.
        Space Complexity: O(n) for the recursion stack depth (if not counting output).
                        The output itself takes O(n * C_n) space.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            List[str]: A list of all combinations of well-formed parentheses.
        """
        # Your solution here
        result = []
        # Helper function for backtracking
        def backtrack(current_string, open_count, close_count):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            if open_count < n:
                # Add open parenthesis
                backtrack(current_string + "(", open_count + 1, close_count)

            if close_count < open_count:
                # Add close parenthesis
                backtrack(current_string + ")", open_count, close_count + 1)
                current_string = current_string[
                    :-1
                ]  # Backtrack: undo the addition for this frame

        backtrack("", 0, 0)
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (n_input, expected_output)
test_data = [
    (
        3,
        sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ),  # Sort expected for consistent comparison
    (1, sorted(["()"])),
    (2, sorted(["(())", "()()"])),
    # Add more test cases if needed, e.g., n=0 (though constraint is 1 <= n)
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("n_input, expected", test_data)
def test_solution(n_input, expected):
    solution = Solution()
    result = solution.generateParenthesis(n_input)
    # Sort the result as the order of well-formed parentheses might not be guaranteed
    # by all valid solutions, but the set of parentheses should be the same.
    assert sorted(result) == expected
