class PaperTrader:

    def __init__(self, initial_balance=100000):
        self.balance = initial_balance
        self.position = None
        self.entry_price = 0
        self.trade_history = []

    def buy(self, stock, price):
        if self.position is None:
            self.position = "BUY"
            self.entry_price = price

            print("Paper BUY:", stock)
            print("Entry Price:", price)

    def sell(self, stock, price):
        if self.position == "BUY":
            profit = price - self.entry_price

            self.balance += profit

            trade = {
                "stock": stock,
                "entry_price": self.entry_price,
                "exit_price": price,
                "profit_loss": profit
            }

            self.trade_history.append(trade)

            self.position = None
            self.entry_price = 0

            print("Paper SELL:", stock)
            print("Exit Price:", price)
            print("Profit/Loss:", profit)

            return profit

        return 0

    def get_balance(self):
        return self.balance

    def get_trade_history(self):
        return self.trade_history