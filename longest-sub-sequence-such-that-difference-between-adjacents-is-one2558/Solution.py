class Solution:
    def longestSubseq(self, arr):
        dp = {}
        ans = 0
        for x in arr:
            dp[x] = max(dp.get(x - 1, 0), dp.get(x + 1, 0)) + 1
            if dp[x] > ans:
                ans = dp[x]
        return ans