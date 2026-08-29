class Solution:
    def countSubsequences(self, s: str, n: int) -> int:
        mod = 10**9 + 7
        dp = [0] * n
        for c in s:
            d = int(c)
            nxt = list(dp)
            
            for j in range(n):
                if dp[j]:
                    r = (j * 10 + d) % n
                    nxt[r] = (nxt[r] + dp[j]) % mod
                    
            nxt[d % n] = (nxt[d % n] + 1) % mod
            dp = nxt
            
        return dp[0]