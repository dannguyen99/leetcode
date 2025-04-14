"""
LeetCode Problem: 383 - Ransom Note
Link: https://leetcode.com/problems/ransom-note/
Difficulty: Easy

Problem Description:
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Examples:
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
* 1 <= ransomNote.length, magazine.length <= 10^5
* ransomNote and magazine consist of lowercase English letters.
"""
import pytest
from collections import Counter  # Counter is very useful here

# Solution Class - Implement the logic here
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if the ransomNote can be constructed from the letters in magazine.

        Approach:
        Use a character count map (implemented as a fixed-size array of 26).
        First, count the occurrences of each character in the magazine.
        Then, iterate through the ransomNote, decrementing the count for each
        required character. If a required character's count is already zero
        (meaning not available in sufficient quantity), return False.
        If the loop completes, return True.

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            ransomNote: The string to be constructed.
            magazine: The string containing available letters.

        Returns:
            bool: True if ransomNote can be constructed, False otherwise.
        """
        # --- Implement your solution here ---
        if len(ransomNote) > len(magazine):
            return False
        result = [0] * 26
        for i in magazine:
            result[ord(i) - ord("a")] += 1
        for i in ransomNote:
            position = ord(i) - ord("a")
            if result[position] - 1 < 0:
                return False
            result[position] -= 1
        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (ransomNote, magazine, expected_output)
test_data = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("aab", "baa", True),  # Order doesn't matter
    ("", "abc", True),  # Empty note is always possible
    ("abc", "", False),  # Empty magazine cannot construct non-empty note
    ("fihjjj", "hjibagacbhadfaefdjaeaefgi", False),
    ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("ransomNote, magazine, expected", test_data)
def test_solution(ransomNote, magazine, expected):
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    assert result == expected


# You can add more specific test functions if needed
