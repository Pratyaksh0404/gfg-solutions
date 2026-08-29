class Solution:
    def bestNumbers(self, n, a, b, c, d):
        if a == b:
            sm = str(n * a)
            return 1 if str(c) in sm or str(d) in sm else 0
    
        M = 10**9 + 7
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] * i % M
    
        inv = [1] * (n + 1)
        inv[n] = pow(f[n], M - 2, M)
        for i in range(n - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % M
    
        ans = 0
        sc, sd = str(c), str(d)
        for i in range(n + 1):
            sm = str(i * a + (n - i) * b)
            if sc in sm or sd in sm:
                ans = (ans + f[n] * inv[i] * inv[n - i]) % M
        return ans