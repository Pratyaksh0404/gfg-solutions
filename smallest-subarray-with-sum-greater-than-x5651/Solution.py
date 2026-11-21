class Solution:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        curr = 0
        ans = n + 1
        left = 0

        for right in range(n):
            curr += arr[right]
            while curr > x:
                ans = min(ans, right - left + 1)
                curr -= arr[left]
                left += 1

        return 0 if ans == n + 1 else ans