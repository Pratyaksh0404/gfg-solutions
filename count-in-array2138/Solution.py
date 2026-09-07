class Solution:
    def count(self, n: int, m: int) -> int:
        adj = [[] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(i, m + 1, i):
                adj[i].append(j)
                if j != i:
                    adj[j].append(i)
                    
        dp = [1] * (m + 1)
        for _ in range(1, n):
            ndp = [0] * (m + 1)
            for i in range(1, m + 1):
                for j in adj[i]:
                    ndp[j] += dp[i]
            dp = ndp
            
        return sum(dp[1:])