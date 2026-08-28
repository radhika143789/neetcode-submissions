class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency ={}
        for string in arr:
            frequency[string] = frequency.get(string ,0)+1
        for string in arr :
            if frequency[string]==1:
                k-=1
                if k==0:
                    return string
        return ""
                
        
        
        