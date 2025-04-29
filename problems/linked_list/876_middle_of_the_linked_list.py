"""
LeetCode Problem: 876 - Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy

Problem Description:
Given the `head` of a singly linked list, return *the middle node of the linked list*.

If there are two middle nodes, return **the second middle** node.

Examples:
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range `[1, 100]`.
`1 <= Node.val <= 100`.
"""
import pytest
from typing import Optional

# Definition for singly-linked list (assuming it's not in utils or defining here for clarity)


from utils.linked_list_utils import ListNode, create_linked_list, linked_list_to_list

# Solution Class - Implement the logic here
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly linked list.

        Approach:
        Uses the Two Pointers (Slow and Fast) technique.
        Initialize both `slow` and `fast` pointers to the `head` of the list.
        Iterate while `fast` and `fast.next` are not None:
          - Move `slow` one step forward (`slow = slow.next`).
          - Move `fast` two steps forward (`fast = fast.next.next`).
        When the loop finishes, `fast` has reached the end (or passed it),
        and `slow` will be pointing at the middle node. If the list has an
        even number of nodes, this technique naturally lands `slow` on the
        second middle node.

        Time Complexity: O(N), where N is the number of nodes in the linked list.
                         We traverse the list roughly N/2 times with the slow pointer
                         and N times with the fast pointer.
        Space Complexity: O(1), as we only use a constant amount of extra space
                          for the two pointers.

        Args:
            head: Optional[ListNode] - The head of the input linked list.

        Returns:
            Optional[ListNode] - The middle node (or second middle node)
                                  of the linked list. Returns None if the
                                  input list is empty (though constraints say size >= 1).
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (input_list_representation, expected_output_list_representation)
test_data = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),  # Odd number of nodes
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),  # Even number of nodes
    ([1], [1]),  # Single node list
    ([1, 2], [2]),  # Two node list
]

# Use pytest.mark.parametrize to create tests for each case
# Parameter names match the structure of test_data tuples
@pytest.mark.parametrize("input_list, expected_list", test_data)
def test_middleNode(input_list, expected_list):
    solution = Solution()

    # Create the input linked list from the list representation
    head_node = create_linked_list(input_list)

    # Get the result node from the solution method
    result_node = solution.middleNode(head_node)

    # Convert the result linked list (starting from the middle node) back to a list
    result_list = linked_list_to_list(result_node)

    # Assert that the result list matches the expected list
    assert result_list == expected_list
