class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        if m >= n:
            return sum(arr)
    
        curr = ans = sum(arr[:m])
        for i in range(n):
            curr += arr[(i + m) % n] - arr[i]
            if curr > ans:
                ans = curr
    
        return ans