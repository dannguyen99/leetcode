"""
LeetCode Problem: 234 - Palindrome Linked List
Link: https://leetcode.com/problems/palindrome-linked-list/
Difficulty: Easy

Problem Description:
Given the head of a singly linked list, return true if it is a palindrome, false otherwise.

Examples:
Example 1: Input: head = [1,2,2,1] Output: true
Example 2: Input: head = [1,2] Output: false

Constraints:
*   Number of nodes: [1, 10^5]
*   0 <= Node.val <= 9

Follow up: O(n) time and O(1) space?
"""
import pytest
from typing import Optional
from utils.linked_list_utils import ListNode, create_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach:
        [Explain your approach here - e.g., Convert to Array, Reverse Second Half]

        Time Complexity: O(?)
        Space Complexity: O(?)

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if the list is a palindrome, False otherwise.
        """
        # find the middle of the linked list
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        current = slow
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # compare the first half with the reverse second half
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_list_values, expected_output)
test_data = [
    ([1, 2, 2, 1], True),  # Example 1
    ([1, 2], False),  # Example 2
    ([1], True),  # Single node
    ([1, 1], True),  # Two same nodes
    ([1, 2, 3, 2, 1], True),  # Odd length palindrome
    ([1, 2, 3, 4, 5], False),  # Odd length non-palindrome
    ([], True),  # Empty list (conventionally palindrome)
]


@pytest.mark.parametrize("list_vals, expected", test_data)
def test_solution(list_vals, expected):
    solution = Solution()
    # Use create_linked_list from utils
    head = create_linked_list(list_vals)
    result = solution.isPalindrome(head)
    assert result == expected
