class Solution:
    def reverse(self, x: int) -> int:
        min_ = -(2**31)
        max_ = (2**31) - 1
        new_ = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while x:
            new_ = new_*10 + (x%10)
            x //= 10
        new_ = -new_ if neg else new_
        return 0 if new_ < min_ or new_ > max_ else new_