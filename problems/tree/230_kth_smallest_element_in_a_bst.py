"""
LeetCode Problem: 230 - Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium

Problem Description:
Given the root of a binary search tree, and an integer k, return the k-th smallest value (1-indexed) of all the values of the nodes in the tree.

Examples:
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow up: If the BST is modified (insert/delete operations) often and you need to find the k-th smallest frequently, how would you optimize?
"""
import pytest
from typing import Optional

from utils.tree_utils import (
    TreeNode,
    create_binary_tree,
)

"""
        Follow-up Optimization for Frequent Modifications and Queries:

        If the BST is frequently modified (insertions/deletions) and kthSmallest
        is called often, the O(H + k) or O(N) traversal per query can become
        inefficient. An optimized approach involves augmenting the TreeNode
        structure to store the size of the left subtree at each node.

        Augmented TreeNode:
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
                self.left_subtree_size = 0 # Number of nodes in the left subtree

        Algorithm with Augmented Tree:
        1. Maintain `left_subtree_size` during insertions and deletions.
           - Insert: Increment count for nodes where the new node goes left. O(H).
           - Delete: Decrement count along the path; more complex handling needed
             during node replacement (e.g., with inorder successor). O(H).
        2. `kthSmallest(node, k)`:
           - Let `left_count = node.left.left_subtree_size + 1` if node.left exists, else 0.
             (Alternatively, store total size of subtree rooted at node, then left_count is node.left.size if node.left exists).
           - If `k <= left_count`: Recurse on `node.left` with `k`.
           - If `k == left_count + 1`: Return `node.val`.
           - If `k > left_count + 1`: Recurse on `node.right` with `k = k - left_count - 1`.

        Time Complexity:
        - kthSmallest: O(H) (typically O(log N) for balanced trees).
        - insert/delete: O(H) (slightly higher constant factor due to count updates).

        Space Complexity:
        - O(1) extra space per node to store the count.
        - O(H) recursion stack space for the operations.

        This trades slightly slower modifications for significantly faster
        kthSmallest queries.
        """

# Solution Class - Implement the logic here
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach:
        [Explain your approach here - e.g., Inorder traversal and stopping early]

        Time Complexity: O(H + k) in the optimized inorder approach, where H is height. In the worst case (skewed tree), this is O(N). A full inorder traversal is O(N).
        Space Complexity: O(H) for the recursive inorder stack (worst case O(N)). Or O(N) if storing all elements first.

        Args:
            root (Optional[TreeNode]): The root node of the binary search tree.
            k (int): The desired rank (1-indexed) of the smallest element.

        Returns:
            int: The value of the k-th smallest element in the BST.
        """
        # Your solution here
        result = None

        def traverse(node: TreeNode):
            nonlocal k
            nonlocal result
            if result:
                return
            if node:
                traverse(node.left)
                k -= 1
                if k == 0:
                    result = node.val
                    return
                traverse(node.right)

        traverse(root)
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_tree_list, k, expected_output)
test_data = [
    ([3, 1, 4, None, 2], 1, 1),  # Example 1
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),  # Example 2
    ([1], 1, 1),  # Single node tree
    ([2, 1], 1, 1),  # Simple left skew
    ([2, 1], 2, 2),
    ([1, None, 2], 1, 1),  # Simple right skew
    ([1, None, 2], 2, 2),
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 1, 0),  # More complex tree, k=1
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 3),  # More complex tree, k=3
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 6, 6),  # More complex tree, k=6 (root)
    ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 9, 9),  # More complex tree, k=9 (max)
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("tree_list, k, expected", test_data)
def test_solution(tree_list, k, expected):
    solution = Solution()
    root = create_binary_tree(tree_list)  # Use the provided utility function
    result = solution.kthSmallest(root, k)
    assert result == expected
