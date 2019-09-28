class Solution(object):
    def ccc(self, gas, cost):
        n = len(gas)
        totalgas, curr_tank = 0, 0
        start = 0
        for i in range(n):
            totalgas += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        return start if totalgas >= 0 else -1
'''
totalgas其实是记录总数和的，
totalgas只有在大于0的情况下才能保证绕一圈。
'''


    def simple(self, gas, cost):
        n = len(gas)
        if (sum(gas)-sum(cost)) < 0:
            return -1
        tank = 0
        idx = 0
        p = 0
        while True:
            tank += gas[p]
            if tank - cost[p] < 0:
                tank = 0
                idx = (p+1)%n
                p = idx
                continue
            tank -= cost[p]
            p = (p+1)%n
            if idx == p:
                return idx
