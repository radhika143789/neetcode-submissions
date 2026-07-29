class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            
        # Step 2: Group numbers by their frequency
        # Index = frequency, Value = list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq_map.items():
            buckets[count].append(num)
            
        # Step 3: Gather the top k frequent elements from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result