class Solution:
    def getDivisors(self, n):
        s = []
        l = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                s.append(i)
                if i * i != n:
                    l.append(n // i)
            i += 1
            
        return s + l[::-1]