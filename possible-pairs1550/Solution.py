import math
class Solution:
    def pairCount(self, x, y):
        if y % x != 0:
            return 0

        k = y // x
        ans = 0

        for i in range(1, int(math.isqrt(k)) + 1):
            if k % i == 0:
                j = k // i
                if math.gcd(i, j) == 1:
                    ans += 1 if i == j else 2

        return ans