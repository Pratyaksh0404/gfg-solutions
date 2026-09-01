class Solution:
    def remConsonants(self, s):
        v = 'aAeEiIoOuU'
        for i in s:
            if i not in v:
                s = s.replace(i,'')
        return s
        