class Solution:
    def socialNetwork(self, arr):
        ans = []
        n = len(arr) + 1
        for i in range(2, n + 1):
            f = []
            curr = i
            dist = 0
            while curr >= 2:
                curr = arr[curr - 2]
                dist += 1
                f.append((curr, dist))
            f.sort(key=lambda x: x[0])
            for j, d in f:
                ans.append([i, j, d])
                
        return ans