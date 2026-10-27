class Solution:
    def getMaxWeight(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        n1 = 0  
        n2 = 0  

        for i in range(n - 1, -1, -1):
            curr = 1 + n1

            if i + 1 < n:
                p = 4 if s[i] != s[i+1] else 3
                curr = max(curr, p + n2)

            n2 = n1
            n1 = curr

        return n1