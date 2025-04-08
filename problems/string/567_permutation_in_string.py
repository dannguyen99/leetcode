"""
LeetCode Problem: 567 - Permutation in String
Link: https://leetcode.com/problems/permutation-in-string/description/
Difficulty: Medium

Problem Description:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Examples:
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
* 1 <= s1.length, s2.length <= 10^4
* s1 and s2 consist of lowercase English letters.
"""
import pytest
from collections import Counter  # Counter might be useful for frequency counts

# Solution Class - Implement the logic here
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1 as a substring.

        Approach:
        Use fix length array with 26 element to check for character count.
        Using a sliding windows of constant length to keep track of the count.
        If count met between sliding widows and s1, return True otherwise return False

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            s1: The string whose permutation is searched for.
            s2: The string to search within.

        Returns:
            bool: True if a permutation of s1 is found in s2, False otherwise.
        """
        # --- Implement your solution here ---
        len_1 = len(s1)
        len_2 = len(s2)
        if len_2 < len_1:
            return False

        def convert_to_count(s: str):
            str_key = [0] * 26
            # build the str_key for the string
            for char in s:
                str_key[ord(char) - ord("a")] += 1
            return str_key

        str_key_1 = convert_to_count(s1)
        str_key_window = convert_to_count(s2[:len_1])
        if str_key_1 == str_key_window:
            return True

        for i in range(len_2 - len_1):
            str_key_window[ord(s2[i]) - ord("a")] -= 1
            str_key_window[ord(s2[i + len_1]) - ord("a")] += 1
            if str_key_window == str_key_1:
                return True
        return False


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (s1, s2, expected_output)
test_data = [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("a", "ab", True),
    ("abc", "bbbca", True),
    ("adc", "dcda", True),
    ("hello", "ooolleoooleh", False),
    (
        "trinitrophenylmethylnitramine",
        "dinitrophenylhydrazinetrinitrophenylmethylnitramine",
        True,
    ),  # Long strings
    ("ab", "a", False),  # s2 shorter than s1
    ("aabc", "aaacb", True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("s1, s2, expected", test_data)
def test_solution(s1, s2, expected):
    solution = Solution()
    result = solution.checkInclusion(s1, s2)
    assert result == expected


# You can add more specific test functions if needed
