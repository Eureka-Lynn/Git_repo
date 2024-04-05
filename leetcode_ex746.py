class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
            l = len(cost)
            c = [0] * (l+1)
            for i in range(2,l+1):
                c[i] = min(c[i-2] + cost[i-2],c[i-1]+cost[i-1])
            return c[l]