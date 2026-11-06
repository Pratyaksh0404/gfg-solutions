class Solution:
    def countBT(self, h: int) -> int:
        MOD = 10**9 + 7
        if h == 0:
            return 0
        if h == 1:
            return 1

        dp0 = 1  # dp[0]
        dp1 = 1  # dp[1]

        for _ in range(2, h + 1):
            dp2 = (dp1 * (dp1 + 2 * dp0)) % MOD
            dp0 = dp1
            dp1 = dp2

        return dp1