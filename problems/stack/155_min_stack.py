# --- File: 155_min_stack.py ---
"""
LeetCode Problem: 155 - Min Stack
Link: https://leetcode.com/problems/min-stack/
Difficulty: Medium

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

# Solution Class - Implement the logic here
class MinStack:
    """
    Approach (Optimized Single Stack):
    Uses a single stack to store values and one variable `min_value` to track
    the current minimum.
    When pushing a value `val` that is less than the current `min_value`,
    instead of pushing `val`, we push a calculated marker: `2 * val - self.min_value`.
    This marker will always be less than the new `min_value` (`val`).
    We then update `self.min_value = val`.
    When popping, if the popped value `top_val` is less than `self.min_value`,
    it indicates it was a marker. We restore the previous minimum using the
    formula: `self.min_value = 2 * self.min_value - top_val`.
    `top()` also needs to check if the value on the stack is a marker.

    Time Complexity: O(1) for all operations.
    Space Complexity: O(N) - For the single stack storing N elements (or markers).
                      No auxiliary stack needed.
    """

    def __init__(self):
        """
        Initializes the MinStack object.
        Uses float('inf') as the initial minimum placeholder.
        """
        self.stack = []
        self.min_value = float("inf")  # Placeholder for minimum

    def push(self, val: int) -> None:
        """
        Pushes element val onto the stack. Encodes if val is new minimum.
        """
        if not self.stack:
            # First element: push directly, set as min
            self.stack.append(val)
            self.min_value = val
        elif val < self.min_value:
            # New minimum found: push encoded marker, then update min_value
            # Formula: marker = 2 * new_min - old_min
            self.stack.append(2 * val - self.min_value)
            self.min_value = val
        else:
            # Value is not a new minimum: push directly
            self.stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack. Decodes if necessary.
        Constraint: Will always be called on a non-empty stack.
        """
        # Constraint guarantees stack is not empty
        top_val = self.stack.pop()

        # Check if the popped value was an encoded marker
        if top_val < self.min_value:
            # It was a marker, restore the previous minimum
            # Formula derived from marker = 2 * new_min - old_min
            # => old_min = 2 * new_min - marker
            # where new_min is the current self.min_value
            self.min_value = 2 * self.min_value - top_val

        # If the stack becomes empty, reset min_value placeholder
        # (Important if push is called again later)
        if not self.stack:
            self.min_value = float("inf")

    def top(self) -> int:
        """
        Gets the 'logical' top element of the stack. Decodes if necessary.
        Constraint: Will always be called on a non-empty stack.

        Returns:
            int: The actual value at the top of the stack.
        """
        # Constraint guarantees stack is not empty
        top_val = self.stack[-1]

        # If the stored value is a marker (less than current min),
        # the actual logical top value *is* the current minimum.
        if top_val < self.min_value:
            return self.min_value
        else:
            # Otherwise, the stored value is the actual top value.
            return top_val

    def getMin(self) -> int:
        """
        Retrieves the minimum element currently in the stack.
        Constraint: Will always be called on a non-empty stack.

        Returns:
            int: The minimum value currently in the stack.
        """
        # Constraint guarantees stack is not empty, min_value holds the minimum
        # Note: Can return float('inf') ONLY if the stack somehow became empty
        # outside the allowed operations, but constraints prevent this.
        return self.min_value


# --- Test Section ---

# Test function for the example scenario
def test_min_stack_example_1():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    # After pushing -2, 0, -3
    assert minStack.getMin() == -3, "Test Case 1 Failed: getMin after pushes"

    minStack.pop()

    # After popping -3
    assert minStack.top() == 0, "Test Case 1 Failed: top after pop"
    assert minStack.getMin() == -2, "Test Case 1 Failed: getMin after pop"


# You can add more specific test functions if needed
def test_min_stack_further_operations():
    minStack = MinStack()
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)

    # Stack: [0, 1, 0], Min should be 0
    assert minStack.getMin() == 0, "Test Case 2 Failed: getMin with duplicates"

    minStack.pop()

    # Stack: [0, 1], Min should be 0
    assert (
        minStack.getMin() == 0
    ), "Test Case 2 Failed: getMin after popping duplicate min"
    assert minStack.top() == 1, "Test Case 2 Failed: top after popping duplicate min"

    minStack.pop()
    # Stack: [0], Min should be 0
    assert minStack.getMin() == 0, "Test Case 2 Failed: getMin after popping 1"
    assert minStack.top() == 0, "Test Case 2 Failed: top after popping 1"


def test_min_stack_negative_and_zero():
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    # Stack: [2, 0, 3, 0] Min: 0
    assert minStack.getMin() == 0
    minStack.pop()  # Pop 0
    # Stack: [2, 0, 3] Min: 0
    assert minStack.getMin() == 0
    minStack.pop()  # Pop 3
    # Stack: [2, 0] Min: 0
    assert minStack.getMin() == 0
    minStack.pop()  # Pop 0
    # Stack: [2] Min: 2
    assert minStack.getMin() == 2


# Command to run tests: pytest problems/stack/155_min_stack.py
