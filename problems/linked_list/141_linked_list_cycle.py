"""
LeetCode Problem: 141 - Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy

Problem Description:
Given head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Examples:
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 2nd node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from utils.test_runner import run_tests


class Solution:
    def hasCycle(self, head):
        """
        Approach:
        Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare):
        1. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
        2. If there's a cycle, fast pointer will eventually meet slow pointer
        3. If fast reaches end of list, no cycle exists

        Time Complexity: O(n) - Each node visited at most twice
        Space Complexity: O(1) - Only two pointers used

        Args:
            head: Head of the linked list

        Returns:
            bool: True if cycle exists, False otherwise
        """
        # Your solution here
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Helper function to create linked list with optional cycle
def create_linked_list(values, pos):
    if not values:
        return None

    # Create nodes
    nodes = [ListNode(val) for val in values]

    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos is valid
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Format: ((head, pos), expected_output)
        ((create_linked_list([3, 2, 0, -4], 1), 1), True),
        ((create_linked_list([1, 2], 0), 0), True),
        ((create_linked_list([1], -1), -1), False),
        ((create_linked_list([], -1), -1), False),
    ]

    # Custom test runner for linked list problems
    def test_runner(head, _):
        return solution.hasCycle(head)

    run_tests(test_runner, test_cases)
