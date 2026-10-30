class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0


        curr = 1

        for k in range(0, r + 1):
            if k > 0:
                cp = freq.get(k - 1, 0)
                wp = (pow2[cp] - 1) % MOD
                curr = (curr * wp) % MOD

            if curr == 0:
                break

            if k >= l:
                cnt_k = freq.get(k, 0)

                ele = 0
                for val in freq:
                    if val > k:
                        ele += freq[val]

                ww = pow2[ele]
                ways_k = (curr * ww) % MOD
                ans = (ans + ways_k) % MOD

            if freq.get(k, 0) == 0:
                break

        return ans