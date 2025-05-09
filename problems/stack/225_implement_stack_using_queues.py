"""
LeetCode Problem: 225 - Implement Stack using Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/
Difficulty: Easy

Problem Description:
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
- You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only standard operations of a queue.

Examples:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
"""
import pytest
import collections  # For collections.deque

# Solution Class - Implement the logic here
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        Approach:
        [Explain your approach: e.g., using one queue or two queues]
        - For push: ...
        - For pop: ...
        - For top: ...
        """
        # Example: using one deque as a queue
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        # Your implementation here
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            item = self.q.popleft()
            self.q.append(item)

    def pop(self) -> int:
        """
        Removes the element on the top of the stack and returns it.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Your implementation here
        return self.q.popleft()

    def top(self) -> int:
        """
        Returns the element on the top of the stack.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Your implementation here
        # simlar to queue peek
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Your implementation here
        return not len(self.q)


# --- Test Section ---
# Testing class-based problems with pytest can be done by asserting states after operations.


def test_my_stack_example_1():
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    assert myStack.top() == 2, "Test Case 1 Failed: top()"
    assert myStack.pop() == 2, "Test Case 1 Failed: pop()"
    assert not myStack.empty(), "Test Case 1 Failed: empty()"
    assert (
        myStack.pop() == 1
    ), "Test Case 1 Failed: pop() after second push"  # Added to empty the stack
    assert (
        myStack.empty()
    ), "Test Case 1 Failed: empty() after all pops"  # Added to check final empty state


def test_my_stack_single_element():
    myStack = MyStack()
    myStack.push(5)
    assert not myStack.empty()
    assert myStack.top() == 5
    assert myStack.pop() == 5
    assert myStack.empty()


def test_my_stack_empty_initially():
    myStack = MyStack()
    assert myStack.empty()


# You can add more complex sequences of operations if needed.
# For example:
def test_my_stack_complex_sequence():
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.top() == 2
    s.push(4)
    assert s.top() == 4
    assert s.pop() == 4
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.empty()


"""
Follow-up: Can you implement the stack using only one queue?
(The template above can be adapted for either one or two queues)
"""
