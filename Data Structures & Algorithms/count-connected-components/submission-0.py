class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        isConnected = [[0] * n for _ in range(n)]
        for a, b in edges:
            isConnected[a][b] = 1
            isConnected[b][a] = 1
        visited = [False] * n
        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                dfs(node)
        return count

