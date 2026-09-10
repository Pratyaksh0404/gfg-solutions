class Solution:
    def roundToNearest(self, s): 
        n = len(s)
        l = int(s[-1])
    
        if l <= 5:
            return s[:-1] + '0'
    
        sl = list(s)
        sl[-1] = '0'
    
        i = n - 2
        while i >= 0 and sl[i] == '9':
            sl[i] = '0'
            i -= 1
    
        if i >= 0:
            sl[i] = str(int(sl[i]) + 1)
            return "".join(sl)
        else:
            return "1" + "".join(sl)
