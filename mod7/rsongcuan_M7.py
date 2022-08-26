# Ryan Songcuan, 9/19/21, Module 7 Assignment
# The purpose is to determine how long it takes for an investment to double at the given interest rate

interest = input("\nWhat is the annual interest rate, in percentage? ")
interest = float(interest)

initial_inv = input("\nWhat is the initial investment amount? $")
initial_inv = float(initial_inv)

newValue = initial_inv + (initial_inv * float(interest/100))
years = 1

while newValue < (initial_inv*2):
	newValue = newValue + (newValue * float(interest/100))
	years = years + 1

print(f"\nYour initial investment of ${initial_inv:.2f} will double in {years} years.")