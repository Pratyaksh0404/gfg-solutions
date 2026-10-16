class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        l = [0] * n
        curr = arr[0]
        for i in range(n):
            if arr[i] > curr:
                curr = arr[i]
            l[i] = curr

        ans = 0
        r = arr[-1]
        if arr[-1] == l[-1]:
            ans += 1

        for i in range(n - 2, -1, -1):
            if arr[i] == l[i] and arr[i] < r:
                ans += 1
            if arr[i] < r:
                r = arr[i]

        return ans