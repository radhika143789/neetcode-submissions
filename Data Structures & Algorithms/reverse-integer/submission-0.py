class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)  # -2147483648
        INT_MAX = 2**31 - 1  # 2147483647
        sign = 1
        if x < 0:
         sign = -1
        rev_str =str(abs(x))[::-1]
        rev_num = sign * int(rev_str)
        if rev_num < INT_MIN or rev_num >INT_MAX:
         rev_num = 0
        return rev_num