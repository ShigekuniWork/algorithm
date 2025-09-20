class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I iterate through list to efficiently solve this problem more than brute force.
        # Iterate and check max profit and update grater than profit.
        
        # if prices list is empty, profit is 0
        if prices is None:
            return 0
        
        # default maximum profit is 0
        max_profit = 0
        
        # I keep minimal buy price for calculate profit
        buy_price = prices[0]
        
        # Iterate from 1 index
        for current_price in prices[1:]:
            # check weather less than maximum buy price
            buy_price = min(current_price, buy_price)
            
            # update maximum profit
            profit = current_price - buy_price
            max_profit = max(profit, max_profit)
        
        return max_profit
            