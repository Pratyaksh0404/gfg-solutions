class Solution:
    def findMax(self, n):
        s = list(str(n))
        m = len(s)
        ans = n
        maxi = sum(int(d) for d in s)

        for i in range(m):
            if s[i] == '0':
                continue

            cst = "".join(s[:i]) + str(int(s[i]) - 1) + "9" * (m - 1 - i)
            c = int(cst)
            c_sum = sum(int(d) for d in str(c))

            if c_sum > maxi or (c_sum == maxi and c > ans):
                maxi = c_sum
                ans = c

        return ans