# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = prices[0] if prices else 0
        profits = [0]
        for i in range(1, len(prices)):
            profits.append(max(prices[i] - min_value, 0))

            if prices[i] < min_value:
                min_value = prices[i]

        return max(profits)
