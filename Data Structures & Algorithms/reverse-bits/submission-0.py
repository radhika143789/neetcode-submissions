class Solution:
    def reverseBits(self, n: int) -> int:
        res =0
        for i in range(32):
           # 1. Extract the bit at position i
            bit = (n >> i) & 1
            
            # 2. If the bit is 1, set the bit at position (31 - i) in res
            if bit:
                res |= (1 << (31 - i))
        return res
        