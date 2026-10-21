class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        ans = curr = arr[0]
        for i in arr[1:]:
            curr = min(i, curr + i)
            ans = min(ans, curr)
            
        return ans