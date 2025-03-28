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
"""

import pytest
from typing import Optional
from utils.linked_list_utils import ListNode, create_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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


test_cases = [
    ([3, 2, 0, -4], 1, True),
    ([1, 1], 0, True),
    ([1], -1, False),
    ([], -1, False),
]


@pytest.mark.parametrize("input_list, pos, expected_output", test_cases)
def test_hasCycle(input_list: list[int], pos: int, expected_output: bool):
    solution = Solution()
    head = create_linked_list(input_list, pos)
    assert solution.hasCycle(head) == expected_output
