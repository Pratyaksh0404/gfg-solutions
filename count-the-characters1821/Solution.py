class Solution:
    def getCount (self, s, k):
        n = len(s)
        gg = [0] * 26
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = ord(s[i]) - ord('a')
            gg[ch] += 1
            i = j

        ans = 0
        for i in gg:
            if i == k:
                ans += 1
                
        return ans