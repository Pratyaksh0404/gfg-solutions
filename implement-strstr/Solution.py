class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        if pat in txt:
            return txt.index(pat)
        else:
            return -1