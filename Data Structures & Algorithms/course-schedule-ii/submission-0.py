from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degrees = defaultdict(int)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        queue = deque([c for c in range(numCourses) if in_degrees[c] == 0])
        courses = []
        while queue:
            prereq = queue.popleft()
            
            for course in adj[prereq]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)
            courses.append(prereq)

        return courses if all(in_degrees[course] == 0 for course in range(numCourses)) else []