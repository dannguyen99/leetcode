# --- File: utils/tree_utils.py ---

from typing import Optional, List, Deque
from collections import deque

# Definition for a binary tree node (Use consistently)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Optional: Add a __repr__ for easier debugging/printing if needed
    def __repr__(self):
        # Simple representation, could be expanded (e.g., showing children)
        return f"TreeNode({self.val})"


# Helper function to create a binary tree from a Python list (Level Order)
# Mimics LeetCode's list representation for test cases.
def create_binary_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Creates a binary tree from a list of values using level-order traversal.
    `None` values in the list represent missing nodes at that level position.

    Args:
        nodes: A list where elements represent node values level by level,
               left-to-right. `None` indicates an absent child node.

    Returns:
        The root node of the created binary tree, or None if the list is empty
        or the first element is None.
    """
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue: Deque[TreeNode] = deque([root])
    i = 1  # Index for the next node value in the list

    while queue and i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if i < len(nodes):
            left_val = nodes[i]
            if left_val is not None:
                left_child = TreeNode(left_val)
                current_node.left = left_child
                queue.append(left_child)
            i += 1  # Move to the next value even if it was None

        # Process right child
        if i < len(nodes):
            right_val = nodes[i]
            if right_val is not None:
                right_child = TreeNode(right_val)
                current_node.right = right_child
                queue.append(right_child)
            i += 1  # Move to the next value even if it was None

    return root


# Helper function to convert a binary tree back to a Python list (Level Order)
# Useful for verifying test case outputs against LeetCode's format.
def tree_to_level_order_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Converts a binary tree back into a list representation using level-order
    traversal, including `None` for missing nodes, mirroring the input format
    of `create_binary_tree`.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of node values (or None) in level order. Trailing `None` values
        that represent empty spots after the last actual node might be included
        depending on the tree structure. A more sophisticated version could trim
        these, but this is often sufficient for test comparison.
        Returns an empty list for an empty tree.
    """
    if not root:
        return []

    output: List[Optional[int]] = []
    queue: Deque[Optional[TreeNode]] = deque([root])

    while queue:
        # Count nodes at the current level to know when to stop adding Nones
        level_node_count = len(queue)
        if all(node is None for node in queue):  # Stop if the whole level is None
            break

        for _ in range(level_node_count):
            node = queue.popleft()

            if node:
                output.append(node.val)
                # Add children to the queue, even if they are None
                queue.append(node.left)
                queue.append(node.right)
            else:
                output.append(None)  # Append None for null nodes encountered

    # Optional: Trim trailing Nones for a cleaner list matching LeetCode examples sometimes
    while output and output[-1] is None:
        output.pop()

    return output
