class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: check if curr price is less than the curr min_price
        # if yes: set min_price = curr price
        # if no: compare curr price - min_price > max_prof

        max_prof = 0
        min_price = prices[0]

        for curr_price in prices:
            if curr_price < min_price:
                min_price = curr_price
            
            if curr_price - min_price > max_prof:
                max_prof = curr_price - min_price

        return max_prof