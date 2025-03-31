"""
LeetCode Problem: 142 - Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Difficulty: Medium

Problem Description:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to. Note that pos is not passed as a parameter.

Do not modify the linked list.

Examples:
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: returns the node at index 1

Example 2:
Input: head = [1,2], pos = 0
Output: returns the node at index 0

Example 3:
Input: head = [1], pos = -1
Output: null

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.
"""

import pytest
from typing import Optional
from utils.linked_list_utils import ListNode, create_linked_list


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        1. Use Floyd's Cycle Detection Algorithm:
           - Use slow and fast pointers to detect the cycle.
        2. If a cycle is found:
           - Reset one pointer to head.
           - Move both pointers at the same pace until they meet at the cycle start.
        3. If no cycle is found, return None.

        Time Complexity: O(n) - Both pointers traverse at most n steps
        Space Complexity: O(1) - Only two pointers used

        Args:
            head: Head of the linked list

        Returns:
            ListNode: The node where the cycle begins, or None if there is no cycle
        """
        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None


test_cases = [
    ([3, 2, 0, -4], 1, 2),
    ([1, 2], 0, 1),
    ([1], -1, None),
    ([], -1, None),
]


@pytest.mark.parametrize("input_list, pos, expected_val", test_cases)
def test_detectCycle(input_list: list[int], pos: int, expected_val: Optional[int]):
    solution = Solution()
    head = create_linked_list(input_list, pos)
    result = solution.detectCycle(head)
    if expected_val is None:
        assert result is None
    else:
        assert result.val == expected_val
