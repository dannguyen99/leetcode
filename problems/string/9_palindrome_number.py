"""
LeetCode Problem: 9 - Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy

Problem Description:
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
- -2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""
import pytest
from typing import List, Optional  # Not strictly needed here, but good habit

# Solution Class - Implement the logic here
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Approach:
        [Explain your approach here - e.g., String conversion, Reversing half the number]

        Time Complexity: O(log10(n)) - Number of digits in n. String conversion might be O(log10(n)) or O(n) depending on how string length is defined relative to the number's value.
        Space Complexity: O(1) if solving without string conversion. O(log10(n)) if converting to string.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        # --- Approach 1: String Conversion (Easiest) ---
        # Convert to string
        # return str(x) == str(x)[::-1]

        # --- Approach 2: Reversing the Number (Math) ---
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10

    def isPalindromeDiv(self, x: int) -> bool:
        # --- Approach 1 Modified: Math Two Pointers ---

        # Handle negative numbers and numbers ending in 0 (but not 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True  # Base case for 0

        # Calculate the divisor to get the most significant digit
        divisor = 1
        while x // divisor >= 10:  # Find the correct power of 10
            divisor *= 10

        while x > 0:
            # Get the most significant digit
            msd = x // divisor

            # Get the least significant digit
            lsd = x % 10

            # If digits don't match, it's not a palindrome
            if msd != lsd:
                return False

            # Remove the most significant digit and the least significant digit
            # 1. Remove MSD part using modulo
            # 2. Remove LSD part using integer division
            x = (x % divisor) // 10

            # Update the divisor since we removed two digits (one from each end)
            # Integer division is important here
            divisor //= 100

            # Optional: Optimization break if divisor becomes 0 before x does
            # (e.g., if x becomes single digit and divisor becomes < 1)
            # The `while x > 0` condition usually handles this naturally.

        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_x, expected_output)
test_data = [
    (121, True),  # Example 1
    (-121, False),  # Example 2
    (10, False),  # Example 3
    (0, True),  # Single digit 0
    (5, True),  # Single digit non-zero
    (1221, True),  # Even number of digits palindrome
    (1234, False),  # Non-palindrome
    (-101, False),  # Negative
    (100, False),  # Ends in 0 but isn't 0
    (100001, True),
    (1000021, False),
    (999, True),  # Ends in 1
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("x, expected", test_data)
def test_solution(x, expected):
    solution = Solution()
    result = solution.isPalindromeDiv(x)
    assert result == expected
