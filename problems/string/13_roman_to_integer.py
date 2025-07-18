# LeetCode Problem: 13 - Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
"""
Problem Description: [See above]
"""

import pytest

# Solution Class - Implement the logic here
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Approach:
        [Explain your approach here]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            s: A string representing a valid Roman numeral.

        Returns:
            The integer equivalent of the Roman numeral.
        """
        # Your solution here
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = symbols[s[0]]
        for i in range(1, len(s)):
            result += symbols[s[i]]
            if symbols[s[i - 1]] < symbols[s[i]]:
                result -= 2 * symbols[s[i - 1]]
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_string, expected_output)
test_data = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("IV", 4),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),
    ("I", 1),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("s_input, expected", test_data)
def test_solution(s_input, expected):
    solution = Solution()
    result = solution.romanToInt(s_input)
    assert result == expected
