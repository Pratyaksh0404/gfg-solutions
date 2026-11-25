class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = a - b

        def floor_prefix_sum(n: int, div: int) -> int:
            if n < 0:
                return 0
            cnt = (n + 1) // div
            rem = (n + 1) % div
            return div * cnt * (cnt - 1) // 2 + rem * cnt

        def sum_ceil_div(lo_y: int, hi_y: int, div: int) -> int:
            if lo_y > hi_y:
                return 0
            total_terms = hi_y - lo_y + 1
            extra = floor_prefix_sum(hi_y - 1, div) - floor_prefix_sum(lo_y - 2, div)
            return total_terms + extra

        if d <= a:
            t_normal = d
        else:
            k_d = (d - a + c - 1) // c
            t_normal = d + 2 * b * k_d

        def t_jump_val(target: int) -> int:
            if target <= a:
                return target + 1
            k = (target - a + c - 1) // c
            return target + 1 + 2 * b * k

        lo_t = d - r
        hi_t = d - l

        ans = 0

        if lo_t <= a:
            end_le_a = min(hi_t, a)
            cnt_le_a = end_le_a - lo_t + 1
            sum_t_le_a = (lo_t + end_le_a) * cnt_le_a // 2
            ans += sum_t_le_a + cnt_le_a

        start_gt_a = max(lo_t, a + 1)
        if start_gt_a <= hi_t:
            left = start_gt_a - 1
            right = hi_t
            while left < right:
                mid = (left + right + 1) // 2
                if t_jump_val(mid) <= t_normal:
                    left = mid
                else:
                    right = mid - 1
            cut = left

            if cut >= start_gt_a:
                cnt_c = cut - start_gt_a + 1
                sum_t_c = (start_gt_a + cut) * cnt_c // 2
                sum_k_c = sum_ceil_div(start_gt_a - a, cut - a, c)
                ans += sum_t_c + (1 + 2 * b) * cnt_c + 2 * b * (sum_k_c - cnt_c)

            if hi_t > cut:
                ans += (hi_t - cut) * t_normal

        return ans % MOD