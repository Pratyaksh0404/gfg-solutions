class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        vowels = set("aeiou")
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if s[i] in vowels else 0)
        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] - pref[l])
            
        return ans