class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, req in prerequisites:
            graph[req].append(course)
        
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for c in graph[course]:
                if dfs(c) is False:
                    return False
            state[course] = 2
            return True
        return all(dfs(c) for c in range(numCourses))