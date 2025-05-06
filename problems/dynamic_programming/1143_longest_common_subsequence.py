"""
LeetCode Problem: 1143 - Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/
Difficulty: Medium

Problem Description:
Given two strings `text1` and `text2`, return the length of their longest common subsequence (LCS).
A subsequence is formed by deleting zero or more characters without changing the order of the rest.

Examples:
Example 1: text1 = "abcde", text2 = "ace" -> Output: 3 ("ace")
Example 2: text1 = "abc", text2 = "abc" -> Output: 3 ("abc")
Example 3: text1 = "abc", text2 = "def" -> Output: 0

Constraints:
*   1 <= text1.length, text2.length <= 1000
*   text1, text2 consist of lowercase English characters.
"""
import pytest

# Solution Class - Implement the logic here
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Approach: Dynamic Programming
        We use a 2D DP table, `dp[i][j]`, to store the length of the longest
        common subsequence between the first `i` characters of `text1` (i.e., `text1[0...i-1]`)
        and the first `j` characters of `text2` (i.e., `text2[0...j-1]`).

        The table is 1-indexed for convenience, so `dp` has dimensions `(len(text1)+1) x (len(text2)+1)`.
        `dp[0][...]` and `dp[...][0]` are initialized to 0, representing the LCS with an empty string.

        Recurrence Relation:
        For `i` from 1 to `len(text1)` and `j` from 1 to `len(text2)`:
        1. If `text1[i-1] == text2[j-1]` (current characters match):
           The LCS includes this character. So, `dp[i][j] = 1 + dp[i-1][j-1]`.
        2. If `text1[i-1] != text2[j-1]` (current characters do not match):
           The LCS is the longest of the LCS formed by either excluding the current
           character of `text1` or excluding the current character of `text2`.
           So, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

        The final answer is `dp[len(text1)][len(text2)]`.

        Time Complexity: O(M * N) where M = len(text1), N = len(text2), as we fill each cell of the DP table once.
        Space Complexity: O(M * N) for the DP table. (Can be optimized to O(min(M, N)))

        Args:
            text1 (str): The first string.
            text2 (str): The second string.

        Returns:
            int: The length of the longest common subsequence.
        """
        len1, len2 = len(text1), len(text2)

        # Ensure text2 is the shorter string for space optimization, if desired.
        # This step is optional but makes the explanation of using len2 for dp array size simpler.
        if len1 < len2:
            return self.longestCommonSubsequence(
                text2, text1
            )  # Recurse with swapped strings

        # dp array will store results for the current row being processed for text1
        # prev_dp array will store results for the previous row of text1
        # Size is len2 + 1 because text2 is now guaranteed to be the shorter (or equal length) string
        prev_dp = [0] * (len2 + 1)
        current_dp = [0] * (len2 + 1)

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    current_dp[j] = prev_dp[j - 1] + 1
                else:
                    current_dp[j] = max(prev_dp[j], current_dp[j - 1])
            # After processing all columns for row i of text1,
            # current_dp becomes prev_dp for the next iteration.
            # Important: copy the values, not the reference.
            prev_dp = current_dp[:]  # or prev_dp = list(current_dp)

        return prev_dp[
            len2
        ]  # The last element of prev_dp (which was the last current_dp)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_text1, input_text2, expected_length)
test_data = [
    ("abcde", "ace", 3),  # Example 1
    ("abc", "abc", 3),  # Example 2
    ("abc", "def", 0),  # Example 3
    ("ezupkr", "ubmrapg", 2),  # LCS is "ur"
    ("bsbininm", "jmjkbkjkv", 1),  # LCS is "b" or "k" or "j"
    ("abcba", "abcbcba", 5),  # LCS is "abcba"
    ("aaaaaaaaaa", "aaaaa", 5),
    ("a", "b", 0),
    ("a", "a", 1),
]


@pytest.mark.parametrize("text1_input, text2_input, expected", test_data)
def test_solution(text1_input, text2_input, expected):
    solution = Solution()
    result = solution.longestCommonSubsequence(text1_input, text2_input)
    assert result == expected
