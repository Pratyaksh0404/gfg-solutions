class Solution:
    def isSumString (self, s):
        n = len(s)
    
        def is_valid(num):
            return len(num) == 1 or num[0] != '0'
    
        def check(a, b, remaining):
            if not remaining:
                return True
            sum_str = str(int(a) + int(b))
            if remaining.startswith(sum_str):
                return check(b, sum_str, remaining[len(sum_str):])
            return False
    
        for i in range(1, n):
            for j in range(i+1, n):
                a, b = s[:i], s[i:j]
                if is_valid(a) and is_valid(b):
                    if check(a, b, s[j:]):
                        return True
        return False