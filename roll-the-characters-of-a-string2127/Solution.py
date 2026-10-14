class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        diff = [0] * (n + 1)
        for r in roll:
            diff[0] += 1
            if r < n:
                diff[r] -= 1

        ans = []
        curr = 0
        for i in range(n):
            curr += diff[i]
            shift = curr % 26
            nc = chr(ord('a') + (ord(s[i]) - ord('a') + shift) % 26)
            ans.append(nc)

        return "".join(ans)