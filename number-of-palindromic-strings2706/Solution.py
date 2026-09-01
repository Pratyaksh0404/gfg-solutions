class Solution:
    def palindromicStrings(self, n, k):
        M, P = 10**9 + 7, [1]
        for i in range(k):
            P.append(P[-1] * (k - i) % M)
            
        return sum(P[(i + 1) // 2] for i in range(1, n + 1)) % M