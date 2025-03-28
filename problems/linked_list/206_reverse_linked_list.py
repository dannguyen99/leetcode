"""
LeetCode Problem: 206 - Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy

Problem Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Examples:
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
"""
import pytest
from typing import Optional, List

# Import helpers and ListNode from the central utility module
from utils.linked_list_utils import ListNode, create_linked_list, linked_list_to_list

# Solution Class - Implementation goes here
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach (Iterative):
        Initialize prev = None, curr = head. While curr exists: store next node (temp = curr.next),
        point curr.next to prev, update prev to curr, and move curr to temp. Return prev.

        Approach (Recursive):
        Base case: If head is None or head.next is None, return head.
        Recursively reverse the rest: new_head = reverseList(head.next).
        Make head.next.next point to head. Make head.next point to None. Return new_head.

        Time Complexity: O(N) - Both iterative and recursive traverse each node once.
        Space Complexity: O(1) (Iterative), O(N) (Recursive - due to call stack)

        Args:
            head: Optional[ListNode] - The head of the linked list.

        Returns:
            Optional[ListNode] - The new head of the reversed linked list.
        """
        # --- Iterative Implementation ---
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

        # --- Recursive Implementation ---
        # if head is None or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head


# --- Test Section ---

# Define test cases: (input_list, expected_output_list)
test_data = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
]

# Use pytest.mark.parametrize to run the test function for each case
@pytest.mark.parametrize("input_list, expected_list", test_data)
def test_reverseList(input_list: List[int], expected_list: List[int]):
    solution = Solution()
    # Create ListNode head from input list
    head_node = create_linked_list(input_list)
    # Call the solution method
    result_node = solution.reverseList(head_node)
    # Convert result ListNode back to list for comparison
    result_list = linked_list_to_list(result_node)
    # Assert the result matches the expectation
    assert result_list == expected_list
