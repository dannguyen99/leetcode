# --- File: 703_kth_largest_element_in_a_stream.py ---

"""
LeetCode Problem: 703 - Kth Largest Element in a Stream
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy

Problem Description:
Design a class to find the kth largest element in a stream. Note that it is the
kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the
  stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element
  representing the kth largest element in the stream.

Examples:
Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth largest element.
"""
import heapq  # <--- Needed for heap implementation
from typing import List

# Solution Class - Implement the logic here
class KthLargest:
    """
    Approach:
    This problem suggest using min-heap data structure from heapq.
    It is easy to manage since we can used the existing functions.

    Time Complexity:
     - __init__: O(N) - We perform the add operation for each element in nums.
     - add: O(logk) - Based on the nature of lib function

    Space Complexity: O(k) - Only need to manage the current heap
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object.
        Process the initial nums stream to establish the initial k largest elements.

        Args:
            k: The target rank (kth largest).
            nums: Initial list of numbers in the stream.
        """
        # Your initialization code here
        # Store k and initialize the data structure (likely a min-heap)
        self.k = k
        self.heap = []  # Or other structure
        # Process initial nums
        for num in nums:
            self.add(
                num
            )  # Can reuse the add logic, but careful about return value during init

    def add(self, val: int) -> int:
        """
        Adds val to the stream and returns the current kth largest element.

        Args:
            val: The integer value to add to the stream.

        Returns:
            int: The kth largest element after adding val.
        """
        # Your add logic here
        # 1. Add the new value `val` to your data structure.
        # 2. Maintain the size constraint (keep only k largest).
        # 3. Return the kth largest element (which is related to the top of the min-heap).
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# --- Test Section ---

# Testing this class requires simulating the sequence of calls.
# pytest parametrize doesn't directly map well here.
# We write specific test functions simulating the scenarios.


def test_kth_largest_example_1():
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)

    assert kthLargest.add(3) == 4, "Test Case 1 Failed: add(3)"
    assert kthLargest.add(5) == 5, "Test Case 1 Failed: add(5)"
    assert kthLargest.add(10) == 5, "Test Case 1 Failed: add(10)"
    assert kthLargest.add(9) == 8, "Test Case 1 Failed: add(9)"
    assert kthLargest.add(4) == 8, "Test Case 1 Failed: add(4)"


def test_kth_largest_empty_initial():
    k = 1
    nums = []
    kthLargest = KthLargest(k, nums)
    assert kthLargest.add(-3) == -3, "Test Case 2 Failed: add(-3)"
    assert kthLargest.add(-2) == -2, "Test Case 2 Failed: add(-2)"
    assert kthLargest.add(-4) == -2, "Test Case 2 Failed: add(-4)"
    assert kthLargest.add(0) == 0, "Test Case 2 Failed: add(0)"
    assert kthLargest.add(4) == 4, "Test Case 2 Failed: add(4)"


def test_kth_largest_with_duplicates():
    k = 2
    nums = [0]
    kthLargest = KthLargest(k, nums)
    assert (
        kthLargest.add(-1) == -1
    ), "Test Case 3 Failed: add(-1)"  # Stream: [0, -1], 2nd largest: -1
    assert (
        kthLargest.add(1) == 0
    ), "Test Case 3 Failed: add(1)"  # Stream: [0, -1, 1], 2nd largest: 0
    assert (
        kthLargest.add(-2) == 0
    ), "Test Case 3 Failed: add(-2)"  # Stream: [0, -1, 1, -2], 2nd largest: 0
    assert (
        kthLargest.add(-4) == 0
    ), "Test Case 3 Failed: add(-4)"  # Stream: [0, -1, 1, -2, -4], 2nd largest: 0
    assert (
        kthLargest.add(3) == 1
    ), "Test Case 3 Failed: add(3)"  # Stream: [0, -1, 1, -2, -4, 3], 2nd largest: 1
