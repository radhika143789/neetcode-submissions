class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

        n -= empty // 2 # If we end with a sequence of zeros calculate the flowers that fit

        return n <= 0

# Time complexity: O(n)
# Space complexity: O(1)