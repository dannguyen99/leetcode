"""
LeetCode Problem: 94 - Binary Tree Inorder Traversal
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Difficulty: Easy

Problem Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Examples:
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100
"""
import pytest
from typing import List, Optional

# Import from the new utility file
from utils.tree_utils import (
    TreeNode,
    create_binary_tree,
)  # Removed tree_to_level_order_list as it's not used directly here

# Solution Class - Implement the logic here
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal (Left -> Root -> Right) of a binary tree.

        Approach:
        [Explain your approach here - e.g., Recursive or Iterative]

        Time Complexity: O(N) - where N is the number of nodes in the tree, as each node is visited once.
        Space Complexity:
            O(H) - for the recursive approach, where H is the height of the tree (call stack). Worst case O(N) for skewed tree.
            O(H) or O(N) - for the iterative approach using a stack. Worst case O(N).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list containing the values of the nodes in inorder sequence.
        """
        # --- Your solution here ---
        result = []

        # Example: Recursive helper function structure (you'll need to implement it)
        # def traverse(node):
        #     if node:
        #         # 1. Traverse left subtree
        #         # 2. Visit root node
        #         # 3. Traverse right subtree
        #         pass
        # traverse(root)

        # Example: Iterative structure using a stack (you'll need to implement it)
        # stack = []
        # current = root
        # while current or stack:
        #     # Logic to go left and push onto stack
        #     # Logic to pop, visit, and go right
        #     pass

        return result  # Replace with your actual implementation


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output_list)
# test_data = [
#     ([1, None, 2, 3], [1, 3, 2]),
#     ([], []),
#     ([1], [1]),
#     ([1, 2, 3], [2, 1, 3]), # Simple balanced tree
#     ([3, 1, None, None, 2], [1, 2, 3]), # Tree with right child having left child
#     ([2, 3, None, 1], [1, 3, 2]), # Tree requiring deeper left traversal
# ]

# # Use pytest.mark.parametrize to create tests for each case
# @pytest.mark.parametrize("tree_list, expected", test_data)
# def test_solution(tree_list, expected):
#     solution = Solution()
#     # Use the imported helper function to create the tree
#     root_node = create_binary_tree(tree_list)
#     result = solution.inorderTraversal(root_node)
#     assert result == expected

# # You can add more specific test functions if needed
# def test_edge_case_single_node():
#    solution = Solution()
#    root = TreeNode(5) # TreeNode is now imported
#    assert solution.inorderTraversal(root) == [5]
