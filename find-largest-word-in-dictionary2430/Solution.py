from collections import defaultdict
import bisect

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        ans = ""
        for word in d:
            curr = -1
            possible = True
            for ch in word:
                idx = bisect.bisect_right(pos[ch], curr)
                if idx == len(pos[ch]):
                    possible = False
                    break
                curr = pos[ch][idx]

            if possible:
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans