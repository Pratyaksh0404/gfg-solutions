class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)

        def solve(days):
            temp = list(s)
            for i in range(days):
                temp[p[i]] = '?'

            for i in range(n - 1):
                if temp[i] != '?' and temp[i + 1] != '?' and temp[i] == temp[i + 1]:
                    return False
            return True

        low = 0
        high = n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if solve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans