"""
LeetCode Problem: 125 - Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy

Problem Description:
A phrase is a palindrome if it reads the same forward and backward, ignoring cases, spaces,
and non-alphanumeric characters. Given a string s, return True if it is a palindrome and False otherwise.

Examples:
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists of printable ASCII characters.
"""

from typing import List
from utils.test_runner import run_tests


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach:
        [Filters the string to keep only alphanumeric characters, converts to lowercase,
         then checks if the resulting sequence is the same forwards and backwards.]

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            s: str - Input string

        Returns:
            bool - True if the input string is a palindrome, False otherwise
        """
        # Your solution here
        # Keep original string s
        i = 0
        j = len(s) - 1

        while i < j:  # Using < might be simpler than <=
            # 1. Move i forward past non-alphanumeric chars
            while i < j and not s[i].isalnum():
                i += 1

            # 2. Move j backward past non-alphanumeric chars
            while i < j and not s[j].isalnum():
                j -= 1

            # 3. Now, compare the alphanumeric characters (if i < j still)
            if s[i].lower() != s[j].lower():
                return False  # Found a mismatch

            # 4. Characters match, move pointers inwards
            i += 1
            j -= 1

        # If the loop finishes without returning False, it's a palindrome
        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (("A man, a plan, a canal: Panama",), True),
        (("race a car",), False),
        ((" ",), True),
        (("0P",), False),
    ]

    run_tests(solution.isPalindrome, test_cases)
