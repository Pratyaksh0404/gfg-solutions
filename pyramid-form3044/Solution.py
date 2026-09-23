class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        right[-1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        maxi = 0
        for i in range(n):
            h = min(left[i], right[i])
            if h <= (i + 1) and h <= (n - i):
                maxi = max(maxi, h)

        ans = sum(arr)
        f = maxi ** 2

        return ans - f