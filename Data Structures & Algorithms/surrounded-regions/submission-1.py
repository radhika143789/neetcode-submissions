class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        m = len(board)
        n = len(board[0])
        dir_ = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            if board[i][0] == "O":
                q.append([i,0])
                board[i][0] = "Y"
            if board[i][n-1] == "O":
                q.append([i,n-1])
                board[i][n-1] = "Y"
        
        for j in range(1,n-1):
            if board[0][j] == "O":
                q.append([0,j])
                board[0][j] = "Y"
            if board[m-1][j] == "O":
                q.append([m-1,j])
                board[m-1][j] = "Y"
        
        while q:
            x, y = q.popleft()

            for dx, dy in dir_:
                nx = dx + x
                ny = dy + y

                if 0<= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    q.append([nx,ny])
                    board[nx][ny] = "Y"
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "Y":
                    board[x][y] = "O"