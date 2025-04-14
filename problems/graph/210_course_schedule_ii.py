"""
LeetCode Problem: 210 - Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Difficulty: Medium

Problem Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Examples:
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct order is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= numCourses * (numCourses - 1)
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* ai != bi
* All the pairs [ai, bi] are distinct.
"""
import pytest
from typing import List
from collections import defaultdict, deque

# Solution Class - Implement the logic here
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Finds a valid order to take courses given prerequisites.

        Approach:
        Similar setup to Course Schedule I (build graph, in-degrees/visited states)
        Use a list to store the topological order
        Modify the BFS/DFS loop to append to the order list
        Check at the end if the order includes all courses

        Time Complexity: O(V+E)
        Space Complexity: O(V+E)

        Args:
            numCourses: The total number of courses.
            prerequisites: A list of pairs [ai, bi] meaning course bi is a prerequisite for ai.

        Returns:
            List[int]: A valid course order, or an empty list if impossible (cycle detected).
        """
        # Similar setup to Course Schedule I (build graph, in-degrees/visited states)
        # Need a list to store the topological order
        # Modify the BFS/DFS loop to append to the order list
        # Check at the end if the order includes all courses
        if numCourses <= 1 or not prerequisites:
            return list(range(numCourses))

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
        order = []
        while queue:
            prereq_course = queue.popleft()  # Course whose prerequisites are met
            order.append(prereq_course)

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
        return order if len(order) == numCourses else []

    def findOrderDFS(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        if numCourses <= 1 or not prerequisites:
            return list(range(numCourses))
        # State tracker: 0=Unvisited, 1=Visiting, 2=Visited
        visit_state = [0] * numCourses
        # Adjacency list: prerequisite -> list of courses needing it
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)

        def dfs(node, order: deque):
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
                    if not dfs(neighbor, order):
                        return False
                # Else (visit_state[neighbor] == 2): Neighbor is fully visited, known to be safe, do nothing.

            # Finished exploring all paths from 'node'. Mark as fully 'Visited'.
            # Remove from 'visiting' state (implicitly done by changing state to 2)
            visit_state[node] = 2
            order.appendleft(node)
            # No cycle found originating from this node or its descendants
            return True

        # Iterate through all courses to handle disconnected graph components
        order = deque([])
        for node in range(numCourses):
            # Start DFS only if node hasn't been fully visited yet
            # (It could be 0=Unvisited or potentially 1=Visiting if there's a bug,
            #  but we really only need to start if it's 0. Checking != 2 is safe)
            # A simpler check `if visit_state[node] == 0:` also works.
            if visit_state[node] == 0:  # Start DFS only for unvisited nodes
                # If DFS starting from this node detects a cycle, return False immediately
                if not dfs(node, order):
                    return []

        # If loops complete without finding any cycles, all courses can be finished.
        return order


# --- Test Section ---

# Define test cases as a list of tuples
# Format: (numCourses, prerequisites, possible_expected_orders or [])
# Note: Since multiple valid orders might exist, we check if the result is *a* valid order.
def is_valid_order(num_courses, prerequisites, order):
    if len(order) != num_courses:
        return False
    pos = {course: i for i, course in enumerate(order)}
    for course, pre in prerequisites:
        if pre not in pos or course not in pos or pos[pre] >= pos[course]:
            return False
    return True


test_data = [
    (2, [[1, 0]], [0, 1]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),  # One possible valid order
    (1, [], [0]),
    (2, [[1, 0], [0, 1]], []),  # Cycle
    (3, [[0, 1], [1, 2], [2, 0]], []),  # Cycle
    (3, [[1, 0], [1, 2], [0, 1]], []),  # Cycle
    (
        7,
        [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]],
        [6, 5, 4, 2, 3, 0, 1],
    ),  # Complex DAG
]

# Use pytest.mark.parametrize to create tests for each case
@pytest.mark.parametrize("numCourses, prerequisites, expected_example", test_data)
def test_solution(numCourses, prerequisites, expected_example):
    solution = Solution()
    result = solution.findOrderDFS(numCourses, prerequisites)

    if not expected_example:  # Expecting impossibility (cycle)
        assert result == []
    else:
        # Check if the result is a valid topological sort
        # 1. Check if the length is correct
        assert len(result) == numCourses
        # 2. Check if it respects prerequisites
        position_map = {course: index for index, course in enumerate(result)}
        valid = True
        for course, pre in prerequisites:
            if position_map[pre] >= position_map[course]:
                valid = False
                break
        assert (
            valid
        ), f"Result {result} is not a valid order for prerequisites {prerequisites}"


# You can add more specific test functions if needed
