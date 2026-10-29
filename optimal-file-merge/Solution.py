import heapq

class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        ans = 0

        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)

            cost = first + second
            ans += cost

            heapq.heappush(files, cost)

        return ans