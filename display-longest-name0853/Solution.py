class Solution:
    def longest(self, arr):
        ans = arr[0]
        maxi = len(arr[0])

        for i in arr[1:]:
            if len(i) > maxi:
                maxi = len(i)
                ans = i

        return ans