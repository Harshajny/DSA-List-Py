
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Initialize min_price to a very high value
        # and max_profit to 0 (since we return 0 if no profit is found)
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 2. Update the minimum price we've seen so far
            if price < min_price:
                min_price = price
            
            # 3. Calculate profit if we sold today at current price
            # and compare it to the best profit we've found so far
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit