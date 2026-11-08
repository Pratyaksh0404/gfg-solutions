class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        low = 0
        high = min(s1, s2) * n
        ans = high

        while low <= high:
            mid = (low + high) // 2
            docs = (mid // s1) + (mid // s2)

            if docs >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans