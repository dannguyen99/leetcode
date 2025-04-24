"""
LeetCode Problem: 160 - Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Difficulty: Easy

Problem Description:
Given the heads of two singly linked-lists `headA` and `headB`, return *the node at which the two lists intersect*. If the two linked lists have no intersection at all, return `null`.
The lists must retain their original structure. No cycles exist.

Examples: See LeetCode page for visual examples.
Example 1: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 -> Output: Node with value 8
Example 2: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 -> Output: Node with value 2
Example 3: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 -> Output: null

Constraints:
*   1 <= m, n <= 3 * 10^4
*   1 <= Node.val <= 10^5
*   Lists retain original structure.
*   No cycles.
"""
from typing import List, Optional

import pytest

# Import necessary components from utils
from utils.linked_list_utils import ListNode, create_linked_list

# Solution Class - Implement the logic here
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        Approach: Two Pointers
        1. Initialize two pointers, pA at headA and pB at headB.
        2. Iterate while pA is not equal to pB:
           - If pA reaches the end of list A (pA is None), redirect it to headB.
           - Otherwise, advance pA to pA.next.
           - If pB reaches the end of list B (pB is None), redirect it to headA.
           - Otherwise, advance pB to pB.next.
        3. If the pointers meet (pA == pB), they are at the intersection node
           (or both are None if there's no intersection). Return pA (or pB).

        Why it works:
        - If the lists intersect, let len(A) = M, len(B) = N, length of common part = C.
        - Pointer pA travels M-C steps to the intersection, then N steps (through B). Total M-C+N.
        - Pointer pB travels N-C steps to the intersection, then M steps (through A). Total N-C+M.
        - Both pointers travel the same total distance (M+N-C) before meeting at the intersection.
        - If there's no intersection, pA travels M+N, pB travels N+M. They will both become None
          at the same time after traversing both lists, and the loop terminates returning None.

        Time Complexity: O(M + N) - Each pointer traverses at most M+N nodes.
        Space Complexity: O(1) - Only two extra pointers are used.

        Args:
            headA (ListNode): The head of the first linked list.
            headB (ListNode): The head of the second linked list.

        Returns:
            Optional[ListNode]: The intersecting node, or None if no intersection.
        """
        # Handle edge case of empty lists
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            # Advance pA, redirecting to headB if it reaches the end of A
            pA = pA.next if pA else headB
            # Advance pB, redirecting to headA if it reaches the end of B
            pB = pB.next if pB else headA

        # If pA == pB, they are either at the intersection node or both are None
        return pA


# --- Test Section ---

# Define test cases: (listA_values, listB_values, intersect_val, skipA, skipB)
# intersect_val = 0 means no intersection.
test_data = [
    # Example 1
    ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 8, 2, 3),
    # Example 2
    ([1, 9, 1, 2, 4], [3, 2, 4], 2, 3, 1),
    # Example 3
    ([2, 6, 4], [1, 5], 0, 3, 2),
    # Custom: Intersection at head A
    ([1, 2, 3], [1, 2, 3], 1, 0, 0),
    # Custom: Intersection at head B (conceptually, list A points into B)
    ([5, 1, 2, 3], [1, 2, 3], 1, 1, 0),
    # Custom: No intersection, different lengths
    ([1, 2, 3, 4], [5, 6], 0, 4, 2),
    # Custom: One list empty
    ([], [1, 2], 0, 0, 2),
    ([1, 2], [], 0, 2, 0),
    ([], [], 0, 0, 0),
    # Custom: Intersection at last node
    ([1, 2, 3], [4, 5, 3], 3, 2, 2),
]


@pytest.mark.parametrize(
    "listA_values, listB_values, intersect_val, skipA, skipB", test_data
)
def test_getIntersectionNode(
    listA_values: List[int],
    listB_values: List[int],
    intersect_val: int,
    skipA: int,
    skipB: int,
):
    solution = Solution()

    # --- Construct the linked lists with potential intersection ---
    headA = None
    headB = None
    expected_node = None

    if intersect_val == 0:
        # No intersection - create lists independently
        headA = create_linked_list(listA_values)
        headB = create_linked_list(listB_values)
        expected_node = None
    else:
        # Intersection exists - construct carefully
        # 1. Create the common tail part
        # Ensure skipA is within bounds for slicing listA_values
        if skipA >= len(listA_values):
            # This case implies intersection node doesn't exist as described
            # Or it's the node *after* the last element, which means common tail is empty
            common_head = None
        else:
            common_tail_values = listA_values[skipA:]
            common_head = create_linked_list(common_tail_values)

        expected_node = (
            common_head  # The first node of the common tail is the intersection
        )

        # 2. Create listA prefix
        listA_prefix_values = listA_values[:skipA]
        headA = create_linked_list(listA_prefix_values)
        if headA:
            # Find tail of prefix A and link to common head
            currentA = headA
            while currentA.next:
                currentA = currentA.next
            currentA.next = common_head
        else:  # skipA was 0, intersection is at headA
            headA = common_head

        # 3. Create listB prefix
        listB_prefix_values = listB_values[:skipB]
        headB = create_linked_list(listB_prefix_values)
        if headB:
            # Find tail of prefix B and link to common head
            currentB = headB
            while currentB.next:
                currentB = currentB.next
            currentB.next = common_head
        else:  # skipB was 0, intersection is at headB
            headB = common_head

    # Handle cases where input lists might be empty initially
    if not listA_values:
        headA = None
    if not listB_values:
        headB = None
    if not listA_values and not listB_values:
        expected_node = None

    # --- Call the function ---
    result_node = solution.getIntersectionNode(headA, headB)

    # --- Assert ---
    # Compare the node objects directly
    assert result_node == expected_node


# You might need to run pytest or adapt the test execution
# Example manual run (if not using pytest):
# test_getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 8, 2, 3)
# test_getIntersectionNode([2, 6, 4], [1, 5], 0, 3, 2)
