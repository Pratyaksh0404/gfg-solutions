from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dist[src] = 0
        dq = deque([src])

        while dq:
            u = dq.popleft()

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)

        return dist[dst] if dist[dst] != float('inf') else -1