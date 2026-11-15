class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        n = len(s)
        ans = sum(int(c) for c in s) % MOD
        m = pow(2, n - 1, MOD)
        
        return (ans * m) % MOD