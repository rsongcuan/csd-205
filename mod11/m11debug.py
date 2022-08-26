def investment_function():
    investment_amount = float(input("Enter the initial investment: "))
    interest_rate = float(input("Enter the annualized interest rate : "))
    balance_amount = investment_amount
    year = 0
    while balance_amount < 2 * investment_amount:
        balance_amount = balance_amount + (balance_amount *(interest_rate/100))
        year+=1
    print('The number of years it takes an investment to double is:',year)
investment_function()

ryansongcuan@Ryans-MacBook-Air M11 % python3 test_m11debug.py
Enter the initial investment: 100
Enter the annualized interest rate : 10
The number of years it takes an investment to double is 0
E
======================================================================
ERROR: test_investment (__main__.InvestmentTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/ryansongcuan/Desktop/I Love College/CSD 205 Intro to Programming with Python/M11/test_m11debug.py", line 6, in test_investment
    years_to_double = function()
  File "/Users/ryansongcuan/Desktop/I Love College/CSD 205 Intro to Programming with Python/M11/m11debug.py", line 13, in function
    while balance_amount < 2 * investment_amount:
TypeError: '<' not supported between instances of 'int' and 'str'

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (errors=1)