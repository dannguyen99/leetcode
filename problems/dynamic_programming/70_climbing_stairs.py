"""
LeetCode Problem: 70 - Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy

Problem Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
* 1 <= n <= 45
"""
import pytest

# Solution Class - Implement the logic here
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb a staircase of n steps,
        taking 1 or 2 steps at a time.

        Approach:
        Recognizes ways(n) = ways(n-1) + ways(n-2).
        Since calculating ways(i) only requires the results for ways(i-1) and ways(i-2),
        we only need to store the two most recent results instead of the entire DP table.
        Iteratively update these two variables.

        Time Complexity: O(n) - Single loop from 3 to n.
        Space Complexity: O(1) - Only uses a fixed number of variables.

        Args:
            n: The total number of steps in the staircase.

        Returns:
            int: The number of distinct ways to climb to the top.
        """
        # --- Implement your solution here ---
        if n <= 2:
            return n
        way_n2 = 1
        way_n1 = 2
        for _ in range(3, n + 1):
            way_n1, way_n2 = way_n2 + way_n1, way_n1
        return way_n1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_n, expected_ways)
test_data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89),  # Check for larger values
    (45, 1836311903),  # Max constraint
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("n, expected", test_data)
def test_solution(n, expected):
    solution = Solution()
    result = solution.climbStairs(n)
    assert result == expected


# You can add more specific test functions if needed
