class Solution:
    def findPattern(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n:
            if s[i] != 'x':
                return False

            cnt_x = 0
            while i < n and s[i] == 'x':
                cnt_x += 1
                i += 1

            cnt_y = 0
            while i < n and s[i] == 'y':
                cnt_y += 1
                i += 1

            if cnt_x != cnt_y:
                return False

        return True