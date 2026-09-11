import math

class Solution:
    def sameMod(self, arr):
        first = arr[0]
        if all(x == first for x in arr):
            return -1

        g = 0
        for x in arr:
            diff = abs(x - first)
            if diff > 0:
                g = math.gcd(g, diff)

        ans = 0
        limit = int(math.isqrt(g))
        for i in range(1, limit + 1):
            if g % i == 0:
                ans += 1
                if i * i != g:
                    ans += 1

        return ans