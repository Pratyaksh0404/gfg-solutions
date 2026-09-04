class Solution:
    def segregateElements(self, arr):
        t = [x for x in arr if x >= 0]
        t += [x for x in arr if x < 0]
        
        arr[:] = t