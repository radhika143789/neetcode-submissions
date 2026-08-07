import bisect

class Solution:
    def canShip(self, weights: List[int], days: int, maxWeight: int) -> bool:
        time = 0
        i, sz = 0, len(weights)

        while i<sz:
            left, right = i+1, sz-1
            time+=1
            i = bisect.bisect_right(weights, (weights[i-1]+maxWeight if i>0 else maxWeight))
            if time > days:
                break
        return time <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        for i in range(1, len(weights)):
            weights[i]+=weights[i-1]
        
        while left<right:
            mid = left + (right-left)//2
            if self.canShip(weights, days, mid):
                right = mid
            else:
                left = mid+1
        return left