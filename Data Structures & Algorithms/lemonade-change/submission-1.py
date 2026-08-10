class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                # No change needed, just collect the $5 bill
                fives += 1
                
            elif bill == 10:
                # Need to give $5 in change
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
                    
            elif bill == 20:
                # Need to give $15 in change
                # Priority 1: Give one $10 and one $5 (saves your versatile $5 bills)
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                # Priority 2: Give three $5 bills
                elif fives >= 3:
                    fives -= 3
                # Cannot make change
                else:
                    return False
                    
        # If we make it through the whole loop without returning False, we succeeded!
        return True