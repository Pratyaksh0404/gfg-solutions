from itertools import zip_longest

class Solution:
    def findSum(self, s1: str, s2: str) -> str:
        carry = 0
        res = []
        for d1, d2 in zip_longest(reversed(s1), reversed(s2), fillvalue='0'):
            carry, digit = divmod(int(d1) + int(d2) + carry, 10)
            res.append(str(digit))
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res)).lstrip('0') or '0'