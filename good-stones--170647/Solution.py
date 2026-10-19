class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n

        def dfs(curr):
            if not (0 <= curr < n):
                return True
            if state[curr] != 0:
                return state[curr] == 1

            state[curr] = -1

            nxt = curr + arr[curr]

            is_good = dfs(nxt)

            state[curr] = 1 if is_good else 2
            return is_good

        for i in range(n):
            if state[i] == 0:
                dfs(i)

        return sum(1 for x in state if x == 1)