class Solution:
    def countMinOperations(self, arr):
        inc = 0
        mx = 0
        for x in arr:
            inc += x.bit_count()
            if x > mx:
                mx = x
                
        return inc + (mx.bit_length() - 1 if mx else 0)