class Solution:
    def findConvexHull(self, points):
        pts = list(set(tuple(p) for p in points))
        n = len(pts)
        if n < 3:
            return [[-1]]

        pts.sort()

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        hull = lower[:-1] + upper[:-1]

        if len(hull) < 3:
            return [[-1]]

        return [list(p) for p in hull]