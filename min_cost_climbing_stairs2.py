class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        def solve(i):
            if i==0 or i==1:
                return cost[i]
            return cost[i]+min(solve(i-1),solve(i-2))
        return min(solve(n-1),solve(n-2))
