class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            return sum(int(digit) ** 2 for digit in str(number))
            
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
