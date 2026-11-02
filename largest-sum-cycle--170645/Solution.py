class Solution:
    def largestSumCycle(self, edge: list[int]) -> int:
        n = len(edge)
        vis = [0] * n
        ans = -1

        for i in range(n):
            if vis[i] == 0:
                curr = i
                path = {}
                step = 0
                while curr != -1 and vis[curr] == 0:
                    vis[curr] = i + 1
                    path[curr] = step
                    step += 1
                    curr = edge[curr]

                if curr != -1 and vis[curr] == i + 1:
                    cc = path[curr]
                    cs = 0
                    for node, stp in path.items():
                        if stp >= cc:
                            cs += node
                    if cs > ans:
                        ans = cs

        return ans