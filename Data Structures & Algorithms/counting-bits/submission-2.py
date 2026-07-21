class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * n
        dp = [0, 1, 1, 2, 1]
        if n <= 4:
            return dp[:n+1]
        offset = 4
        for i in range(5, n+1):
            if offset * 2 == i:
                offset = i
            dp.append(1 + dp[i-offset])
        return dp