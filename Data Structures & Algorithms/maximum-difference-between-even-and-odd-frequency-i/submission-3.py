class Solution:
    def maxDifference(self, s: str) -> int:
        s=sorted(s)
        maxi_odd=0
        mini_odd=float('inf')
        maxi_even=0
        mini_even=float('inf')
        l=0
        r=0
        while r<len(s):
            while r<len(s) and s[l]==s[r]:
                r+=1
            tot=r-l
            if tot%2==0:
                mini_even=min(tot,mini_even)
            else:
                maxi_odd=max(tot,maxi_odd)
            l=r
        return maxi_odd-mini_even
            



        