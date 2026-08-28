class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_nums = Counter(arr)

        for i in arr:
            if arr_nums.get(i) == 1:
                k-=1
            if k == 0:
                return i
        return ""