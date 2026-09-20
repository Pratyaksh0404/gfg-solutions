class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        if not n:
            return 0

        horiz = [[0] * n for _ in range(n)]
        vert = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    horiz[i][j] = (horiz[i][j + 1] + 1) if (j + 1 < n) else 1

        for j in range(n):
            for i in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    vert[i][j] = (vert[i + 1][j] + 1) if (i + 1 < n) else 1

        ans = 0
        for i in range(n):
            for j in range(n):
                k = min(horiz[i][j], vert[i][j])
                while k > ans:
                    if vert[i][j + k - 1] >= k and horiz[i + k - 1][j] >= k:
                        ans = k
                        break
                    k -= 1

        return ans