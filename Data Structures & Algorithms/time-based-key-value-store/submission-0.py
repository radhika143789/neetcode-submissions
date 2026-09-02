import collections
class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append((timestamp , value))
    def get(self, key: str, timestamp: int) -> str:
        # Default return value if no valid timestamp is found
        res = ""
        
        # If the key doesn't exist, we can immediately return ""
        if key not in self.store:
            return res
            
        values = self.store[key]
        
        # Binary search to find the largest timestamp_prev <= timestamp
        left, right = 0, len(values) - 1
        
        while left <= right:
            # Prevents integer overflow in languages other than Python
            mid = left + (right - left) // 2 
            
            if values[mid][0] <= timestamp:
                # We found a valid candidate, but there might be a closer one to the right
                res = values[mid][1]
                left = mid + 1
            else:
                # The timestamp at mid is strictly greater than our target
                right = mid - 1
                
        return res
