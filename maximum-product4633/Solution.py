class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        if k == n:
            prod = 1
            for x in arr:
                prod *= x
            return prod

        if arr[-1] == 0 and k % 2 == 1:
            return 0

        if arr[-1] < 0 and k % 2 == 1:
            prod = 1
            for i in range(n - 1, n - 1 - k, -1):
                prod *= arr[i]
            return prod

        prod = 1
        i, j = 0, n - 1

        if k % 2 == 1:
            prod *= arr[j]
            j -= 1
            k -= 1

        for _ in range(k // 2):
            lp = arr[i] * arr[i + 1]
            rp = arr[j] * arr[j - 1]
            if lp > rp:
                prod *= lp
                i += 2
            else:
                prod *= rp
                j -= 2

        return prod