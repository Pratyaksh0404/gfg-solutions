class Solution:
    def minCount(self, arr):
        n = len(arr)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        dp[n][n] = 0

        for k in range(n):
            ind = list(range(k)) + [n]
            for i in ind:
                for j in ind:
                    v = dp[i][j]
                    if v != -1:
                        if i == n or arr[k] > arr[i]:
                            if v + 1 > dp[k][j]:
                                dp[k][j] = v + 1
                        if j == n or arr[k] < arr[j]:
                            if v + 1 > dp[i][k]:
                                dp[i][k] = v + 1

        return n - max(max(row) for row in dp)