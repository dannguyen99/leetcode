"""
LeetCode Problem: 322 - Coin Change
Link: https://leetcode.com/problems/coin-change/
Difficulty: Medium

Problem Description:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
import pytest
from typing import List, Optional  # Keep Optional just in case, List is needed

# Solution Class - Implement the logic here
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach:
        Uses bottom-up Dynamic Programming. Creates a `dp` array (`min_coins`)
        where `dp[i]` stores the minimum number of coins needed to make amount `i`.
        The array is initialized with -1 (representing impossible).
        Initializes `dp[c] = 1` for amounts `c` that match a coin denomination.
        Iterates from the smallest coin value up to the target `amount`. For each
        amount `i`, it checks all coins `c`. If the subproblem `dp[i-c]` is solvable
        (value > 0), it updates `dp[i]` with the minimum value found so far,
        calculated as `1 + dp[i-c]`. The final answer is `dp[amount]`.

        Time Complexity: O(A * N) - Where A is the target amount and N is the number
                         of coin denominations. The nested loops dominate: the outer
                         loop runs ~A times, and the inner loop runs N times.
        Space Complexity: O(A) - Required for the `dp` array (`min_coins`) to store
                          results for amounts from 0 to A.

        Args:
            coins (List[int]): A list of available coin denominations.
            amount (int): The target amount of money.

        Returns:
            int: The fewest number of coins needed to make up the amount,
                 or -1 if it's impossible.
        """
        # --- Handle edge cases ---
        if amount == 0:
            return 0  # No coins needed for amount 0
        if not coins:
            return -1  # Cannot make any amount without coins
        # Optimization: If smallest coin > amount, it's impossible
        if min(coins) > amount:
            return -1

        # Optimization: Remove coins larger than the target amount
        coins = list(filter(lambda c: c <= amount, coins))
        if not coins:  # Check again in case all coins were too large
            return -1

        # Initialize dp table: dp[i] = min coins for amount i. -1 means impossible/not computed.
        min_coins = [-1] * (amount + 1)

        # Initialize amounts matching a coin denomination to 1 (potential seed/optimization)
        # Note: Standard DP usually only sets dp[0]=0.
        for c in coins:
            min_coins[c] = 1

        # Iterate through all amounts from smallest coin value up to target amount
        # Note: Standard DP often starts from 1. Starting from min(coins) is an optimization.
        for i in range(min(coins), amount + 1):
            # Optimization: If already found a solution (potentially the initial dp[c]=1), skip redundant checks?
            # (Caution: This skip might be risky if the initial dp[c]=1 wasn't optimal, but worked for tests)
            if min_coins[i] > 0:
                continue

            # Try subtracting each coin `c` to see if we can reach amount `i`
            for c in coins:
                # Check if the remaining amount `i-c` is valid
                if i - c < 0:
                    continue  # Cannot use coin `c` if it's larger than current amount `i`

                # Check if the subproblem `dp[i-c]` was solvable
                if min_coins[i - c] > 0:
                    # Calculate potential new minimum for amount `i`
                    current_path_count = min_coins[i - c] + 1

                    # If `dp[i]` hasn't been set (-1) or the new path is better
                    if min_coins[i] == -1 or min_coins[i] > current_path_count:
                        min_coins[
                            i
                        ] = current_path_count  # Update with the better minimum

        # Return the calculated minimum coins for the target amount
        return min_coins[amount]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (coins_list, amount_target, expected_output)
test_data = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([186, 419, 83, 408], 6249, 20),  # A slightly more complex case
    ([], 1, -1),  # Edge case: no coins
    (
        [1, 2, 5],
        -1,
        -1,
    ),  # Edge case: negative amount (based on constraints amount >= 0, but good to consider)
    # The actual expected output for amount=0 is 0 per Example 3, negative amount test case may need adjustment or clarification based on assumptions.
    # Let's stick to constraint examples for now.
]

# Adjusting test data based on constraints (amount >= 0)
test_data = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([186, 419, 83, 408], 6249, 20),
    ([], 1, -1),  # No coins to make amount 1
    ([], 0, 0),  # No coins needed to make amount 0
    ([102, 220, 186, 465, 336, 107, 387, 418], 495, -1),
]


# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("coins, amount, expected", test_data)
def test_solution(coins: List[int], amount: int, expected: int):
    solution = Solution()
    result = solution.coinChange(coins, amount)
    assert result == expected
