# LeetCode Problem: 392 - Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
"""
Problem Description:
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative order of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

Examples:
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
*   `0 <= s.length <= 100`
*   `0 <= t.length <= 10^4`
*   `s` and `t` consist only of lowercase English letters.
"""

import pytest

# Solution Class - Implement the logic here
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Approach:
        [Explain your approach here]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            s: The potential subsequence string.
            t: The main string to check against.

        Returns:
            True if s is a subsequence of t, False otherwise.
        """
        # Your solution here
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (s, t, expected_output)
test_data = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),  # Empty string is always a subsequence
    ("abc", "", False),  # Non-empty string cannot be a subsequence of empty string
    ("", "", True),  # Empty string is a subsequence of empty string
    ("aaaaaa", "bbaaaa", False),  # Not enough 'a's in order
    ("ace", "abcde", True),
    ("ab", "ba", False),  # Order matters
    ("le", "yolo", False),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("s, t, expected", test_data)
def test_solution(s, t, expected):
    solution = Solution()
    result = solution.isSubsequence(s, t)
    assert result == expected
