class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [0] * (target + 1)

        for p, s in zip(position, speed):
            cars[p] = s
        
        fleets = 0
        max_time = .0

        for p in range(target, -1, -1):
            s = cars[p]

            if s == 0: continue
            t = (target-p)/s

            if t <= max_time:
                continue
            else:
                max_time = t
                fleets += 1 
        
        return fleets