from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursToEat(rate: int) -> int:
            return sum([ceil(pile / rate) for pile in piles])
        
        l, r = 1, max(piles)
        h_best = l

        while l <= r:
            m = (l + r) // 2
            hours = hoursToEat(m)

            if hours > h:
                l = m + 1
            elif hours <= h:
                h_best = m
                r = m - 1
        
        return h_best
        