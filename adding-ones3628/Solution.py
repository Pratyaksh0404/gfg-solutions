class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        freq = [0] * (n + 2)
        for j in updates:
            freq[j] += 1

        arr = [0] * n
        curr = 0
        for i in range(1, n + 1):
            curr += freq[i]
            arr[i - 1] = curr

        return arr