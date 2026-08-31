class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        tot = 0
        curr = st = 0
        for i in range(n):
            curr += gas[i] - cost[i]
            tot += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                st = i+1
        if tot < 0:
            return -1
    
        return st
