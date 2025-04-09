"""
LeetCode Problem: 121 - Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
* 1 <= prices.length <= 10^5
* 0 <= prices[i] <= 10^4
"""
import pytest
from typing import List
import math  # May need math.inf

# Solution Class - Implement the logic here
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from a single buy and sell transaction.

        Approach:
        Keep track of the potential profit by keeping track of only the lowest initial price.
        Update the max profit accordingly based on the potential profit.

        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            prices: A list of stock prices on consecutive days.

        Returns:
            int: The maximum achievable profit.
        """
        # --- Implement your solution here ---
        max_profit = 0
        initial_price = prices[0]
        for p in prices[1:]:
            potential_profit = p - initial_price
            if potential_profit > max_profit:
                max_profit = potential_profit
            if p < initial_price:
                initial_price = p
        return max_profit


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_prices, expected_max_profit)
test_data = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([2, 4, 1], 2),  # Buy at 2, sell at 4
    ([3, 2, 6, 5, 0, 3], 4),  # Buy at 2, sell at 6
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("prices, expected", test_data)
def test_solution(prices, expected):
    solution = Solution()
    result = solution.maxProfit(prices)
    assert result == expected


# You can add more specific test functions if needed
