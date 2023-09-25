#LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices):
    max_profit = 0
        min_price = prices[0]
    
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
    
        return max_profit
-------------------------------------
class Solution:
    def maxProfit(prices):
        if not prices:
            return 0  # If there are no prices, there's no profit to be made
    
        min_price = prices[0]  # Initialize the minimum price to the first day's price
        max_profit = 0  # Initialize the maximum profit to 0
    
        for price in prices:
            # Update the minimum price if we find a lower price
            min_price = min(min_price, price)
            
            # Calculate the profit we would make by selling at the current price
            current_profit = price - min_price
            
            # Update the maximum profit if the current profit is higher
            max_profit = max(max_profit, current_profit)
    
        return max_profit
        -------------------
Explanation:

We start by initializing min_price to the price on the first day and max_profit to 0.
We then iterate through the prices array, starting from the second day (index 1). For each day's price:
We update min_price if we find a lower price. This ensures that min_price always represents the lowest price seen so far.
We calculate the profit we would make by selling at the current price, which is price - min_price. This represents the profit 
                                                               if we buy at min_price and sell at the current price.
We update max_profit to be the maximum of the current max_profit and current_profit. This step ensures that max_profit always 
                                                               contains the maximum profit seen so far.
After iterating through all prices, max_profit will contain the maximum profit that can be achieved by buying and selling the 
                       stock once.
We return max_profit as the final result.
This solution has a time complexity of O(n) because we iterate through the prices array once, where n is the number of days. It efficiently finds the maximum profit by keeping track of the minimum price and the maximum profit seen so far during the iteration.

