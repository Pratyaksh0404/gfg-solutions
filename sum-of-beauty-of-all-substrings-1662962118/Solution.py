from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            cnt = Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                ans += max(cnt.values()) - min(cnt.values())

        return ans