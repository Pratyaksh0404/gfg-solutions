from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
        if knightPos[0] == targetPos[0] and knightPos[1] == targetPos[1]:
            return 0

        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]

        queue = deque([(knightPos[0], knightPos[1], 0)])
        visited = [[False] * (n + 1) for _ in range(n + 1)]
        visited[knightPos[0]][knightPos[1]] = True

        while queue:
            x, y, moves = queue.popleft()

            if x == targetPos[0] and y == targetPos[1]:
                return moves

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, moves + 1))

        return -1