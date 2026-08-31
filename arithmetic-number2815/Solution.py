class Solution:
    def inSequence(self, a, b, c):
        n = (b-a)/c + 1
        if int(n)==n:
            return True
        else:
            return False
        