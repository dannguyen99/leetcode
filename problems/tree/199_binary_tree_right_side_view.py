"""
LeetCode Problem: 199 - Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Difficulty: Medium

Problem Description:
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

Examples:
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
*   The number of nodes in the tree is in the range `[0, 100]`.
*   -100 <= Node.val <= 100
"""
import pytest
from typing import List, Optional
from collections import deque

from utils.tree_utils import TreeNode, create_binary_tree  # Likely useful for BFS


# Solution Class - Implement the logic here
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach:
        Using level order traversal
        At each level, we only looking at the rightmost element.
        We do this by adding the right most element first to the queue, so naturally, it will be processed first.
        Any subsequence nodes in the same level will be ignore, but we continue to store their children inside the queue.

        Time Complexity: O(N) - Where N is the number of nodes in the tree, as we visit each node once.
        Space Complexity: O(W) - Where W is the maximum width of the tree (for BFS queue) or O(H) where H is the height (for DFS recursion stack). In the worst case (complete binary tree), W can be O(N).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: The values of the nodes visible from the right side.
        """
        # Your solution here
        queue = deque([root]) if root else []
        result = []
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                # append the right child first
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_list_representation, expected_output_list)
test_data = [
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),  # Example 1
    ([1, None, 3], [1, 3]),  # Example 2
    ([], []),  # Example 3
    ([1, 2, 3, 4], [1, 3, 4]),  # Left-heavy
    ([1, 2], [1, 2]),  # Only left child
    ([1, 2, 3, None, None, 4, 5], [1, 3, 5]),  # More complex
    ([1], [1]),  # Single node
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("input_list, expected", test_data)
def test_solution(input_list, expected):
    solution = Solution()
    root = create_binary_tree(input_list)
    result = solution.rightSideView(root)
    assert result == expected
