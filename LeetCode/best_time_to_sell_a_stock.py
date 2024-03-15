
prices = [3, 10, 2, 6]

# best_profit = 0
# for buy_day in range(0, len(prices) - 1):
#     for sell_day in range(buy_day + 1, len(prices)):
#         profit = prices[sell_day] - prices[buy_day]
#         print(f'{prices[sell_day]} {prices[buy_day]} {profit}')
#         if profit > best_profit:
#             best_profit = profit




profit = 0
buy = prices[0]
for sell in prices[1:]:
    if sell > buy:
        profit = max(profit, sell - buy)
    else:
        buy = sell

print(f'The best profit is {profit}')
