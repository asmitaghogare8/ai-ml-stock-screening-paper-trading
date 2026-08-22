from paper_trading import PaperTrader


trader = PaperTrader(100000)

trader.buy("TESTSTOCK", 250)

trader.sell("TESTSTOCK", 255)

print("Final Balance:", trader.get_balance())

print("Trade History:")

for trade in trader.get_trade_history():
    print(trade)