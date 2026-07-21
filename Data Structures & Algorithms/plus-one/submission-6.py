class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        ret=[]
        for i in digits:
            sum+=i
            sum*=10
        sum=sum//10
        sum+=1
        sum=str(sum)
        sum=list(sum)
        for i in range(len(sum)):
            sum[i]=int(sum[i])
        return sum
            

        