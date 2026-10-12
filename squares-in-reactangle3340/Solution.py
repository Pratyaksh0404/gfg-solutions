class Solution:
    def minSquares(self, n, m):
        ans = 0
        while n > 0 and m > 0:
            if n < m:
                n, m = m, n
            ans += n // m
            n %= m
            
        return ans