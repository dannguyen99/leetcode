"""
LeetCode Problem: 205 - Isomorphic Strings
Link: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy

Problem Description:
Given two strings `s` and `t`, determine if they are isomorphic.
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Examples:
Example 1: Input: s = "egg", t = "add" Output: true
Example 2: Input: s = "foo", t = "bar" Output: false
Example 3: Input: s = "paper", t = "title" Output: true

Constraints:
*   1 <= s.length <= 5 * 10^4
*   t.length == s.length
*   s and t consist of any valid ascii character.
"""
import pytest

# Solution Class - Implement the logic here
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Approach:
        [Explain your approach here - e.g., Using Hash Maps to track mappings]

        Time Complexity: O(N) - check each character at most once
        Space Complexity: O(N)

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if s and t are isomorphic, False otherwise.
        """
        # Your solution here
        if len(s) != len(t):
            return False
        mapping = {}
        existed = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] == t[i]:
                    continue
                else:
                    return False
            if t[i] in existed:
                return False
            mapping[s[i]] = t[i]
            existed.add(t[i])

        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_s, input_t, expected_output)
test_data = [
    ("egg", "add", True),  # Example 1
    ("foo", "bar", False),  # Example 2
    ("paper", "title", True),  # Example 3
    ("badc", "baba", False),  # 'd' and 'c' cannot both map to 'a'
    ("abab", "cdcd", True),
    ("aaeaa", "uuxyy", False),  # 'a' maps to 'u' then tries to map to 'x'
    (
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyz",
        True,
    ),  # Long identical
    ("13", "42", True),
    ("bbbaaaba", "aaabbbba", False)
    # Add more edge cases if needed
]


@pytest.mark.parametrize("s_input, t_input, expected", test_data)
def test_solution(s_input, t_input, expected):
    solution = Solution()
    result = solution.isIsomorphic(s_input, t_input)
    assert result == expected
