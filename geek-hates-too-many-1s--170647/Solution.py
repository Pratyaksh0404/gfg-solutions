class Solution:
    def maxValue(self, n: int) -> int:
        s = bin(n)[2:]
        while "111" in s:
            idx = s.find("111")
            s = s[:idx + 2] + "0" + s[idx + 3:]
            
        return int(s, 2)