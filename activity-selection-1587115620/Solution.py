class Solution:
    def activitySelection(self, start: list[int], end: list[int]) -> int:
        n = len(start)
        m = [(start[i], end[i]) for i in range(n)]
        m.sort(key=lambda x: x[1])
        ans = 0
        end = -1
        for s, e in m:
            if s > end:
                ans += 1
                end = e
        return ans
        