class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pair_map = {}
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s not in pair_map:
                    pair_map[s] = []
                pair_map[s].append((i, j))

        for a in range(n):
            for b in range(a + 1, n):
                s = arr[a] + arr[b]
                for c, d in pair_map.get(s, []):
                    if c != a and c != b and d != a and d != b:
                        if (a, b) < (c, d):
                            return [a, b, c, d]

        return [-1, -1, -1, -1]