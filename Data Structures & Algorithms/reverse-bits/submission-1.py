class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = bin(n)[2:].zfill(32)
        int_rev = 0 
        for i in range(len(str_n)):
            if str_n[i] == "1":
                int_rev += 2**i
        return int_rev



        