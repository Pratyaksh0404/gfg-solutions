class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        a = arr[0]
        a2 = arr[0] * arr[0]
        ans = max(a, a2)

        for i in arr[1:]:
            a2 = max(a2 + i, (a if a > 0 else 0) + i * i, i * i)

            a = max(i, a + i)

            ans = max(ans, a, a2)

        return ans