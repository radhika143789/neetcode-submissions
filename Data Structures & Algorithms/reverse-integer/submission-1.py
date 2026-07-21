class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = 1 if x > 0 else -1
        new_x = abs(x)

        while new_x > 0:
            digit = new_x % 10
            num = num * 10 + digit
            new_x //= 10

        num *= sign
        
        if -2 ** 31 > num or num > 2 ** 31 - 1:
            return 0
        
        return num


        