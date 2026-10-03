class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 4 * n
        coil1 = [1]
        r, c = 0, 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d = 0

        steps_pattern = [m - 1] + [m - 2 * i for i in range(1, 2 * n) for _ in range(2)]

        for steps in steps_pattern:
            dr, dc = dirs[d]
            for _ in range(steps):
                r += dr
                c += dc
                coil1.append(r * m + c + 1)
            d = (d + 1) % 4

        coil2 = [m * m + 1 - x for x in coil1]

        return [coil1, coil2]