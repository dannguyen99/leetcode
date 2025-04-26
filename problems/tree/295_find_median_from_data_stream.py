"""
LeetCode Problem: 295 - Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Difficulty: Hard

Problem Description:
Implement the MedianFinder class:
- MedianFinder() initializes the object.
- void addNum(int num) adds the integer num to the data structure.
- double findMedian() returns the median of all elements so far.

The median is the middle value in an ordered integer list. If the size is even,
the median is the mean of the two middle values.

Examples: See LeetCode page.

Constraints:
*   -10^5 <= num <= 10^5
*   At least one element before calling findMedian.
*   At most 5 * 10^4 calls to addNum and findMedian.
"""
import heapq
import pytest  # Added for testing

# Solution Class - Implement the logic here
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        Approach: Two Heaps
        - Use a max-heap (`small_half`) to store the smaller half of the numbers.
        - Use a min-heap (`large_half`) to store the larger half of the numbers.
        - Keep the heaps balanced (size difference <= 1).
        """
        # Max-heap (stores negative values to simulate max-heap with heapq)
        self.small_half = []
        # Min-heap
        self.large_half = []

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        Maintain balance and heap properties.

        Time Complexity: O(log N) - due to heap push/pop operations.
        """
        # add to the smaller part first
        heapq.heappush(self.small_half, -num)

        # pop the largest item on the small heap for insertion to the large half
        heapq.heappush(self.large_half, -heapq.heappop(self.small_half))

        # adjust the heapsize as necessary
        if len(self.large_half) > len(self.small_half) + 1:
            heapq.heappush(self.small_half, -heapq.heappop(self.large_half))

    def findMedian(self) -> float:
        """
        Returns the median of current numbers.

        Time Complexity: O(1) - Peeking at heap tops.
        """
        if len(self.small_half) == len(self.large_half):
            return (-self.small_half[0] + self.large_half[0]) / 2
        else:
            return self.large_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# --- Test Section ---


def test_example_1():
    """Tests the sequence from Example 1."""
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    # Use pytest.approx for floating point comparisons
    assert mf.findMedian() == pytest.approx(1.5)
    mf.addNum(3)
    assert mf.findMedian() == pytest.approx(2.0)


def test_negative_numbers():
    """Tests adding negative numbers."""
    mf = MedianFinder()
    mf.addNum(-1)
    assert mf.findMedian() == pytest.approx(-1.0)
    mf.addNum(-2)
    assert mf.findMedian() == pytest.approx(-1.5)
    mf.addNum(-3)
    assert mf.findMedian() == pytest.approx(-2.0)


def test_mixed_numbers():
    """Tests adding a mix of positive, negative, and zero."""
    mf = MedianFinder()
    mf.addNum(6)  # [6] -> 6.0
    assert mf.findMedian() == pytest.approx(6.0)
    mf.addNum(10)  # [6, 10] -> 8.0
    assert mf.findMedian() == pytest.approx(8.0)
    mf.addNum(2)  # [2, 6, 10] -> 6.0
    assert mf.findMedian() == pytest.approx(6.0)
    mf.addNum(6)  # [2, 6, 6, 10] -> 6.0
    assert mf.findMedian() == pytest.approx(6.0)
    mf.addNum(5)  # [2, 5, 6, 6, 10] -> 6.0
    assert mf.findMedian() == pytest.approx(6.0)
    mf.addNum(0)  # [0, 2, 5, 6, 6, 10] -> 5.5
    assert mf.findMedian() == pytest.approx(5.5)
    mf.addNum(6)  # [0, 2, 5, 6, 6, 6, 10] -> 6.0
    assert mf.findMedian() == pytest.approx(6.0)
    mf.addNum(3)  # [0, 2, 3, 5, 6, 6, 6, 10] -> 5.5
    assert mf.findMedian() == pytest.approx(5.5)
    mf.addNum(1)  # [0, 1, 2, 3, 5, 6, 6, 6, 10] -> 5.0
    assert mf.findMedian() == pytest.approx(5.0)
    mf.addNum(0)  # [0, 0, 1, 2, 3, 5, 6, 6, 6, 10] -> 4.0
    assert mf.findMedian() == pytest.approx(4.0)
    mf.addNum(0)  # [0, 0, 0, 1, 2, 3, 5, 6, 6, 6, 10] -> 3.0
    assert mf.findMedian() == pytest.approx(3.0)


def test_single_element():
    """Tests with only one element."""
    mf = MedianFinder()
    mf.addNum(100)
    assert mf.findMedian() == pytest.approx(100.0)


def test_two_elements():
    """Tests with two elements."""
    mf = MedianFinder()
    mf.addNum(10)
    mf.addNum(20)
    assert mf.findMedian() == pytest.approx(15.0)
    mf = MedianFinder()  # Reset
    mf.addNum(20)
    mf.addNum(10)
    assert mf.findMedian() == pytest.approx(15.0)
