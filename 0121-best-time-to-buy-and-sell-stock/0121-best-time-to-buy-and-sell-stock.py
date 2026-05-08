
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        max=0
        for price in prices:
            if(price<min):
                min=price
            current=price-min
            if(current>max):
                max=current
        return max