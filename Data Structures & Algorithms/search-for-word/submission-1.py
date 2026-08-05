class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        def dfs(r, c, i):
            if i == n:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]\
            or board[r][c] == '0':
                return False
            board[r][c] = '0'
            new_paths = []
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                new_paths.append(dfs(nr, nc, i + 1))
            board[r][c] = word[i]
            return any(new_paths)
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

                



        return False