class Solution:
    def maxFrequency(self, arr, k):
        arr.sort()
        left = 0
        curr = 0
        ans = 0

        for right in range(len(arr)):
            curr += arr[right]

            while arr[right] * (right - left + 1) - curr > k:
                curr -= arr[left]
                left += 1

            if right - left + 1 > ans:
                ans = right - left + 1

        return ans