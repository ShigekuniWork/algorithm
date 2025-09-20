from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We solve this in one pass instead of brute force.
        # We keep the lowest price so far and update the max profit as we go.

        # When the list is empty, profit is zero.
        if not prices:
            return 0

        # The profit starts at zero.
        max_profit = 0

        # The lowest price starts as the first price.
        min_price = prices[0]

        # Iterate through the list from the second price.
        for price in prices[1:]:
            # If it sells here, profit is current price minus the lowest.
            max_profit = max(max_profit, price - min_price)
            # Then it updates the lowest if this price is smaller.
            min_price = min(min_price, price)

        # In the end, we get the best profit.
        return max_profit

        # Time is O(n). Space is O(1).
