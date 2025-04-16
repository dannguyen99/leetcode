"""
LeetCode Problem: 98 - Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium

Problem Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Examples:
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""
import pytest
from typing import Optional

from utils.tree_utils import (
    TreeNode,
    create_binary_tree,
)  # Needed for build_tree helper


# Solution Class - Implement the logic here
class Solution:
    def __init__(self):
        self.prev_val = float("-inf")  # Initialize with negative infinity

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # Traverse left
        if not self.isValidBST(root.left):
            return False

        # Check current node against the previous value
        if root.val <= self.prev_val:
            return False
        self.prev_val = root.val  # Update previous value

        # Traverse right
        if not self.isValidBST(root.right):
            return False

        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output)
test_data = [
    ([2, 1, 3], True),  # Example 1
    ([5, 1, 4, None, None, 3, 6], False),  # Example 2
    ([1], True),  # Single node
    (
        [],
        True,
    ),  # Empty tree (considered valid by LeetCode's definition in context, though constraints say >= 1 node)
    ([1, 1], False),  # Duplicate value violation (equal not allowed on left/right)
    ([3, 1, 5, 0, 2, 4, 6], True),  # A valid BST
    (
        [3, 1, 5, 0, 4, 2, 6],
        False,
    ),  # Invalid: 4 is > 3 but in left subtree (via node 1's right) - need range check
    ([5, 4, 6, None, None, 3, 7], False),  # Invalid: 3 is < 5 but in right subtree
    ([2**31 - 1], True),  # Max value node
    ([-(2**31)], True),  # Min value node
    # Add more test cases
    ([-(2**31)], True),
    ([3, 1, 5, None, 2], True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    root = create_binary_tree(tree_list)
    result = solution.isValidBST(root)
    assert result == expected
