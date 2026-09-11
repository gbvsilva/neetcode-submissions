class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        def addCell(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
