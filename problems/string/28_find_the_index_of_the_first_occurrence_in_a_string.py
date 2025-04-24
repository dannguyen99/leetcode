"""
LeetCode Problem: 28 - Find the Index of the First Occurrence in a String
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy

Problem Description:
Given two strings `needle` and `haystack`, return the index of the first occurrence of
`needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

Examples:
Example 1: Input: haystack = "sadbutsad", needle = "sad" Output: 0
Example 2: Input: haystack = "leetcode", needle = "leeto" Output: -1

Constraints:
*   1 <= haystack.length, needle.length <= 10^4
*   haystack and needle consist of only lowercase English letters.
"""
import pytest

# Solution Class - Implement the logic here
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Approach:
        [Explain your approach here - e.g., Sliding Window, Built-in find]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            haystack (str): The string to search within.
            needle (str): The string to search for.

        Returns:
            int: The index of the first occurrence of needle in haystack, or -1.
        """
        # Your solution here
        if not needle or haystack == needle:
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and haystack[i : i + len(needle)] == needle:
                return i
        return -1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_haystack, input_needle, expected_output_index)
test_data = [
    ("sadbutsad", "sad", 0),  # Example 1
    ("leetcode", "leeto", -1),  # Example 2
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("mississippi", "issip", 4),
    ("mississippi", "mississippi", 0),  # Needle equals haystack
    ("abc", "c", 2),
    ("abc", "a", 0),
    ("a", "a", 0),
    (
        "",
        "a",
        -1,
    ),  # Empty haystack (based on constraints, len >= 1, but good edge case)
    ("a", "", 0),  # Empty needle (standard behavior is index 0)
    ("", "", 0),  # Both empty
]


@pytest.mark.parametrize("haystack_input, needle_input, expected", test_data)
def test_solution(haystack_input, needle_input, expected):
    solution = Solution()
    result = solution.strStr(haystack_input, needle_input)
    assert result == expected
