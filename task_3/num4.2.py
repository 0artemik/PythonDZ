class Wallet:

    paymentSystem = "Visa"

    def __init__(self, name: str, currency: str, balance: float = 0):
        self.name = name
        self._balance = balance
        self.currency = currency

    def deposit(self, amount: float):
        self._balance += amount

    def pay(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return f"{self._balance} {self.currency}"

    def delete(self):
        del self._balance
        del self.name
        del self.currency

class CryptoWallet(Wallet):
    def __init__(self, name, currency, coin, balance=0):
        super().__init__(name, currency, balance)
        self.coin = coin

    def get_balance(self):
        return f"{self._balance} {self.coin}"

    def get_balance_in_usd(self):
        if self.coin == "BTC":
            return self._balance * 72000
        elif self.coin == "ETH":
            return self._balance * 3500
        else:
            return "Неизвестная монета"

a = CryptoWallet("Vic", "$", "ETH", 5000)

print(a.get_balance())
print(a.get_balance_in_usd())