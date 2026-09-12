import math
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        g = math.gcd(a, b)
        l = (a * b) // g
        return [l, g]
    