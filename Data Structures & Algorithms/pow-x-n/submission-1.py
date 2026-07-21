class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x == 0 :return 0
            if n ==0 :return 1
            power = helper(x*x,n//2)
            return x * power if n %2 else power
        power = helper(x, abs(n))
        return power if n>0 else 1/power

        