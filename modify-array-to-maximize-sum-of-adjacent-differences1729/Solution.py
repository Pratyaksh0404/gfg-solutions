class Solution:
    def maxDiffSum(self, arr):
        a, b = 0, 0
        for i in range(1, len(arr)):
            a, b = max(a + abs(arr[i] - arr[i-1]), b + abs(arr[i] - 1)), max(a + abs(1 - arr[i-1]), b)
            
        return max(a, b)