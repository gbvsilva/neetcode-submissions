class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        def addCell(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            q.append((r, c))
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            minutes += 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return max(0, minutes - 1)

            
