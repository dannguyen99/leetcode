"""
LeetCode Problem: 5 - Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Difficulty: Medium

Problem Description:
Given a string `s`, return the longest palindromic substring in `s`.

Examples:
Example 1: Input: s = "babad" Output: "bab" (or "aba")
Example 2: Input: s = "cbbd" Output: "bb"

Constraints:
*   1 <= s.length <= 1000
*   s consists of only digits and English letters.
"""
import pytest

# Solution Class - Implement the logic here
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach:
        [Explain your approach here - e.g., Expand Around Center, Dynamic Programming Table]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            s (str): The input string.

        Returns:
            str: The longest palindromic substring found in s.
        """
        # Your solution here
        input_length = len(s)
        current_max = s[0]
        for i in range(input_length - 1):
            positions = [i]
            if s[i] == s[i + 1]:
                positions.append(i + 1)
            for position in positions:
                j = 0
                while (
                    i - j - 1 >= 0
                    and position + j + 1 < input_length
                    and s[i - j - 1] == s[position + j + 1]
                ):
                    j += 1
                current_max = (
                    s[i - j : position + j + 1]
                    if len(current_max) < len(s[i - j : position + j + 1])
                    else current_max
                )
        return current_max


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_string, expected_output_substring) - Note: Multiple valid outputs possible
test_data = [
    ("babad", ["bab", "aba"]),  # Example 1 (multiple valid)
    ("cbbd", ["bb"]),  # Example 2
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("bb", ["bb"]),
    ("racecar", ["racecar"]),
    ("forgeeksskeegfor", ["geeksskeeg"]),
    ("abaxyzzyxf", ["xyzzyx"]),
    ("bananas", ["anana"]),
    ("ccc", ["ccc"]),
]


@pytest.mark.parametrize("s_input, expected_options", test_data)
def test_solution(s_input, expected_options):
    solution = Solution()
    result = solution.longestPalindrome(s_input)
    assert result in expected_options
    # Check if the result is indeed a palindrome
    assert result == result[::-1]
    # Verify it's the longest possible among the options for this input
    max_len = 0
    for option in expected_options:
        max_len = max(max_len, len(option))
    assert len(result) == max_len
