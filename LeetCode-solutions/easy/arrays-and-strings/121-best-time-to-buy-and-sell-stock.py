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
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')  # Set the initial minimum price to positive infinity.

        for price in prices:
            # Imagine you are riding a roller coaster!
            if price < min_price:
                # Woohoo! We found a new dip in the roller coaster. Let's update the minimum price.
                min_price = price
            elif price - min_price > max_profit:
                # Whee! We found a peak after the dip, and it gives us a higher profit!
                max_profit = price - min_price

        return max_profit
------------------------------

Input:
[7,1,5,3,6,4]

Output:
5
Expected
5
------------------------------

Explanation:
1. The function maxProfit takes a list prices as input, representing the stock prices on different days.
2. It initializes maxProfit variable to 0, which will keep track of the maximum profit we can achieve.
3. It sets min_price to positive infinity (float('inf')) as an initial placeholder for the minimum price. 
     We can think of this as the lowest point of the roller coaster ride.
4. The function then goes through each price in the prices list.
5. It imagines that you are riding a roller coaster. When the price goes down (you encounter a dip), 
it gets excited and updates the min_price to the current price.
6. When the price goes up (you reach a peak after a dip), it checks if the difference between the current 
price and the min_price gives a higher profit than the current max_profit. If it does, the function 
updates max_profit with the new higher value.
7. After looping through all the prices, the function returns the max_profit, which represents the maximum 
profit you can achieve by buying at the lowest point (dip) and selling at the highest point (peak) in the roller coaster ride of stock prices.
