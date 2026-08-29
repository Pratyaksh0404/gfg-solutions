class Solution:
    def twoOddNum(self, arr):
        xor_sum = 0
        for num in arr:
            xor_sum ^= num
    
        rsb = xor_sum & -xor_sum
    
        a = 0
        b = 0
        for num in arr:
            if num & rsb:
                a ^= num
            else:
                b ^= num
    
        return [a, b] if a > b else [b, a]