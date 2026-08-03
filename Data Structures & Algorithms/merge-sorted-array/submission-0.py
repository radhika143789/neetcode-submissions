class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for the end of valid elements in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # Pointer for the last available slot in the entire nums1 array
        p = m + n - 1

        # Compare elements from the back and move the larger one to the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in nums2, copy them over.
        # Note: If p1 >= 0 elements are left, they are already in their correct places.
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1