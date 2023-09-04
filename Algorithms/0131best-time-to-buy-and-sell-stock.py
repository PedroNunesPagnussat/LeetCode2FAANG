from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell < buy:
                buy = sell
            elif sell - buy > profit:
                profit = sell - buy

        return profit
    

    def bruteForce(self, prices: List[int]) -> int:
        profit = 0
        for i, buy in enumerate(prices):
            for sell in prices[i:]:
                if  sell - buy > profit:
                    profit = sell - buy

    

if __name__ == "__main__":
    prices = [1, 2]
    solution = Solution()
    answer = solution.maxProfit(prices)
    print(answer)