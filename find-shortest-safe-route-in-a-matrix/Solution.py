from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                            mat[nr][nc] = -1

        q = deque()
        for r in range(n):
            if mat[r][0] == 1:
                q.append((r, 0, 1)) 
                mat[r][0] = 2       

        while q:
            r, c, d = q.popleft()

            if c == m - 1:
                return d

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2  
                    q.append((nr, nc, d + 1))

        return -1