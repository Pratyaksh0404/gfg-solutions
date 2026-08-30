from bisect import bisect_left

class Solution:
    def getMarks(self, l, r, rank):
        pre = []
        tot = 0
        for i in range(len(l)):
            tot += (r[i] - l[i] + 1)
            pre.append(tot)

        ans = []
        for q in rank:
            idx = bisect_left(pre, q)
            prev = pre[idx - 1] if idx > 0 else 0
            ans.append(l[idx] + (q - prev - 1))

        return ans