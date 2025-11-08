prices = [12.5, 9.9, 15.0, 22.3, 5.0]
quantities = [2, 5, 1, 3, 4]

totals = list(map(lambda p_q: p_q[0] * p_q[1], zip(prices, quantities)))
high_totals = list(filter(lambda x: x > 30, totals))
paired = list(zip(prices, quantities))

print("Prices:", prices)
print("Quantities:", quantities)
print("Totals:", totals)
print("High totals (>30):", high_totals)
print("Paired (price, quantity):", paired)
