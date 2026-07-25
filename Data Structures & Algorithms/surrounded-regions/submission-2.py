class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == ROWS - 1 or r == 0 or
                        c == COLS - 1 or c == 0) and board[r][c] == 'O':
                            q.append((r, c))
            while q:
                row, col = q.popleft()
                if board[row][col] == 'O':
                    board[row][col] = 'T'
                    for d in directions:
                        r, c = row + d[0], col + d[1]
                        if (r < ROWS and r >=0 and
                            c < COLS and c >=0):
                            q.append((r,c))

        bfs()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                     board[r][c] = 'O'