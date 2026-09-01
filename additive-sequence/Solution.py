class Solution:
    def isSumString (self, s):
        n = len(s)
    
        def solve1(num):
            return len(num) == 1 or num[0] != '0'
    
        def solve(a, b, rem):
            if not rem:
                return True
            ss = str(int(a) + int(b))
            if rem.startswith(ss):
                return solve(b, ss, rem[len(ss):])
            return False
    
        for i in range(1, n):
            for j in range(i+1, n):
                a, b = s[:i], s[i:j]
                if solve1(a) and solve1(b):
                    if solve(a, b, s[j:]):
                        return True
                        
        return False