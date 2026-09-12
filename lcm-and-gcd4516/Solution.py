class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        x, y = a, b
        while y:
            x, y = y, x % y
        gcd = x
        lcm = (a * b) // gcd if gcd != 0 else 0
        return [lcm, gcd]
    