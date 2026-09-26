class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for c in nums:
            for t in range(c, target + 1):
                for comb in dp[t - c]:
                    dp[t].append(comb + [c])
        return dp[target]
        