from collections import Counter

class Solution:
    def areKAnagrams(self, s1, s2, k):
        if len(s1) != len(s2):
            return False
        return sum((Counter(s1) - Counter(s2)).values()) <= k