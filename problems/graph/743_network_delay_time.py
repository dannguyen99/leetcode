"""
LeetCode Problem: 743 - Network Delay Time
Link: https://leetcode.com/problems/network-delay-time/
Difficulty: Medium

Problem Description:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Examples:
Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: The signal travels from node 2 to node 1 (1ms) and node 3 (1ms). Then node 3 sends to node 4 (1ms). The signal reaches node 4 at 1 + 1 = 2ms. This is the time it takes for all nodes to receive the signal.

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 1 is unreachable from node 2.

Constraints:
* 1 <= k <= n <= 100
* 1 <= times.length <= 6000
* times[i].length == 3
* 1 <= ui, vi <= n
* ui != vi
* 0 <= wi <= 100
* All the pairs (ui, vi) are unique. (i.e., no multiple edges between the same pair of nodes.)
"""

import pytest
import heapq  # For the priority queue (min-heap)
import math  # For float('inf')
from collections import defaultdict  # For adjacency list
from typing import List


# Solution Class - Implement the logic here
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calculates the minimum time for a signal starting from node k to reach all nodes.

        Approach:
        # 1. Build adjacency list (node -> list of (neighbor, weight))
        # 2. Initialize distances array/map (dist[k]=0, others=infinity)
        # 3. Initialize priority queue with (0, k)
        # 4. While priority queue is not empty:
        #    a. Extract node 'u' with minimum distance 'd'
        #    b. If d > current known distance to u, continue (already found shorter path)
        #    c. For each neighbor 'v' of 'u' with weight 'w':
        #       i. If d + w < distance[v]:
        #          - Update distance[v] = d + w
        #          - Push (distance[v], v) onto priority queue
        # 5. After loop, find max distance among all nodes. If any is infinity, return -1.

        Time Complexity: O(E log V)
        Space Complexity: O(V + E)

        Args:
            times: List of edges [u, v, w] representing travel time w from u to v.
            n: Total number of nodes (labeled 1 to n).
            k: The starting node (1-indexed).

        Returns:
            int: The minimum time for the signal to reach all nodes, or -1 if impossible.
        """
        # --- Implement your solution here ---
        # 1. Build adjacency list (node -> list of (neighbor, weight))
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append([target, time])
        # 2. Initialize distances array/map (dist[k]=0, others=infinity)
        dist = [math.inf] * n
        dist[k - 1] = 0
        # 3. Initialize priority queue with (0, k)
        heap = [(0, k)]
        # 4. While priority queue is not empty:
        while heap:
            #    a. Extract node 'u' with minimum distance 'd'
            d, u = heapq.heappop(heap)
            #    b. If d > current known distance to u, continue (already found shorter path)
            if d > dist[u - 1]:
                continue
            #    c. For each neighbor 'v' of 'u' with weight 'w':
            for v, w in adj[u]:
                # i. If d + w < distance[v]:
                if d + w < dist[v - 1]:
                    # - Update distance[v] = d + w
                    dist[v - 1] = d + w
                    # - Push (distance[v], v) onto priority queue
                    heapq.heappush(heap, (dist[v - 1], v))

        max_dist = max(dist)  # Find the longest shortest path
        return -1 if max_dist == math.inf else max_dist


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (times, n, k, expected_time)
test_data = [
    ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
    ([[1, 2, 1]], 2, 1, 1),
    ([[1, 2, 1]], 2, 2, -1),
    (
        [[1, 2, 1], [2, 3, 2], [1, 3, 4]],
        3,
        1,
        3,
    ),  # 1->2->3 (1+2=3) is shorter than 1->3 (4)
    ([[1, 2, 1], [2, 1, 3]], 2, 1, 1),  # Cycle doesn't prevent reaching nodes
    ([[1, 2, 1], [2, 3, 7], [1, 3, 4], [3, 4, 1]], 4, 1, 5),  # 1->3 (4) + 3->4 (1) = 5
]


# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("times, n, k, expected", test_data)
def test_solution(times, n, k, expected):
    solution = Solution()
    result = solution.networkDelayTime(times, n, k)
    assert result == expected


# You can add more specific test functions if needed
