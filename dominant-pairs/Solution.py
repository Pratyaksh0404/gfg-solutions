class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        m = len(arr) // 2
        a, b, ans, i, j = sorted(arr[:m]), sorted(arr[m:]), 0, 0, 0
        while i < m and j < m:
            if a[i] >= 5 * b[j]:
                ans += m - i
                j += 1
            else:
                i += 1
                
        return ans