# LeetCode Problem: 409 - Longest Palindrome
# Link: https://leetcode.com/problems/longest-palindrome/
# Difficulty: Easy
"""
Problem Description:
Given a string `s` which consists of lowercase or uppercase English letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, `"Aa"` is not considered a palindrome here.

Examples:
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd". Its length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2

Constraints:
*   `1 <= s.length <= 2000`
*   `s` consists of lowercase and/or uppercase English letters.
"""

from collections import Counter
import pytest

# Solution Class - Implement the logic here
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Approach:
        [Explain your approach here]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            s: The input string.

        Returns:
            The length of the longest palindrome that can be built from s.
        """
        # Your solution here
        count_char = Counter(s)
        result = 0
        odd = False
        for val in count_char.values():
            if val % 2 == 0:
                result += val
            else:
                odd = True
                result += val - 1

        return result + 1 if odd else result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (s_input, expected_output)
test_data = [
    ("abccccdd", 7),
    ("a", 1),
    ("bb", 2),
    ("racecar", 7),  # All characters used
    ("aabbcc", 6),  # All characters have even counts
    ("Aa", 1),  # Case-sensitive
    ("bananas", 5),  # "anana"
    ("ab", 1),  # "a" or "b"
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("s_input, expected", test_data)
def test_solution(s_input, expected):
    solution = Solution()
    result = solution.longestPalindrome(s_input)
    assert result == expected
