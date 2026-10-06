class Solution:
    def longIncPath(self, matrix, n, m):
        if not matrix:
            return 0

        dp = [[0] * m for _ in range(n)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            res = 1
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))

            dp[i][j] = res
            return res

        return max(dfs(i, j) for i in range(n) for j in range(m))