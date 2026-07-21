class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        le =   0x7FFFFFFF
        while b!=0:

            tem= (a^b)&mask
            b= ((a&b)<<1)&mask
            a= tem
        return a if a<=le else ~(a^mask)

