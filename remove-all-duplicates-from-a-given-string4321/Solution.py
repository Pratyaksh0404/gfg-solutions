class Solution:
	def removeDuplicates(self, s):
	    ans = ''
	    for i in s:
	        if i not in ans:
	            ans += ans.join(i)
	    return ans
	    