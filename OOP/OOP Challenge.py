import datetime
import pytz

class Account:
    """Simple account class with balance"""

    #When defining a static method, don't use 'self', instead use the class name, i.e. Account
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.___balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.___balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.___balance:
            self.___balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.___balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.withdraw(100)
    steph.deposit(50)
    steph.show_transactions()
