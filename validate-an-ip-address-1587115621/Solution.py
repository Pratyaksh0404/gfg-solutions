class Solution:
    def isValid(self, s):
        if s.count('.') != 3:
            return False
    
        p = s.split('.')
        if len(p) != 4:
            return False
    
        for i in p:
            if not i.isdigit():
                return False
    
            if len(i) > 1 and i[0] == '0':
                return False
    
            n = int(i)
            if n < 0 or n > 255:
                return False
    
        return True