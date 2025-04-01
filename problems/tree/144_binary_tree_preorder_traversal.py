"""
LeetCode Problem: 144 - Binary Tree Preorder Traversal
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Difficulty: Easy

Problem Description:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Examples:
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

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

# Import from the utility file
from utils.tree_utils import TreeNode, create_binary_tree

# Solution Class - Implement the logic here
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a preorder traversal (Root -> Left -> Right) of a binary tree.

        Approach:
        With Recursive approach
        1. First, record the current value
        2. Then, go to the left path
        3. After left part done,  go to the right path.


        Time Complexity: O(N) - Visits each node once.
        Space Complexity:
            Recursive: O(H) - Due to call stack depth (H = tree height). Worst case O(N).
            Iterative: O(H or W) - Using a stack. Worst case O(N) for stack size (W = max width for some BFS-like iter, H for stack-based DFS iter). Generally O(H) for typical stack-based DFS preorder.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list containing the values of the nodes in preorder sequence.
        """
        # --- Implement your solution here ---
        result = []

        # Recursive approach
        # def traverse(node: TreeNode):
        #     if node:
        #       # 1. record the current value (visit me)
        #       result.append(node.val)
        #       # 2. go left
        #       traverse(node.left)
        #       # 3. go right
        #       traverse(node.right)
        # traverse(root)

        # Iteratie approach
        stack = []
        current = root
        while current or stack:
            # handle adding current, and push left to the stack
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output_list)
test_data = [
    ([1, None, 2, 3], [1, 2, 3]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),  # Simple balanced tree
    ([4, 2, 5, 1, 3], [4, 2, 1, 3, 5]),  # The example tree from intuition
    ([3, 1, None, None, 2], [3, 1, 2]),
    ([2, 3, None, 1], [2, 3, 1]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    # Use the imported helper function to create the tree
    root_node = create_binary_tree(tree_list)
    result = solution.preorderTraversal(root_node)
    assert result == expected


# You can add more specific test functions if needed
def test_edge_case_single_node():
    solution = Solution()
    root = TreeNode(5)  # TreeNode is now imported
    assert solution.preorderTraversal(root) == [5]
