class Solution:
    def maxPackages(self, arr: list[int], tot: int) -> int:
        n = len(arr)
        if tot > n:
            tot = n

        curr = sum(arr[:tot])
        ans = curr

        for i in range(tot, n):
            curr += arr[i] - arr[i - tot]
            if curr > ans:
                ans = curr

        return ans