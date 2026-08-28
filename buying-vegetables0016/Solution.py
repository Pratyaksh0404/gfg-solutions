class Solution:
    def minCost(self, mat):
        if not mat:
            return 0
    
        c0, c1, c2 = mat[0][0], mat[0][1], mat[0][2]
    
        for i in range(1, len(mat)):
            n0 = mat[i][0] + min(c1, c2)
            n1 = mat[i][1] + min(c0, c2)
            n2 = mat[i][2] + min(c0, c1)
            c0, c1, c2 = n0, n1, n2
    
        return min(c0, c1, c2)