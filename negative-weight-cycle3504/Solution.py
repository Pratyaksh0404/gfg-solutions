class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        d = [0] * V
        
        for _ in range(V - 1):
            f = False
            for u, v, w in edges:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    f = True
            if not f:
                return False
    
        for u, v, w in edges:
            if d[u] + w < d[v]:
                return True
                
        return False