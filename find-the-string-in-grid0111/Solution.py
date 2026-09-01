class Solution:
    def searchWord(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        k = len(word)
    
        dd = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
    
        ans = []
    
        for i in range(n):
            for j in range(m):
                if mat[i][j] != word[0]:
                    continue
    
                for di, dj in dd:
                    x, y = i, j
                    f = True
    
                    for p in range(1, k):
                        x += di
                        y += dj
    
                        if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != word[p]:
                            f = False
                            break
    
                    if f:
                        ans.append([i, j])
                        break
    
        return ans