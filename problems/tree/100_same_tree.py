"""
LeetCode Problem: 100 - Same Tree
Link: https://leetcode.com/problems/same-tree/
Difficulty: Easy

Problem Description:
Given the roots of two binary trees, p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Examples:
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
* The number of nodes in both trees is in the range [0, 100].
* -10^4 <= Node.val <= 10^4
"""
import pytest
from typing import Optional

# Import from the utility file
from utils.tree_utils import (
    TreeNode,
    create_binary_tree,
)  # Assuming tree_utils.py exists

# Solution Class - Implement the logic here
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are structurally identical and have the same node values.

        Approach:
        Recursion
        - Base case:
        - If 2 nodes are None, they are considered the same (structurally identical here). Return True.
        - If only one node is None (but not both), the structures differ. Return False.
        - If both nodes exist, check their value equality AND recursively check
          if their left subtrees are the same AND if their right subtrees are the same.

        Time Complexity: O(N) - Visits each node in both trees at most once (N = min(nodes in p, nodes in q)).
        Space Complexity: O(H) - Recursion call stack depth (H = height of the tree, worst case N).

        Args:
            p: The root node of the first binary tree.
            q: The root node of the second binary tree.

        Returns:
            bool: True if the trees are the same, False otherwise.
        """
        # --- Implement your solution here ---
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_p_list, input_q_list, expected_output)
test_data = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([], [], True),  # Both empty
    ([1], [1], True),  # Single node, same value
    ([1], [2], False),  # Single node, different value
    ([1, 2], [1, 2], True),
    ([1, None, 2], [1, None, 2], True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("p_list, q_list, expected", test_data)
def test_solution(p_list, q_list, expected):
    solution = Solution()
    p_root = create_binary_tree(p_list)
    q_root = create_binary_tree(q_list)
    result = solution.isSameTree(p_root, q_root)
    assert result == expected


# You can add more specific test functions if needed
