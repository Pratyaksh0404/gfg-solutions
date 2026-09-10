class Solution:
    def longestCommonPrefix(self, arr):
        ans = ''
        for i in range(len(arr[0])):
            for j in range(1, len(arr)):
                if i >= len(arr[j]) or arr[0][i] != arr[j][i]:
                    return ans

            ans += arr[0][i]

        return ans
