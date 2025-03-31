# --- File: 155_min_stack.py ---
"""
LeetCode Problem: 155 - Min Stack
Link: https://leetcode.com/problems/min-stack/
Difficulty: Easy

Problem Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Examples:
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""
import pytest

# from typing import List, Optional # Not strictly needed for this impl

# Solution Class - Implement the logic here
class MinStack:
    """
    Approach:
    [Explain your overall approach here. How will you keep track of the minimum
     element efficiently alongside the main stack operations?]

    Time Complexity:
     - __init__: O(?)
     - push: O(1) - Required by problem
     - pop: O(1) - Required by problem
     - top: O(1) - Required by problem
     - getMin: O(1) - Required by problem

    Space Complexity: O(?) - Consider any extra space used besides the main stack.
    """

    def __init__(self):
        """
        Initializes the MinStack object.
        """
        # Your initialization code here
        pass

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        Ensure getMin() can still run in O(1).
        """
        # Your push logic here
        pass

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        Ensure getMin() reflects the new minimum if the popped element was the minimum.
        Constraint: Will always be called on a non-empty stack.
        """
        # Your pop logic here
        pass

    def top(self) -> int:
        """
        Gets the top element of the stack.
        Constraint: Will always be called on a non-empty stack.

        Returns:
            int: The value at the top of the stack.
        """
        # Your top logic here
        pass
        # return 0 # Placeholder

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack in O(1) time.
        Constraint: Will always be called on a non-empty stack.

        Returns:
            int: The minimum value currently in the stack.
        """
        # Your getMin logic here
        pass
        # return 0 # Placeholder


# --- Test Section ---

# # Test function for the example scenario
# def test_min_stack_example_1():
#     minStack = MinStack()
#     minStack.push(-2)
#     minStack.push(0)
#     minStack.push(-3)

#     # After pushing -2, 0, -3
#     assert minStack.getMin() == -3, "Test Case 1 Failed: getMin after pushes"

#     minStack.pop()

#     # After popping -3
#     assert minStack.top() == 0, "Test Case 1 Failed: top after pop"
#     assert minStack.getMin() == -2, "Test Case 1 Failed: getMin after pop"

# # You can add more specific test functions if needed
# def test_min_stack_further_operations():
#     minStack = MinStack()
#     minStack.push(0)
#     minStack.push(1)
#     minStack.push(0)

#     # Stack: [0, 1, 0], Min should be 0
#     assert minStack.getMin() == 0, "Test Case 2 Failed: getMin with duplicates"

#     minStack.pop()

#     # Stack: [0, 1], Min should be 0
#     assert minStack.getMin() == 0, "Test Case 2 Failed: getMin after popping duplicate min"
#     assert minStack.top() == 1, "Test Case 2 Failed: top after popping duplicate min"

#     minStack.pop()
#     # Stack: [0], Min should be 0
#     assert minStack.getMin() == 0, "Test Case 2 Failed: getMin after popping 1"
#     assert minStack.top() == 0, "Test Case 2 Failed: top after popping 1"


# def test_min_stack_negative_and_zero():
#     minStack = MinStack()
#     minStack.push(2)
#     minStack.push(0)
#     minStack.push(3)
#     minStack.push(0)
#     # Stack: [2, 0, 3, 0] Min: 0
#     assert minStack.getMin() == 0
#     minStack.pop() # Pop 0
#     # Stack: [2, 0, 3] Min: 0
#     assert minStack.getMin() == 0
#     minStack.pop() # Pop 3
#     # Stack: [2, 0] Min: 0
#     assert minStack.getMin() == 0
#     minStack.pop() # Pop 0
#     # Stack: [2] Min: 2
#     assert minStack.getMin() == 2


# Command to run tests: pytest problems/stack/155_min_stack.py
