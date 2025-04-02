"""
LeetCode Problem: 102 - Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium

Problem Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Examples:
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
* The number of nodes in the tree is in the range [0, 2000].
* -1000 <= Node.val <= 1000
"""
import pytest
from typing import List, Optional
from collections import deque  # Queue implementation

# Import from the utility file
from utils.tree_utils import TreeNode, create_binary_tree

# Solution Class - Implement the logic here
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level order (BFS) traversal of a binary tree.

        Approach:
        Using a queue, we go level by level
        when reaching a level, we check level size using length of current queue
        in each level, popleft the parent nodes to process, and append right to the queue the child nodes

        Time Complexity: O(N) - Visits each node once.
        Space Complexity: O(W) - Where W is the maximum width of the tree. In the worst case (a complete binary tree), W can be roughly N/2, so O(N).

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains the
                             node values for a specific level, from left to right.
        """
        # --- Implement your solution here ---
        queue = deque([root]) if root else []
        result = []
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level_nodes)
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output_list_of_lists)
test_data = [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ([1], [[1]]),
    ([], []),
    ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),  # Slightly unbalanced
    ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),  # Skewed left
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    # Use the imported helper function to create the tree
    root_node = create_binary_tree(tree_list)
    result = solution.levelOrder(root_node)
    assert result == expected


# You can add more specific test functions if needed
def test_single_node():
    solution = Solution()
    root = TreeNode(5)  # TreeNode is now imported
    assert solution.levelOrder(root) == [[5]]
