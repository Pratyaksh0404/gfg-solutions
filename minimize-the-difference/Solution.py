class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k >= n:
            return 0

        suff_max = [0] * n
        suff_min = [0] * n
        suff_max[-1] = suff_min[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suff_max[i] = max(suff_max[i + 1], arr[i])
            suff_min[i] = min(suff_min[i + 1], arr[i])

        ans = suff_max[k] - suff_min[k]
        pref_max = arr[0]
        pref_min = arr[0]

        for i in range(1, n - k):
            cur_max = max(pref_max, suff_max[i + k])
            cur_min = min(pref_min, suff_min[i + k])
            ans = min(ans, cur_max - cur_min)
            pref_max = max(pref_max, arr[i])
            pref_min = min(pref_min, arr[i])

        ans = min(ans, pref_max - pref_min)
        return ans