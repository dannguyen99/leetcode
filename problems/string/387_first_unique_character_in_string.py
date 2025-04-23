"""
LeetCode Problem: 387 - First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy

Problem Description:
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Examples:
Example 1: Input: s = "leetcode" Output: 0
Example 2: Input: s = "loveleetcode" Output: 2
Example 3: Input: s = "aabb" Output: -1

Constraints:
*   1 <= s.length <= 10^5
*   s consists of only lowercase English letters.
"""
import pytest
from collections import Counter  # Could be useful

# Solution Class - Implement the logic here
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Approach:
        1. Count character frequencies using collections.Counter.
        2. Iterate through the string again from the beginning.
        3. Return the index of the first character found with a count of 1.
        4. If the loop finishes, return -1.

        Time Complexity: O(N) - Two passes through the string (one for Counter, one for check).
        Space Complexity: O(1) - Counter stores at most 26 characters.

        Args:
            s (str): The input string.

        Returns:
            int: The index of the first unique character, or -1 if none exists.
        """
        # Your solution here
        count = Counter(s)
        if 1 not in count.values():
            return -1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_s, expected_output_index)
test_data = [
    ("leetcode", 0),  # Example 1
    ("loveleetcode", 2),  # Example 2
    ("aabb", -1),  # Example 3
    ("z", 0),  # Single character
    ("aadadaad", -1),  # All repeating
    ("dddccdbba", 8),  # Last character is unique
    ("cc", -1),
]


@pytest.mark.parametrize("s_input, expected", test_data)
def test_solution(s_input, expected):
    solution = Solution()
    result = solution.firstUniqChar(s_input)
    assert result == expected
