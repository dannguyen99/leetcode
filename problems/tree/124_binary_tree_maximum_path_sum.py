# LeetCode Problem: 124 - Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard
"""
Problem Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

Examples:
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
*   The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
*   `-1000 <= Node.val <= 1000`
"""

import pytest
from typing import Optional

# Import TreeNode and the tree utility functions from your utils file
from utils.tree_utils import TreeNode, create_binary_tree, tree_to_level_order_list


# Solution Class - Implement the logic here
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = float(
            "-inf"
        )  # Initialize with negative infinity for global max

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # No contribution from a null node

            # Recursively get max path sum from left and right children
            # Ensure we only consider positive contributions from children
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # Calculate the path sum that *terminates* at the current node
            # This path uses the current node and potentially both left and right positive branches
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum found so far
            self.global_max_sum = max(self.global_max_sum, current_path_sum)

            # Return the max path sum that *can be extended upwards* to the parent
            # This path uses the current node and only one of its positive branches (left or right)
            return node.val + max(left_gain, right_gain)

        # Start the DFS from the root
        dfs(root)

        return self.global_max_sum


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output)
test_data = [
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    ([1], 1),  # Single node
    (
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
        48,
    ),  # LeetCode example from similar problems
    ([-3], -3),  # Single negative node
    ([2, -1], 2),  # Root + left child
    ([2, 1], 3),  # Root + left child
    ([-2, -1], -1),  # Negative nodes, path sum is max of individual node values
]


# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_nodes, expected", test_data)
def test_solution(tree_nodes, expected):
    solution = Solution()
    root_node = create_binary_tree(tree_nodes)  # Using the imported utility function
    result = solution.maxPathSum(root_node)
    assert result == expected
