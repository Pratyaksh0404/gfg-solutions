from collections import deque


class Solution:

    def minTime(self, dur, dep):
        n = len(dur)
        adj = [[] for _ in range(n)]
        ii = [0] * n

        for u, v in dep:
            adj[u].append(v)
            ii[v] += 1

        q = deque([i for i in range(n) if ii[i] == 0])
        dist = [0] * n
        for i in range(n):
            dist[i] = dur[i]

        vis = 0

        while q:
            u = q.popleft()
            vis += 1
            for v in adj[u]:
                dist[v] = max(dist[v], dist[u] + dur[v])
                ii[v] -= 1
                if ii[v] == 0:
                    q.append(v)

        return max(dist) if vis == n else -1