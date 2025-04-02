"""
LeetCode Problem: 101 - Symmetric Tree
Link: https://leetcode.com/problems/symmetric-tree/
Difficulty: Easy

Problem Description:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Examples:
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
* The number of nodes in the tree is in the range [1, 1000].
* -100 <= Node.val <= 100
"""
import pytest
from typing import Optional
from collections import deque  # May be useful for iterative approach

# Import from the utility file
from utils.tree_utils import TreeNode, create_binary_tree

# Solution Class - Implement the logic here
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if a binary tree is symmetric around its center.

        Approach:
        [Explain your approach here - e.g., Recursive comparison, Iterative comparison]

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """
        # --- Implement your solution here ---
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    # --- Helper methods if needed (e.g., for recursion) ---
    def isMirror(
        self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]
    ) -> bool:
        # 1. Base Case: Both nodes are None (Symmetric)
        if not left_node and not right_node:
            return True
        # 2. Base Case: One node is None, the other isn't (Asymmetric)
        if not left_node or not right_node:
            return False
        # 3. Recursive Step: Both nodes exist
        return (
            left_node.val == right_node.val
            and self.isMirror(left_node.left, right_node.right)
            and self.isMirror(left_node.right, right_node.left)  # Check outer children
        )  # Check inner children


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output_bool)
test_data = [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([], True),  # An empty tree is symmetric
    ([1], True),  # A single node tree is symmetric
    ([1, 2, 3], False),  # Simple asymmetric
    ([1, 2, 2], True),  # Root with two identical children
    ([1, 2, 2, 3, None, None, 3], True),  # Symmetric structure, Nones match
    ([1, 2, 2, None, 3, 3, None], True),  # Symmetric structure, Nones match
    ([2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, 9, 8], True),  # Deeper symmetric tree
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    # Use the imported helper function to create the tree
    root_node = create_binary_tree(tree_list) if tree_list else None
    result = solution.isSymmetric(root_node)
    assert result == expected


# You can add more specific test functions if needed
# def test_specific_case():
#    solution = Solution()
#    # ... create specific tree ...
#    assert solution.isSymmetric(root) == ...
