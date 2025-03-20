"""
Test runner utility for LeetCode solutions.
"""

import time
import traceback
from typing import Callable, List, Any, Tuple


def run_tests(
    solution_func: Callable, test_cases: List[Tuple[Tuple[Any, ...], Any]]
) -> None:
    """
    Run tests for a solution function.

    Args:
        solution_func: The solution function to test
        test_cases: List of (inputs, expected_output) tuples
                   where inputs is a tuple of arguments to pass to the function
    """
    passed = 0
    total = len(test_cases)

    for i, (inputs, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {inputs}")
        print(f"Expected: {expected}")

        try:
            start_time = time.time()
            result = solution_func(*inputs)
            end_time = time.time()

            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

            if result == expected:
                passed += 1
                print(f"Result: {result} ✓")
                print(f"Execution time: {execution_time:.2f} ms")
            else:
                print(f"Result: {result} ✗")
                print(f"Execution time: {execution_time:.2f} ms")

        except Exception as e:
            print(f"Error: {e}")
            print(traceback.format_exc())

    print(f"\nSummary: {passed}/{total} test cases passed")


if __name__ == "__main__":
    # Example usage
    def add(a, b):
        return a + b

    test_cases = [((1, 2), 3), ((5, 7), 12), ((0, 0), 0)]

    run_tests(add, test_cases)
