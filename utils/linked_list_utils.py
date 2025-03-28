# --- File: utils/linked_list_utils.py ---

from typing import Optional, List, Set

# Definition for singly-linked list (Use consistently)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Optional: Add a __repr__ for easier debugging/printing if needed
    def __repr__(self):
        return f"ListNode({self.val})"


# Helper function to create a linked list from a Python list, with optional cycle
def create_linked_list(values: List[int], pos: int = -1) -> Optional[ListNode]:
    """
    Creates a singly linked list from a list of values.
    Optionally creates a cycle by connecting the tail to the node at index 'pos'.

    Args:
        values: A list of values for the nodes.
        pos: The index to connect the tail node's next pointer to, creating a cycle.
             Defaults to -1 (no cycle).

    Returns:
        The head node of the created linked list, or None if values is empty.
    """
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    if not nodes:
        return None
    # Link nodes sequentially
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    # Create cycle if pos is valid
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]  # Tail points back to node at pos
    return nodes[0]


# Helper function to convert a linked list back to a Python list
# Includes basic cycle detection to prevent infinite loops.
def linked_list_to_list(head: Optional[ListNode], cycle_limit: int = 1000) -> List[int]:
    """
    Converts a linked list to a Python list of values.
    Includes cycle detection to prevent infinite loops during conversion.

    Args:
        head: The head node of the linked list.
        cycle_limit: Maximum number of nodes to visit (prevents infinite loops in case of cycle).

    Returns:
        A list of values from the linked list. Appends "...cycle detected..." if limit is hit.
    """
    items = []
    current = head
    visited: Set[ListNode] = set()  # Keep track of visited nodes
    count = 0
    while current and current not in visited and count < cycle_limit:
        visited.add(current)
        items.append(current.val)
        current = current.next
        count += 1

    # Indicate if a cycle was likely detected by revisiting a node or hitting the limit
    if current and (current in visited or count >= cycle_limit):
        items.append("...cycle detected...")  # Or handle differently if needed

    return items
