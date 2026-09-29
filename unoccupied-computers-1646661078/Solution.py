class Solution:
    def solve(self, n, s):
        f = set()
        r = set()
        ans = 0

        for c in s:
            if c in r:
                continue
            if c in f:
                f.remove(c)
            elif len(f) < n:
                f.add(c)
            else:
                r.add(c)
                ans += 1

        return ans