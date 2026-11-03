class Solution:
    def maximumWeight(self, n, edges, queries):
        edges.sort(key=lambda x: x[2])
        sorted_q = sorted((q, i) for i, q in enumerate(queries))

        parent = list(range(n + 1))
        sz = [1] * (n + 1)

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        ans = [0] * len(queries)
        edge_idx = 0
        total_paths = 0
        m = len(edges)

        for q, orig_idx in sorted_q:
            while edge_idx < m and edges[edge_idx][2] <= q:
                u, v, _ = edges[edge_idx]
                root_u, root_v = find(u), find(v)
                if root_u != root_v:
                    total_paths += sz[root_u] * sz[root_v]
                    if sz[root_u] < sz[root_v]:
                        root_u, root_v = root_v, root_u
                    parent[root_v] = root_u
                    sz[root_u] += sz[root_v]
                edge_idx += 1
            ans[orig_idx] = total_paths

        return ans