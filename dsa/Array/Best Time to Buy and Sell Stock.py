class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize min_price to a very large number (infinity)
        # It will keep track of the lowest price seen so far (best day to buy)
        min_price = float('inf')

        # Initialize max_profit to 0
        # This will store the maximum profit found during the loop
        max_profit = 0 

        # Loop through each price in the list (one price per day)
        for price in prices:
            # If today's price is lower than the lowest seen so far, update min_price
            # This becomes the new best day to buy
            if price < min_price:
                min_price = price

            # Otherwise, calculate the profit if bought at min_price and sold today
            else:
                profit = price - min_price

                # If this profit is greater than the current max_profit, update it
                max_profit = max(max_profit, profit)  # You can also write this way for quick use

        # Return the best profit found
        return max_profit


# 🧠 Quick Revision Key Points:
# min_price → Track the best buying price so far.

# max_profit → Track the best profit possible so far.

# Always buy before you sell (i.e., maintain the order in the array).

# Time Complexity: O(n) → One loop through the array.

# Let me know if you want a commented version of the multiple transactions variant too (Best Time to Buy and Sell Stock II).







