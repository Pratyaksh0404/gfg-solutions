class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)

        mini = 0
        buy = 0
        free = n - 1
        while buy <= free:
            mini += prices[buy]
            buy += 1
            free -= k  

        maxi = 0
        prices.sort(reverse=True)
        buy = 0
        free = n - 1
        while buy <= free:
            maxi += prices[buy]
            buy += 1
            free -= k  

        return [mini, maxi]
