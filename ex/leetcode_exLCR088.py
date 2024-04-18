class Solution:
    def minCostClimbingStairs(self, cost: list[int]):
        ans = [0] * (len(cost)+1)
        for i in range(2,len(cost)+1):
            ans[i] = min(ans[i-2] + cost[i-2],ans[i-1] + cost[i-1])
        return ans[len(cost)]