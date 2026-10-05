class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            check = 0
            for p in piles:
                check += -(p // -mid)
            if check <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer