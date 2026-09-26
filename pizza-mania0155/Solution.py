class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        dp = [0] + [float('inf')] * x
        for i in range(1, x + 1):
            dp[i] = min(dp[max(0, i-s)] + cs, dp[max(0, i-m)] + cm, dp[max(0, i-l)] + cl)
            
        return dp[x]