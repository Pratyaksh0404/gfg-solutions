class Solution:
    def isBinary(self, s):
        a = ['2','3','4','5','6','7','8','9']
        for i in a:
            if i in s:
                return False
        return True
        
        