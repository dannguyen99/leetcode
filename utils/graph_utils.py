# --- File: utils/graph_utils.py ---

from typing import List, Optional, Dict
from collections import deque

# Definition for a Graph Node (Use consistently)
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    # Optional: Add a __repr__ for easier debugging if needed
    def __repr__(self):
        # Shows value and neighbor values for quick inspection
        neighbor_vals = sorted([n.val for n in self.neighbors])
        return f"Node({self.val}, neighbors={neighbor_vals})"


# Helper function to build a graph from an adjacency list (1-indexed assumption based on LC format)
def build_graph(adjList: List[List[int]]) -> Optional[Node]:
    """
    Builds a graph from an adjacency list representation.
    Assumes nodes are valued 1 to n corresponding to list indices 0 to n-1.

    Args:
        adjList: A list of lists where adjList[i] contains the neighbors of node i+1.

    Returns:
        The Node object corresponding to value 1, or None if the graph is empty.
    """
    if not adjList:
        return None

    nodes: Dict[int, Node] = {}  # Using a dictionary to map value to Node object

    # First pass: Create all nodes
    for i in range(len(adjList)):
        node_val = i + 1
        if node_val not in nodes:
            nodes[node_val] = Node(node_val)

        # Also create neighbor nodes if they don't exist yet based on adjList entry
        for neighbor_val in adjList[i]:
            if neighbor_val not in nodes:
                nodes[neighbor_val] = Node(neighbor_val)

    # Second pass: Add neighbors
    for i in range(len(adjList)):
        node_val = i + 1
        current_node = nodes[node_val]
        for neighbor_val in adjList[i]:
            # Check if neighbor is already added to prevent duplicates if adjList isn't perfectly clean
            if nodes[neighbor_val] not in current_node.neighbors:
                current_node.neighbors.append(nodes[neighbor_val])

    # Return the node with value 1 (as per LeetCode's usual starting point)
    # Handle the case where the list might be structured differently or node 1 doesn't exist
    return nodes.get(1, None)


# Helper function to convert a graph back to an adjacency list (for testing verification)
def graph_to_adjList(start_node: Optional[Node]) -> List[List[int]]:
    """
    Converts a graph (starting from a given node) back to an adjacency list representation.
    Performs a BFS to find all reachable nodes and their neighbors.
    Assumes nodes are valued 1 to n and generates a list of length n.

    Args:
        start_node: The starting node to explore the graph from.

    Returns:
        An adjacency list representing the graph structure.
    """
    if not start_node:
        return []

    adj: Dict[int, List[int]] = {}  # Store adjacency list {node_val: [neighbor_vals]}
    queue = deque([start_node])
    visited = {start_node}  # Keep track of visited nodes (objects) to handle cycles
    max_val = 0

    while queue:
        node = queue.popleft()
        max_val = max(max_val, node.val)  # Track highest node value found

        # Store neighbors sorted for consistent test output
        adj[node.val] = sorted([n.val for n in node.neighbors])

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Build the final list, ensuring entries for all nodes from 1 to max_val
    resultList = []
    for i in range(1, max_val + 1):
        resultList.append(
            adj.get(i, [])
        )  # Use empty list if a node had no neighbors or wasn't reachable (though problem says connected)

    # Handle case where only node 1 exists with no neighbours explicitly if needed
    if max_val == 1 and 1 not in adj:
        return [[]]

    return resultList
