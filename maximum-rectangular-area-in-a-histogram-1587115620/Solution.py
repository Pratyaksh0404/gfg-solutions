class Solution:
    def getMaxArea(self,arr):
        n = len(arr)
        s = []
        ans = 0
        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:
                top = s.pop()
                wid = i if not s else i - s[-1] - 1

                ans = max(ans,arr[top]*wid)

            s.append(i)

        while s:
            top = s.pop()
            wid = n if not s else n - s[-1] - 1
            ans = max(ans,arr[top]*wid)
        return ans