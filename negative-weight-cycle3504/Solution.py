class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        dist = [0] * V
        for _ in range(V - 1):
            f = False
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    f = True
            if not f:
                return False
    
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True
        return False