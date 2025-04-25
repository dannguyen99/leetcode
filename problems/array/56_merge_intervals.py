"""
LeetCode Problem: 56 - Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium

Problem Description:
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals,
and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

Examples:
Example 1: Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
Example 2: Input: intervals = [[1,4],[4,5]] Output: [[1,5]]

Constraints:
*   1 <= intervals.length <= 10^4
*   intervals[i].length == 2
*   0 <= start_i <= end_i <= 10^4
"""
import pytest
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach:
        Sort the intervals by the starting point.
        Initialize the start and end of the current examining interval
        Iterate through the sorted interval, at each iteration check:
        - If the start_i is larger than the current end, means we end the current interval and start a new one.
        - Else we only update the new end of the current interval appropriately.

        Time Complexity: O(N log N) - Sorted and iterate once
        Space Complexity: O(N) - List to store the result

        Args:
            intervals (List[List[int]]): A list of intervals [start, end].

        Returns:
            List[List[int]]: A list of merged, non-overlapping intervals.
        """
        # Your solution here
        if not intervals:
            return []
        result = []
        intervals.sort(key=lambda elements: elements[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for start_i, end_i in intervals:
            if start_i > end:
                result.append([start, end])
                start = start_i
            if end_i > end:
                end = end_i
        result.append([start, end])
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_intervals, expected_output_intervals)
# Note: Expected output should be sorted for consistent comparison.
test_data = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  # Example 1
    ([[1, 4], [4, 5]], [[1, 5]]),  # Example 2
    ([[1, 4], [0, 4]], [[0, 4]]),  # Overlap with earlier start
    ([[1, 4], [2, 3]], [[1, 4]]),  # Contained interval
    ([[1, 5], [2, 4]], [[1, 5]]),  # Contained interval 2
    ([[1, 4], [0, 1]], [[0, 4]]),  # Overlap at start
    ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),  # Non-overlapping before
    ([[1, 4]], [[1, 4]]),  # Single interval
    ([], []),  # Empty input
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),  # Merge all
    ([[1, 3], [3, 5], [5, 7]], [[1, 7]]),  # Touching intervals
]

# Helper to sort lists of lists for comparison
def sort_intervals(intervals: List[List[int]]) -> List[List[int]]:
    return sorted(intervals, key=lambda x: x[0])


@pytest.mark.parametrize("intervals_input, expected", test_data)
def test_solution(intervals_input, expected):
    solution = Solution()
    # Make a copy to avoid modifying the input list during sorting within the function
    intervals_copy = [list(interval) for interval in intervals_input]
    result = solution.merge(intervals_copy)
    # Sort the result and expected for consistent comparison
    sorted_result = sort_intervals(result)
    sorted_expected = sort_intervals(expected)
    assert sorted_result == sorted_expected
