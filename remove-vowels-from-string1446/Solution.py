class Solution:
	def removeVowels(self, s):
		# code here
		vow = ['a','e','i','o','u']
		return "".join(c for c in s if c not in vow)