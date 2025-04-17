"""
LeetCode Problem: 66 - Plus One
Link: https://leetcode.com/problems/plus-one/
Difficulty: Easy

Problem Description:
You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

Examples:
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Example 3:
Input: digits = [9]
Output: [1,0]

Constraints:
*   1 <= digits.length <= 100
*   0 <= digits[i] <= 9
*   digits does not contain any leading `0`'s.
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments a large integer represented by an array of digits by one.

        Approach:
        Simulates manual addition starting from the rightmost digit.
        1. Check the last digit: If it's less than 9, simply increment it and
           return the array immediately (common case optimization).
        2. Iterate from right-to-left: If the last digit was 9, iterate through
           the digits from the end towards the beginning.
        3. Handle Carry:
           - If adding 1 to the current digit results in 10, set the digit to 0
             and continue the loop to carry over the 1 to the next digit left.
           - If adding 1 does *not* result in 10, increment the digit and break
             the loop, as no further carry is needed.
        4. Handle All Nines Case: After the loop, if the loop index `i` reached 0
           *and* the first digit `digits[0]` is 0, it means the original number
           was composed entirely of nines. In this case, insert a leading 1
           at the beginning of the array.
        5. Return the modified `digits` array.

        Time Complexity: O(N) - In the worst case (all nines), we iterate through
                       all N digits once.
        Space Complexity: O(1) - The modification is done in-place. In the edge
                        case where a leading 1 is inserted, the list resizing
                        might internally take O(N), but we typically consider
                        the *extra* space used beyond input modification as O(1).

        Args:
            digits (List[int]): The array representing the large integer.

        Returns:
            List[int]: The array representing the incremented large integer.
        """
        # Your solution here
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        i = len(digits)
        while i > 0:
            i -= 1
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_digits, expected_output_digits)
test_data = [
    ([1, 2, 3], [1, 2, 4]),  # Example 1
    ([4, 3, 2, 1], [4, 3, 2, 2]),  # Example 2
    ([9], [1, 0]),  # Example 3
    ([1, 2, 9], [1, 3, 0]),  # Carry within the array
    ([9, 9, 9], [1, 0, 0, 0]),  # Carry resulting in larger array
    (
        [0],
        [1],
    ),  # Single zero (though constraints say no leading zeros, this might be tested)
    ([8, 9, 9, 9], [9, 0, 0, 0]),  # Carry stops mid-array
]


@pytest.mark.parametrize("digits_input, expected", test_data)
def test_solution(digits_input, expected):
    solution = Solution()
    result = solution.plusOne(list(digits_input))  # Pass a copy
    assert result == expected
