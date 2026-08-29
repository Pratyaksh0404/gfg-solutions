class Solution:
    def findMax(self, n, a, b, k):
        d = [0] * (n + 1)
        for l, r, val in zip(a, b, k):
            d[l] += val
            if r + 1 < n:
                d[r + 1] -= val
        curr = 0
        ans = 0
        for i in range(n):
            curr += d[i]
            if curr > ans:
                ans = curr
        return ans