"""
LeetCode Problem: 20 - Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Problem Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""
import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach:
        Use a stack (implemented with a list) to keep track of open brackets.
        Iterate through the string:
        - If an open bracket is found, push it onto the stack.
        - If a closing bracket is found, check if the stack is non-empty and
          if the top of the stack is the corresponding opening bracket.
          If yes, pop the stack. If no, the string is invalid.
        After iterating, the stack must be empty for the string to be valid.

        Time Complexity: O(N) - We iterate through the string once. Stack operations are O(1).
        Space Complexity: O(N) - In the worst case (e.g., "((("), the stack stores all N characters.

        Args:
            s: str - The input string containing parentheses.

        Returns:
            bool - True if the string is valid, False otherwise.
        """
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        # Use a list as a stack to store open brackets
        stack = []

        for char in s:
            # If the character is an opening bracket, push it onto the stack.
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracket_map:
                # Check if stack is empty (no matching opener) OR
                # if the top of the stack doesn't match the expected opener.
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # If checks pass, it's a valid match, pop the opener.
                stack.pop()
            # Optional: Handle characters that are not brackets (if constraints allowed)
            # else: return False # Or ignore, depending on requirements

        # After the loop, the stack must be empty for the string to be valid.
        # If any open brackets remain, they were not closed.
        return not stack  # Returns True if stack is empty, False otherwise


test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("]", False),
    ("", True),
    ("{", False),
    ("((", False),
    ("){", False),
]


@pytest.mark.parametrize("input_string, expected_output", test_cases)
def test_isValid(input_string: str, expected_output: bool):
    solution = Solution()
    assert solution.isValid(input_string) == expected_output
