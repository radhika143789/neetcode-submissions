class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        q = deque()

        # Add boundary O's
        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r, 0))

            if board[r][cols - 1] == 'O':
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0, c))

            if board[rows - 1][c] == 'O':
                q.append((rows - 1, c))

        while q:
            r, c = q.popleft()

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'
            ):
                continue

            board[r][c] = 'T'

            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'