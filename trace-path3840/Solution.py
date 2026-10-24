class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        min_r, max_r = 0, 0
        min_c, max_c = 0, 0
        cur_r, cur_c = 0, 0

        for char in s:
            if char == 'L':
                cur_c -= 1
            elif char == 'R':
                cur_c += 1
            elif char == 'D':
                cur_r -= 1
            elif char == 'U':
                cur_r += 1

            min_r = min(min_r, cur_r)
            max_r = max(max_r, cur_r)
            min_c = min(min_c, cur_c)
            max_c = max(max_c, cur_c)

        height = max_r - min_r + 1
        width = max_c - min_c + 1

        return height <= n and width <= m