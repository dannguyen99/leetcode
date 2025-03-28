# --- File: 3_longest_substring_without_repeating_characters.py ---

"""
LeetCode Problem: 3 - Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""
import pytest
from typing import List  # Keep for template consistency, though not used in signature


# Solution Class - Implement the logic here
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach:
        Use a sliding window with two pointers (left, right) and a hash map `seen`
        to store the last seen index of each character ({char: index}).
        The window `s[left...right-1]` contains the current substring candidate.
        Expand the window by incrementing `right`. If `s[right]` is a character
        already in `seen` and its last occurrence is within the current window
        (`seen[s[right]] >= left`), slide the `left` pointer forward past that
        last occurrence. Update max length and the character's last seen index.
        An early stopping condition `max_len < len(s) - left` is used in the loop.

        Time Complexity: O(N) - Each character is visited by `left` and `right` pointers at most once.
        Space Complexity: O(min(N, M)) - Where N is the length of the string and M is the
                         size of the character set. The hash map stores at most M distinct characters.
                         Often simplified to O(1) if M is considered constant.

        Args:
            s: str - The input string.

        Returns:
            int - The length of the longest substring without repeating characters.
        """
        # Your solution here
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        seen = {s[0]: 0}
        max_len = 1
        while max_len < len(s) - left:
            if s[right] in seen and left <= seen[s[right]]:
                left = seen[s[right]] + 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
            seen[s[right]] = right
            right += 1
        return max_len


# --- Test Section ---

# Define test cases as a list of tuples: (input_string, expected_length)
test_data = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),  # Empty string
    (" ", 1),  # String with a single space
    ("au", 2),  # No repeats
    ("dvdf", 3),  # Example: "vdf"
    ("anviaj", 5),  # Example: "nviaj"
]


# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("input_string, expected_length", test_data)
def test_lengthOfLongestSubstring(input_string: str, expected_length: int):
    solution = Solution()
    result = solution.lengthOfLongestSubstring(input_string)
    assert result == expected_length
