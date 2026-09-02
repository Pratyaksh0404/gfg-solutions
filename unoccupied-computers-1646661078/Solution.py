class Solution:
    def solve(self, n, s):
        assigned = set()
        r = set()
        ans = 0
    
        for c in s:
            if c in r:
                continue
            if c in assigned:
                assigned.remove(c)
            elif len(assigned) < n:
                assigned.add(c)
            else:
                r.add(c)
                ans += 1
    
        return ans