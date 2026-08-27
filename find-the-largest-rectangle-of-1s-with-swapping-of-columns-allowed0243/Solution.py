class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
    
        for i in range(1, n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i-1][j]
    
        ans = 0
        for i in range(n):
            cc = [0] * (n + 1)
            for j in range(m):
                cc[mat[i][j]] += 1
    
            col = 1
            for h in range(n, 0, -1):
                while cc[h] > 0:
                    ans = max(ans, h * col)
                    col += 1
                    cc[h] -= 1
    
        return ans