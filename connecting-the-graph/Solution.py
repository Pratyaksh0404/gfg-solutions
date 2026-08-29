class Solution:
    def minEdgesReq(self, n, edges):
        if len(edges) < n - 1:
            return -1

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n
        ans = 0

        for i in range(n):
            if not vis[i]:
                ans += 1
                stack = [i]
                vis[i] = True

                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if not vis[v]:
                            vis[v] = True
                            stack.append(v)

        return ans - 1