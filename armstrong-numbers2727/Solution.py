class Solution:
    def armstrongNumber(self, n):
        d1 = n // 100
        d2 = (n // 10) % 10
        d3 = n % 10
        return d1**3 + d2**3 + d3**3 == n