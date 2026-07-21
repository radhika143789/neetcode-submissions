class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # If we find a lower buying price, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit