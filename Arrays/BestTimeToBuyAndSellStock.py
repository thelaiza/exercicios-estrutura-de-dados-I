# Link: leetcode.com/problems/best-time-to-buy-and-sell-stock
# Nivel Fácil - Complexidade de tempo: O(n); Complexidade de espaço: O(1)

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit


# Testes
print(maxProfit([7,1,5,3,6,4]))  # 5
print(maxProfit([7,6,4,3,1]))    # 0