"""
LeetCode Problem: 110 - Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/
Difficulty: Easy

Problem Description:
Given a binary tree, determine if it is height-balanced. A tree is height-balanced if
the depth of the two subtrees of every node never differs by more than one.

Examples: See LeetCode page.

Constraints: See LeetCode page.
"""
import pytest
from typing import Optional

from utils.tree_utils import TreeNode, create_binary_tree


# Solution Class - Implement the logic here
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: Recursive Height Check
        [Explain your approach here - How do you check balance and height simultaneously?]

        Time Complexity: O(N) - Visit each node once.
        Space Complexity: O(H) - Recursion stack depth (H is height, N in worst case).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: True if the tree is height-balanced, False otherwise.
        """
        # Your solution here
        if not root:
            return True

        def checkHeight(node: TreeNode):
            if not node:
                return 0  # Base case: empty tree has height 0

            # Recursively get the height of the left subtree
            leftHeight = checkHeight(node.left)
            if leftHeight == -1:
                return -1  # If the left subtree is unbalanced, return -1

            # Recursively get the height of the right subtree
            rightHeight = checkHeight(node.right)
            if rightHeight == -1:
                return -1  # If the right subtree is unbalanced, return -1

            # If the height difference between left and right subtrees is more than 1, return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1

            # Return the height of the current node
            return max(leftHeight, rightHeight) + 1

        return checkHeight(root) != -1


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_nodes, expected_output)
test_data = [
    ([3, 9, 20, None, None, 15, 7], True),  # Example 1
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),  # Example 2
    ([], True),  # Example 3
    ([1], True),  # Single node
    ([1, 2], True),  # Two nodes left
    ([1, None, 2], True),  # Two nodes right
    ([1, 2, None, 3], False),  # Unbalanced left heavy
    ([1, None, 2, None, 3], False),  # Unbalanced right heavy
]


@pytest.mark.parametrize("nodes_input, expected", test_data)
def test_solution(nodes_input, expected):
    solution = Solution()
    root = create_binary_tree(nodes_input)
    result = solution.isBalanced(root)
    assert result == expected
