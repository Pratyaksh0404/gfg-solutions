class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        s = list(s)

        for i in range(n // 2):
            left = s[i]
            right = s[n - 1 - i]

            if left != '?' and right != '?':
                if left != right:
                    return -1
            elif left != '?':
                s[n - 1 - i] = left
            elif right != '?':
                s[i] = right

        half_len = (n + 1) // 2
        known_chars = []
        for i in range(half_len):
            if s[i] != '?':
                known_chars.append(s[i])

        if not known_chars:
            return 0

        ans = 0
        for i in range(len(known_chars) - 1):
            ans += abs(ord(known_chars[i]) - ord(known_chars[i + 1]))

        return ans * 2