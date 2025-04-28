"""
LeetCode Problem: 236 - Lowest Common Ancestor of a Binary Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Difficulty: Medium

Problem Description:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes `p` and `q`.
The LCA is the lowest node that has both `p` and `q` as descendants (a node can be a
descendant of itself). All node values are unique. `p` and `q` exist in the tree.

Examples: See LeetCode page.

Constraints: See LeetCode page.
"""
import pytest

# Import necessary components from tree_utils
# Assuming tree_utils.py is in a 'utils' directory relative to this file
# Adjust the path if your structure is different (e.g., from ..utils import ...)

from utils.tree_utils import TreeNode, create_binary_tree, find_node


# Solution Class - Implement the logic here
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Approach: Recursive Traversal
        [Explain your approach here - How does recursion help find the split point?]

        Time Complexity: O(N) - Visits each node once.
        Space Complexity: O(H) - Recursion stack depth (H is height, N in worst case).

        Args:
            root (TreeNode): The root of the binary tree.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor node.
        """
        if root:
            if root.val == q.val or root.val == p.val:
                return root
            left_found = self.lowestCommonAncestor(root.left, p, q)
            right_found = self.lowestCommonAncestor(root.right, p, q)
            if left_found and right_found:
                return root
            if left_found:
                return left_found
            if right_found:
                return right_found
            return None


# --- Test Section ---
# Uses create_binary_tree from utils and local find_node


def test_example_1():
    solution = Solution()
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 5)
    q_node = find_node(root, 1)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 3


def test_example_2():
    solution = Solution()
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 5)
    q_node = find_node(root, 4)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 5


def test_example_3():
    solution = Solution()
    nodes = [1, 2]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 1)
    q_node = find_node(root, 2)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 1


def test_direct_parent():
    solution = Solution()
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 5)
    q_node = find_node(root, 6)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 5


def test_root_is_lca():
    solution = Solution()
    nodes = [1, 2, 3]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 2)
    q_node = find_node(root, 3)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 1


def test_nodes_in_different_deep_branches():
    solution = Solution()
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 7)
    q_node = find_node(root, 0)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 3  # LCA should be root


def test_nodes_in_same_branch_deeper():
    solution = Solution()
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_binary_tree(nodes)
    p_node = find_node(root, 7)
    q_node = find_node(root, 4)
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    assert lca is not None and lca.val == 2  # LCA should be node 2
