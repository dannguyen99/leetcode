"""
LeetCode Problem: 133 - Clone Graph
Link: https://leetcode.com/problems/clone-graph/
Difficulty: Medium

Problem Description:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists representing the connections of nodes. For example, [[2,4],[1,3],[2,4],[1,3]] means the graph has 4 nodes:
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Examples:
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: Node 1's value is 1, and it has neighbors 2 and 4. Node 2's value is 2, and it has neighbors 1 and 3. etc.

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Graph consists of only one node with val = 1 and no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: Graph is empty.

Constraints:
* The number of nodes in the graph is in the range [0, 100].
* 1 <= Node.val <= 100
* Node.val is unique for each node.
* There are no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.
"""
import pytest
from typing import Optional

from utils.graph_utils import Node, build_graph, graph_to_adjList  # For BFS

# Solution Class - Implement the logic here
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Creates a deep copy of a connected undirected graph.

        Approach:
        [Explain your approach here - e.g., DFS/BFS with hash map for visited/cloned nodes]

        Time Complexity: O(N + E) - Where N is the number of nodes and E is the number of edges.
        Each node is visited once (due to the visited_map), and each edge is considered once when processing neighbors.
        Space Complexity: O(N)

        Args:
            node: A reference to any node in the connected undirected graph.

        Returns:
            Optional['Node']: The reference to the corresponding node in the cloned graph.
        """
        # --- Implement your solution here ---
        # Often needs a hash map to store {original_node: cloned_node}
        visited_map = {}

        def dfs_clone(original_node: Node):
            if not original_node:
                return None
            if original_node in visited_map:
                return visited_map[original_node]
            clone_node = Node(val=original_node.val)

            visited_map[original_node] = clone_node

            if original_node.neighbors:
                for n in original_node.neighbors:
                    clone_node.neighbors.append(dfs_clone(original_node=n))
            return clone_node

        return dfs_clone(original_node=node)

        # def bfs_clone(original_node): ...


# --- Test Section ---
# Define test cases as a list of tuples
# Format: (input_adjList, expected_adjList)
test_data = [
    ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
    ([[]], [[]]),
    ([], []),
    ([[2], [1]], [[2], [1]]),  # Two nodes connected
]


@pytest.mark.parametrize("adjList, expectedAdjList", test_data)
def test_solution(adjList, expectedAdjList):
    solution = Solution()
    original_node = build_graph(adjList)
    cloned_node = solution.cloneGraph(original_node)

    # Important check: Ensure cloned node is not the same object as original (deep copy)
    if original_node:
        assert cloned_node is not original_node

    resultAdjList = graph_to_adjList(cloned_node)
    assert resultAdjList == expectedAdjList


# Add more specific tests if needed, e.g., testing neighbor objects identity
