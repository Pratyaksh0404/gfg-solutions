class Solution:
    def nthTerm(self, a, r, n):
        mod = 10**9 + 7
        return (a % mod * pow(r, n - 1, mod)) % mod