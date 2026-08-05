class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. Merge the two arrays
        merged = nums1 + nums2
        
        # 2. Sort the combined array
        merged.sort()
        
        n = len(merged)
        mid = n // 2
        
        # 3. If the total length is odd, return the exact middle value
        if n % 2 != 0:
            return float(merged[mid])
        # 4. If the total length is even, return the average of the two middle values
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0