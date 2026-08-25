class Solution:
    def minMoves(self, arr):
        pos = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            pos[x] = i
    
        l = 1
        curr = 1
    
        for x in range(2, len(arr) + 1):
            if pos[x] > pos[x - 1]:
                curr += 1
            else:
                curr = 1
            l = max(l, curr)
    
        return len(arr) - l