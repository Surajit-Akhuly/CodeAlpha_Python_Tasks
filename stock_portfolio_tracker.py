# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 300,
    "AMZN": 3500
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!\n")

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try another.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_value += stock_prices[stock] * quantity

# Display result
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}")
print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to .txt file
with open("portfolio_summary.txt", "w") as file:
    file.write("Your Portfolio Summary:\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
    file.write(f"\nTotal Investment Value: ${total_value}\n")

print("\nSummary saved to 'portfolio_summary.txt'.")
