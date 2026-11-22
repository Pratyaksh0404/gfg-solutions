class Solution:
    def longestSubarrayDivK(self, arr, k):
        n = len(arr)
        ans = 0
        pre = {}
        add = 0
        for i in range(n):
            add = (add+arr[i])%k
            if add == 0:
                ans = i+1
            elif add in pre:
                ans = max(ans,i-pre[add])
            else:
                pre[add] = i
        return ans