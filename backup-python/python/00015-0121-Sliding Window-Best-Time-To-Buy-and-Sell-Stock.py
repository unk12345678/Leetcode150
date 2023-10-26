"""
Problem Description:
Given an array of stock prices where prices[i] is the price of a given stock on day i, determine the maximum profit that can be achieved. 
You are only allowed to complete one transaction (i.e., buy one and sell one share of the stock).

Approach:
1. Traverse through the price list.
2. Maintain a variable to keep track of the minimum price so far.
3. For every price, calculate the profit (current price minus the minimum price so far).
4. Update the maximum profit if the current profit is greater.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If there are fewer than 2 prices, we cannot perform any transaction
        if len(prices) < 2:
            return 0
        
        maxP = 0  # Stores the maximum profit
        curP = 0  # Stores the current profit
        minPrice = prices[0]  # Stores the minimum price so far

        # Iterate through the prices starting from the second day
        for price in prices[1:]:
            # Update the minimum price if the current price is lower
            minPrice = min(price, minPrice)
            # Calculate the profit for the current day
            curP = price - minPrice
            # Update the maximum profit if the current profit is greater
            maxP = max(maxP, curP)

        return maxP  # Return the maximum profit

# Time Complexity:
# O(n), where n is the length of the prices list.
# Each element in the list is visited once.

# Space Complexity:
# O(1), constant space is used since only a few variables are utilized.

