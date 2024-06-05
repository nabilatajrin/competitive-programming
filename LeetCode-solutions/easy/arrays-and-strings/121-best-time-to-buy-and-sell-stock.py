Understand the Problem: We are given an array where each number represents the price of a stock on a particular day. We need to find the maximum profit we can make by buying and selling one share of that stock.

Think of a Simple Example: Let's say we have [7, 1, 5, 3, 6, 4]. We want to buy when the price is low and sell when the price is high. The lowest price here is 1, and the highest price after it is 6. So, we buy at 1 and sell at 6, making a profit of 5.

Find a Strategy: One way to approach this is by keeping track of the minimum price we've seen so far and updating the maximum profit as we iterate through the array.

Explain the Code:

python
Copy code
def maxProfit(prices):
    if len(prices) < 2:  # If there are fewer than 2 days, we can't make any profit.
        return 0
        
    min_price = prices[0]  # Assume the first day's price is the lowest.
    max_profit = 0  # We start with 0 profit.
    
    for price in prices:
        if price < min_price:  # If we find a lower price, update min_price.
            min_price = price
        elif price - min_price > max_profit:  # If the profit by selling on this day is more than the previous max_profit, update max_profit.
            max_profit = price - min_price
            
    return max_profit  # Return the maximum profit we found.

# Test the function
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output should be 5
Run Through the Code with an Example: We start with the first price, 7, assuming it's the lowest so far. Then we check each price, updating the minimum price if we find a lower one. If the profit by selling on a certain day is higher than what we've seen before, we update the maximum profit.

Explain the Output: The output is 5, which means the maximum profit we can make with this set of prices is 5.

So, to sum it up, we're finding the lowest price to buy and the highest price to sell to maximize profit.

-------------------------------------------------------------------------------------------------------------------------------------------------------
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

