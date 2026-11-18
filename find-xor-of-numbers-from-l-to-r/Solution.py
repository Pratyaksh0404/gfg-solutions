class Solution:
    def computeXOR(self, n: int) -> int:
        mod = n % 4
        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        else:
            return 0

    def findXOR(self, l: int, r: int) -> int:
        return self.computeXOR(r) ^ self.computeXOR(l - 1)