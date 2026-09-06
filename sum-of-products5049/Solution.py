class Solution:
    def pairAndSum(self, arr):
        ans = 0
        for i in range(32):
            cnt = sum(1 for num in arr if num & (1 << i))
            ans += (cnt * (cnt - 1) // 2) << i
            
        return ans