class Solution:
    def minOperation(self, n):
        return n.bit_count() + n.bit_length() - 1