print("Invalid withdrawal amount. Please withdraw a positive amount.")



    def display_balance(self):

        print(f"Account {self.__account_number} balance: ${self.__account_balance:.2f}")





# Testing the BankAccount class

if _name_ == "__main__":

    # Create a BankAccount instance

    account1 = BankAccount("123456", "John Doe", 1000.0)



    # Deposit money

    account1.deposit(500.0)



    # Withdraw money

    account1.withdraw(200.0)



    # Display balance

    account1.display_balance()