"""
LeetCode Problem: 242 - Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy

Problem Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Examples:
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

import pytest
from typing import Tuple


class Solution:
    # Using the standard LeetCode method name
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach:
        2 string must have the same length, else return false
        we could create a hashmap contains the count of each char in the first string, and iteratively
        reduce the count if the char appear in the second string
        if the char in the second string not in the hashmap, return false
        if the char in the second string exhaust the count, return false
        finally, return true if all check passed.

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            s: str - The first input string.
            t: str - The second input string.

        Returns:
            bool - True if t is an anagram of s, False otherwise.
        """
        # Your solution here
        if len(s) != len(t):
            return False

        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char not in char_count or char_count[char] - 1 < 0:
                return False
            char_count[char] -= 1
        return True


test_cases = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("a", "ab"), False),
    (("ab", "a"), False),
    (("aacc", "ccac"), False),  # Added tricky case
    (("listen", "silent"), True),
    (("aabb", "bbaa"), True),
]


@pytest.mark.parametrize("input_strings, expected_output", test_cases)
def test_isAnagram(input_strings: Tuple[str, str], expected_output: bool):
    solution = Solution()
    assert solution.isAnagram(*input_strings) == expected_output
