class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            costS1, costS2 = costS2, costS1

        m, n = len(s1), len(s2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if s2[i - 1] == s1[j - 1]:
                    dp[j] = prev + 1
                else:
                    if dp[j - 1] > dp[j]:
                        dp[j] = dp[j - 1]
                prev = temp

        ans = dp[m]
        return (m - ans) * costS1 + (n - ans) * costS2