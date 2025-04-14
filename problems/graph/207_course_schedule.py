"""
LeetCode Problem: 207 - Course Schedule
Link: https://leetcode.com/problems/course-schedule/
Difficulty: Medium

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Examples:
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= 5000
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* All the pairs prerequisites[i] are unique.
"""
import pytest
from typing import List
from collections import defaultdict, deque  # Useful for graph representation and BFS

# Solution Class - Implement the logic here
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished given the prerequisites.

        Approach:
        [Explain your approach here - e.g., Topological Sort using Kahn's (BFS) or DFS]

        Time Complexity: O(V+E)
        Space Complexity: O(V+E)

        Args:
            numCourses: The total number of courses.
            prerequisites: A list of pairs [ai, bi] meaning course bi is a prerequisite for ai.

        Returns:
            bool: True if all courses can be finished, False otherwise (due to cycle).
        """
        # --- Implement your solution here ---
        # Common steps:
        if numCourses <= 1 or not prerequisites:
            return True

        # --- Need separate in_degree tracking ---
        in_degree = [0] * numCourses  # Index = course, value = in-degree
        # --- Adjacency List: Map prereq -> list of courses that depend on it ---
        adj = defaultdict(list)  # Cleaner way to build adjacency list

        for course, pre in prerequisites:
            # Build adjacency list: pre -> course
            adj[pre].append(course)
            # Increment in-degree of the course requiring the prerequisite
            in_degree[course] += 1

        # --- Initialize Queue ---
        # Find all courses with in-degree 0
        queue = deque()
        for course_id in range(numCourses):  # Iterate 0 to numCourses-1
            if in_degree[course_id] == 0:
                queue.append(course_id)

        # --- Process Queue ---
        count = 0  # Count of courses successfully "taken"
        while queue:
            prereq_course = queue.popleft()  # Course whose prerequisites are met
            count += 1

            # Process neighbors (courses that depend on prereq_course)
            # Use the clean adjacency list `adj`
            if prereq_course in adj:  # Check if this course is a prereq for any others
                for dependent_course in adj[prereq_course]:
                    in_degree[dependent_course] -= 1  # Decrement dependent's in-degree
                    # If dependent course now has no unmet prerequisites, add to queue
                    if in_degree[dependent_course] == 0:
                        queue.append(dependent_course)

        # --- Check Result ---
        # Did we manage to take all courses?
        return count == numCourses

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished given the prerequisites, using DFS cycle detection.

        Approach:
        Use DFS to traverse the course dependency graph. Track node states:
        0: Unvisited
        1: Visiting (currently in the recursion stack for this DFS path)
        2: Visited (fully explored from this node downwards, no cycles found from here)
        If DFS encounters a node marked as 'Visiting', a cycle is detected.

        Time Complexity: O(V + E) - Visits each node and edge once.
        Space Complexity: O(V + E) - For adjacency list and recursion stack depth.

        Args:
            numCourses: The total number of courses.
            prerequisites: A list of pairs [ai, bi] meaning course bi is a prerequisite for ai.

        Returns:
            bool: True if all courses can be finished (no cycle), False otherwise.
        """
        # State tracker: 0=Unvisited, 1=Visiting, 2=Visited
        visit_state = [0] * numCourses
        # Adjacency list: prerequisite -> list of courses needing it
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)

        def dfs(node):
            # Mark current node as 'Visiting' (in the current recursion path)
            visit_state[node] = 1

            # Explore neighbors
            for neighbor in adj[node]:
                # Cycle detected: Neighbor is already being visited in this path
                if visit_state[neighbor] == 1:
                    return False
                # If neighbor is unvisited, recursively explore it
                elif visit_state[neighbor] == 0:
                    # If the recursive call finds a cycle deeper down, propagate False
                    if not dfs(neighbor):
                        return False
                # Else (visit_state[neighbor] == 2): Neighbor is fully visited, known to be safe, do nothing.

            # Finished exploring all paths from 'node'. Mark as fully 'Visited'.
            # Remove from 'visiting' state (implicitly done by changing state to 2)
            visit_state[node] = 2
            # No cycle found originating from this node or its descendants
            return True

        # Iterate through all courses to handle disconnected graph components
        for node in range(numCourses):
            # Start DFS only if node hasn't been fully visited yet
            # (It could be 0=Unvisited or potentially 1=Visiting if there's a bug,
            #  but we really only need to start if it's 0. Checking != 2 is safe)
            # A simpler check `if visit_state[node] == 0:` also works.
            if visit_state[node] == 0:  # Start DFS only for unvisited nodes
                # If DFS starting from this node detects a cycle, return False immediately
                if not dfs(node):
                    return False

        # If loops complete without finding any cycles, all courses can be finished.
        return True


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (numCourses, prerequisites, expected_bool)
test_data = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (1, [], True),
    (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),  # DAG
    (3, [[0, 1], [1, 2], [2, 0]], False),  # Cycle 0->1->2->0
    (4, [[1, 0], [2, 1], [3, 2]], True),  # Linear path
    (4, [[1, 0], [0, 2], [2, 1], [3, 0]], False),  # Cycle 0->2->1->0
    (5, [[1, 4], [2, 4], [3, 1], [3, 2]], True),
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("numCourses, prerequisites, expected", test_data)
def test_solution(numCourses, prerequisites, expected):
    solution = Solution()
    result = solution.canFinishDFS(numCourses, prerequisites)
    assert result == expected


# You can add more specific test functions if needed
