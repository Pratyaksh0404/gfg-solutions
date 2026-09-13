class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        def bfs(src):
            dist = [-1] * len(adj)
            dist[src] = 0
            q = [src]
            for u in q:
                for v in adj[u]:
                    v -= 1
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            far = max(range(len(adj)), key=dist.__getitem__)
            return far, dist[far]

        a, _ = bfs(0)
        _, d = bfs(a)
        
        return (d + 1) // 2