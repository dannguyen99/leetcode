"""
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

from typing import Optional, List

# Assuming your test runner is in a 'utils' directory relative to this file
# NOTE: The test runner might need modification to handle comparing lists
#       or you can convert list nodes to lists within the test section.
from utils.linked_list_utils import create_linked_list, linked_list_to_list
from utils.test_runner import run_tests


# Definition for singly-linked list (provided by LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Using the standard LeetCode method name
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach (Iterative):
        [Think about iterating through the list. You need to change the 'next' pointer
         of each node. What pointers do you need to keep track of as you traverse?
         Consider: the current node, the previous node, and possibly the next node.]

        Approach (Recursive):
        [Think about the base case (empty list or single node). For a node, what if
         the rest of the list (from node.next onwards) is already reversed? How do you
         attach the current node to the end of that reversed tail?]

        Time Complexity: O(?)
        Space Complexity: O(?) - Consider both iterative and recursive separately.

        Args:
            head: Optional[ListNode] - The head of the linked list.

        Returns:
            Optional[ListNode] - The new head of the reversed linked list.
        """
        # Your solution here (try iterative first, then maybe recursive)
        pass


# Custom assertion function for the test runner if needed, or adapt runner
# For now, we'll compare the list representations.
def run_linked_list_tests(solution_func, test_cases):
    # This wrapper adapts the test runner logic if it expects simple comparable outputs
    adapted_cases = []
    for inputs_tuple, expected_list in test_cases:
        # Create ListNode head from input list
        head_list = inputs_tuple[0]  # Assuming head is the first argument
        head_node = create_linked_list(head_list)
        adapted_cases.append(((head_node,), expected_list))

    passed = 0
    total = len(adapted_cases)

    for i, (inputs_nodes_tuple, expected_list) in enumerate(adapted_cases, 1):
        print(f"\nTest Case {i}:")
        # Represent input node for printing
        input_head_node = inputs_nodes_tuple[0]
        input_list_repr = linked_list_to_list(input_head_node)
        print(f"Input List: {input_list_repr}")
        print(f"Expected List: {expected_list}")

        try:
            # Run the actual function which returns the new head node
            result_head_node = solution_func(*inputs_nodes_tuple)
            # Convert the result node back to a list for comparison
            result_list = linked_list_to_list(result_head_node)

            if result_list == expected_list:
                passed += 1
                print(f"Result List: {result_list} ✓")
            else:
                print(f"Result List: {result_list} ✗")

        except Exception as e:
            import traceback

            print(f"Error: {e}")
            print(traceback.format_exc())

    print(f"\nSummary: {passed}/{total} test cases passed")


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # Format: ( (input_list,), expected_output_list )
        (([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
        (([1, 2],), [2, 1]),
        (([1],), [1]),
        (([],), []),
    ]

    # Use the custom runner or adapt your existing one
    run_linked_list_tests(solution.reverseList, test_cases)
    # If your run_tests can handle comparing list outputs directly after conversion,
    # you might not need the custom runner logic above, just the helper functions.
