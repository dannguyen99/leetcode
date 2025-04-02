"""
LeetCode Problem: 145 - Binary Tree Postorder Traversal
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Difficulty: Easy (though iterative is trickier than inorder/preorder)

Problem Description:
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Examples:
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a postorder traversal (Left -> Right -> Root) of a binary tree.

        Approach:
        Recursively, we could handle as follow:
        1. Encounter a node
        2. Go left, until none, add the value of the node
        3. Go right, until none, add the value of the node
        4. Go back to the parent, add the value of the node

        Time Complexity: O(N) - Visits each node once.
        Space Complexity:
            Recursive: O(H) - Due to call stack depth (H = tree height). Worst case O(N).
            Iterative: O(H or N) - Using stack(s). Can require storing more state than pre/inorder.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list containing the values of the nodes in postorder sequence.
        """
        # --- Implement your solution here ---
        result = []
        # Recursive approach
        # def traverse(node: TreeNode):
        #     if node:
        #         # 1. go left
        #         traverse(node.left)
        #         # 2. go right
        #         traverse(node.right)
        #         # 3. add the parent node
        #         result.append(node.val)
        # traverse(root)

        # Iterative approach
        stack = []
        current = root
        last_node_processed = None
        while current or stack:
            # 1. go left, until none
            print(stack)
            if current:
                stack.append(current)
                current = current.left
            else:
                node_on_top = stack[-1]
                if node_on_top.right and node_on_top.right is not last_node_processed:
                    current = node_on_top.right
                else:
                    node_on_top = stack.pop()
                    result.append(node_on_top.val)
                    last_node_processed = node_on_top
                    current = None
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, expected_output_list)
test_data = [
    ([1, None, 2, 3], [3, 2, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [2, 3, 1]),  # Simple balanced tree
    ([4, 2, 5, 1, 3], [1, 3, 2, 5, 4]),  # The example tree from intuition
    ([3, 1, None, None, 2], [2, 1, 3]),
    ([2, 3, None, 1], [1, 3, 2]),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, expected", test_data)
def test_solution(tree_list, expected):
    solution = Solution()
    # Use the imported helper function to create the tree
    root_node = create_binary_tree(tree_list)
    result = solution.postorderTraversal(root_node)
    assert result == expected


# You can add more specific test functions if needed
def test_edge_case_single_node():
    solution = Solution()
    root = TreeNode(5)  # TreeNode is now imported
    assert solution.postorderTraversal(root) == [5]
