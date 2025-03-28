"""
LeetCode Problem: 21 - Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy

Problem Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list.
Return the head of the merged linked list.

Examples:
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
from utils.linked_list_utils import create_linked_list
from utils.test_runner import run_tests


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Approach:
        1. Created a dummy pointer, and a current pointer.
        2. The current pointer starts at dummy and help build the list.
        3. Traverse the two lists, attach appropriate nodes to the current pointer
        4. Add the remaining node of the remaining list to the end.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            list1: ListNode - Head of the first sorted linked list
            list2: ListNode - Head of the second sorted linked list

        Returns:
            ListNode - Head of the merged sorted linked list
        """
        # Your solution here
        # Create a dummy node that acts as a starting point for the merged list.
        dummy = ListNode(-1)
        current = dummy

        # While both lists have nodes, compare the current nodes.
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link current to list1's node.
                list1 = list1.next  # Advance list1's pointer.
            else:
                current.next = list2  # Link current to list2's node.
                list2 = list2.next  # Advance list2's pointer.
            current = current.next  # Move the current pointer forward.

        # If there are remaining nodes in either list, attach them.
        current.next = list1 if list1 else list2

        # Return dummy.next, which is the head of the merged list.
        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    # Helper to convert linked list to value list for easier comparison
    def linked_list_to_list(node):
        values = []
        current = node
        while current:
            values.append(current.val)
            current = current.next
        return values

    test_cases = [
        # Format: ((list1, list2), expected_output)
        (
            (create_linked_list([1, 2, 4]), create_linked_list([1, 3, 4])),
            [1, 1, 2, 3, 4, 4],
        ),
        ((create_linked_list([]), create_linked_list([])), []),
        ((create_linked_list([]), create_linked_list([0])), [0]),
    ]

    # Custom test runner for linked list problems
    def test_runner(list1, list2):
        result = solution.mergeTwoLists(list1, list2)
        # Convert result to list for comparison
        return linked_list_to_list(result)

    run_tests(test_runner, test_cases)


def test_mergeTwoLists():
    solution = Solution()
    assert linked_list_to_list(
        solution.mergeTwoLists(
            create_linked_list([1, 2, 4]), create_linked_list([1, 3, 4])
        )
    ) == [1, 1, 2, 3, 4, 4]
    assert (
        linked_list_to_list(
            solution.mergeTwoLists(create_linked_list([]), create_linked_list([]))
        )
        == []
    )
    assert linked_list_to_list(
        solution.mergeTwoLists(create_linked_list([]), create_linked_list([0]))
    ) == [0]
