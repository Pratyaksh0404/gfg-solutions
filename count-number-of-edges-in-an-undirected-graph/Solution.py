class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        ans = 0
        for i in adj:
            ans += len(i)
            
        return ans // 2