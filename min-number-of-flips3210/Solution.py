class Solution:
    def minFlips(self, s):
        n = len(s)
        ans = 0

        for i, ch in enumerate(s):
            e = "0" if i % 2 == 0 else "1"
            if ch != e:
                ans += 1

        return min(ans, n - ans)