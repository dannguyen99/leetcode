"""
LeetCode Problem: 226 - Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy

Problem Description:
Given the root of a binary tree, invert the tree, and return its root.

Examples:
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100
"""
import pytest
from typing import Optional

# Import from the utility file
# Make sure you have tree_utils.py with TreeNode and create_binary_tree/tree_to_level_order_list
from utils.tree_utils import TreeNode, create_binary_tree, tree_to_level_order_list
from collections import deque  # Potentially for iterative or BFS approach

# Solution Class - Implement the logic here
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree.

        Approach:
        Using BFS swap and a queue.
        Simply swap left and right node level by level, using a temp node in the action.

        Time Complexity: O(N) - W the maximum width of the tree
        Space Complexity: O(W)

        Args:
            root: The root node of the binary tree.

        Returns:
            Optional[TreeNode]: The root node of the inverted binary tree.
        """
        # --- Implement your solution here ---
        if root is None:
            return root
        # queue = deque([root])
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.right:
        #             queue.append(node.right)
        #         if node.left:
        #             queue.append(node.left)
        #         temp = node.right
        #         node.right = node.left
        #         node.left = temp
        # return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_inverted_tree_list)
test_data = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2], [1, None, 2]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("input_list, expected_list", test_data)
def test_solution(input_list, expected_list):
    solution = Solution()
    root = create_binary_tree(input_list)
    inverted_root = solution.invertTree(root)
    result_list = tree_to_level_order_list(inverted_root)  # Convert back for comparison
    assert result_list == expected_list


# You can add more specific test functions if needed
