class Solution:
    def nthRoot(self, n, m):
        low, high = 0, m
    
        while low <= high:
            mid = (low + high) // 2
    
            v = 1
            for _ in range(n):
                v *= mid
                if v > m:
                    break
    
            if v == m:
                return mid
            elif v < m:
                low = mid + 1
            else:
                high = mid - 1
    
        return -1