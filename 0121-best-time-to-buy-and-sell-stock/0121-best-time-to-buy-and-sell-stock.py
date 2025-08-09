class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 1 <= prices.length <= 105
        buy_price = prices[0]

        for price in prices[1::]:
            if price < buy_price:
                buy_price = price
            else:
                result = max(result, price - buy_price)

        return result 

