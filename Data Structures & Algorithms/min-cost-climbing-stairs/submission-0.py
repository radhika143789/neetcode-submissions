class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Step variables representing the min cost to reach the top 
        # starting from (i + 1) and (i + 2) steps ahead
        one, two = 0, 0
        
        # Iterate backward through the cost array
        for i in range(len(cost) - 1, -1, -1):
            current = cost[i] + min(one, two)
            two = one
            one = current
            
        # You can start at index 0 or index 1
        return min(one, two)