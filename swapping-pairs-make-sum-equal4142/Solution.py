class Solution:
    def findSwapValues(self, a, b):
        diff = sum(a) - sum(b)
        if diff % 2 != 0:
            return False
    
        tar = diff // 2
        a.sort()
        b.sort()
    
        i, j = 0, 0
        n, m = len(a), len(b)
    
        while i < n and j < m:
            curr = a[i] - b[j]
            if curr == tar:
                return True
            elif curr < tar:
                i += 1
            else:
                j += 1
    
        return False