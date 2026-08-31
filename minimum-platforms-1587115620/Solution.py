class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        n = len(arr)
        ans = 0
        maxi = max(dep)
        a = [0]*(maxi+2)
        for i in range(n):
            a[arr[i]] += 1
            a[dep[i]+1] -= 1

        c = 0
        for i in range(maxi+2):
            c += a[i]
            ans = max(ans,c)

        return ans
        
