"""
LeetCode Problem: 104 - Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy

Problem Description:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples:
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
* The number of nodes in the tree is in the range [0, 10^4].
* -100 <= Node.val <= 100
"""
import pytest
from typing import Optional
from collections import deque  # Potentially for BFS approach

# Import from the utility file
from utils.tree_utils import TreeNode, create_binary_tree

# Solution Class - Implement the logic here
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree using recursion (DFS).

        Approach:
        Recursively find the depth of the left and right subtrees.
        The depth of the current node is 1 plus the maximum of the two subtree depths.
        The base case is an empty tree (None node), which has a depth of 0.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the tree.
        """
        # Base case: An empty subtree has depth 0
        if not root:
            return 0

        # Recursively find the depth of the left subtree
        left_depth = self.maxDepth(root.left)

        # Recursively find the depth of the right subtree
        right_depth = self.maxDepth(root.right)

        # The depth of the tree rooted at 'root' is 1 (for root itself)
        # plus the depth of the deeper subtree.
        return 1 + max(left_depth, right_depth)


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_depth)
test_data = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),  # Empty tree
    ([0], 1),  # Single node tree
    ([1, 2, 3, 4, 5], 3),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    # Use the imported helper function to create the tree
    root_node = create_binary_tree(tree_list) if tree_list else None
    result = solution.maxDepth(root_node)
    assert result == expected


# You can add more specific test functions if needed
