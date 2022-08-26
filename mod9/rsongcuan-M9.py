# Ryan Songcuan, 9/26/21, Module 9 Assignment
# The purpose is to use parent and child classes to create a banking program
class BankAccount:
	def __init__(self, accountNumber, balance):
		self.accountNumber = accountNumber
		self.balance = balance

	def withdrawal(self):
		print(f"\nThis service has a $5.00 transaction fee.")
		amount = float(input("\nPlease enter the amount you wish to withdraw: "))
		self.balance -= amount
		if self.balance < 0:
			print("Insufficient funds.")

	def deposit(self):
		try:
			amount = float(input("Please enter the amount you with to deposit: "))
			self.balance += amount
			print(f"\nAmount Deposited: ${amount:.2f}")
		except ValueError:
			print("Invalid entry. Please try again.")

	def getBalance(self):
		print(f"\nThe balance available for account # {self.accountNumber} is ${self.balance:.2f}\n")

class CheckingAccount(BankAccount):
	def __init__(self, accountNumber, balance):
		super().__init__(accountNumber, balance)
		self.fees = 5
		self.minimum_balance = 50

	def deductFees(self):
		self.balance -= self.fees

	def checkMinimumBalance(self):
		if self.balance < 50:
			print(f"Your account is lower than the required minimum balance of ${self.minimum_balance:.2f}. Please deposit funds immediately.")

class SavingsAccount(BankAccount):
	def __init__(self, accountNumber, balance):
		super().__init__(accountNumber, balance)
		self.interestRate = 0.02

	def addInterest(self):
		accrued_interest = self.balance * self.interestRate
		self.balance += accrued_interest
		print(f"At an interestRate of 2%, your savings account {self.accountNumber} has accrued ${accrued_interest:.2f}.")

checking1 = CheckingAccount(10001, 200)
checking1.getBalance()
checking1.withdrawal()
checking1.deductFees()
checking1.checkMinimumBalance()
checking1.getBalance()

checking2 = CheckingAccount(10002, 25)
checking2.getBalance()
checking2.checkMinimumBalance()
checking2.deposit()
checking2.getBalance()

savings1 = SavingsAccount(10003, 200)
savings1.getBalance()
savings1.addInterest()
savings1.getBalance()

savings2 = SavingsAccount(10004, 25)
savings2.getBalance()
savings2.addInterest()
savings2.getBalance()