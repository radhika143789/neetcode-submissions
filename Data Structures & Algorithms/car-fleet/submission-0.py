class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time_ahead = 0.0
        
        for p, s in cars:
            time_to_target = (target - p) / s
            
            # If the current car takes strictly longer to reach the target than the fleet ahead, 
            # it cannot catch up, thus forming a new fleet.
            if time_to_target > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time_to_target
                
        return fleets