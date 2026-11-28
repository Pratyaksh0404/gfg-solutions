from collections import deque


class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        visited = [False] * len(adj)
        queue = deque([u])
        visited[u] = True

        while queue:
            curr = queue.popleft()
            if curr == v:
                return True
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
    
    