__author__ = 'dare7'
import math

class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            self.fees += 5

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    count = 0
    while count <=25:
        sum = lst[-1] + lst[-2] + lst[-3]
        lst.append(sum)
        count += 1

    return lst

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60
    return seconds_in_minute

if __name__ == "__main__":
    #print(clock_helper(90))
    print(math.log(math.sqrt(5**7), 5))
