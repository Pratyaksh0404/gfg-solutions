class Solution:
    def longestPath(self, s, edges):
        n = len(s)
        same_adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] == s[v]:
                same_adj[u].append(v)
                same_adj[v].append(u)

        order = []
        parent = [-1] * n
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                q = [i]
                visited[i] = True
                head = 0
                while head < len(q):
                    u = q[head]
                    head += 1
                    order.append(u)
                    for v in same_adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            parent[v] = u
                            q.append(v)

        down1 = [1] * n
        down2 = [1] * n
        c_down = [-1] * n

        for u in reversed(order):
            for v in same_adj[u]:
                if v == parent[u]:
                    continue
                val = down1[v] + 1
                if val > down1[u]:
                    down2[u] = down1[u]
                    down1[u] = val
                    c_down[u] = v
                elif val > down2[u]:
                    down2[u] = val

        up = [1] * n
        for u in order:
            for v in same_adj[u]:
                if v == parent[u]:
                    continue
                if c_down[u] == v:
                    up[v] = max(up[u] + 1, down2[u] + 1)
                else:
                    up[v] = max(up[u] + 1, down1[u] + 1)

        dist = [max(down1[i], up[i]) for i in range(n)]

        ans = max(dist) if n > 0 else 0

        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] != s[v]:
                ans = max(ans, dist[u] + dist[v])

        return ans
    