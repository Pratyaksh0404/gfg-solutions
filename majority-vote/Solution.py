class Solution:
    def findMajority(self, arr):
        a = set(arr)
        ans=[]
        n = len(arr)
        for i in a:
            if arr.count(i) > n//3:
                ans.append(i)
        ans.sort()
        return ans