"""
LeetCode Problem: 973 - K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/
Difficulty: Medium

Problem Description:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., sqrt(x1 - x2)^2 + (y1 - y2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Examples:
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
* 1 <= k <= points.length <= 10^4
* -10^4 <= xi, yi <= 10^4
"""
import pytest
import heapq  # Import the heapq module
import math  # Import math if you need sqrt (but maybe you don't!)
from typing import List

# Solution Class - Implement the logic here
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k points closest to the origin (0,0).

        Approach:
        Use min-heap to keep track of the square of distance to the origin and the point it self.
        The trick is to negate the square distance, so that instead of keeping the k largest, we can keep track of k smallest.

        Time Complexity: O(N logk)
        Space Complexity: O(k)

        Args:
            points: A list of points, where each point is [x, y].
            k: The number of closest points to return.

        Returns:
            List[List[int]]: The k closest points to the origin.
        """
        # --- Implement your solution here ---
        if len(points) == k:
            return points
        top_k = []
        for p in points:
            # keep the negative difference square for comparing
            distance_sqr = -(p[0] ** 2 + p[1] ** 2)
            if len(top_k) < k:
                heapq.heappush(top_k, (distance_sqr, p))
            elif distance_sqr > top_k[0][0]:
                heapq.heappushpop(top_k, (distance_sqr, p))
        return [p[1] for p in top_k]


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_points, k, expected_output_points)
# Note: Since output order doesn't matter, we'll sort both results for comparison
def sort_points(point_list):
    return sorted(point_list)


test_data = [
    ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ([[0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
    ([[1, 1], [1, 1]], 1, [[1, 1]]),  # Duplicate points
    ([[10, -2], [2, 3], [5, -1], [1, 1]], 3, [[1, 1], [2, 3], [5, -1]]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("points, k, expected", test_data)
def test_solution(points, k, expected):
    solution = Solution()
    result = solution.kClosest(points, k)
    # Sort both lists of points before comparison because order doesn't matter
    assert sort_points(result) == sort_points(expected)


# You can add more specific test functions if needed
