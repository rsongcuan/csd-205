# Ryan Songcuan, 9/6/21, Module 5 Assignment
# Calculate cost of installing fiber optic cable at a cost of $0.87 for a company with bulk discount
#Start
welcome = "Welcome to the Fiber Optic Cable Cost Calculator!"
print(welcome)
_name = input("What is your company's name?\n")
_feet = input("What is the total length, in feet, of fiber optic cable you wish to install?\n")
_feet = float(_feet)
if _feet > 500:
	_cost = _feet*0.50
elif _feet > 250:
	_cost = _feet*0.70
elif _feet > 100:
	_cost = _feet*0.80
else:
	_cost = _feet*0.87
print(f"The cost for {_name} will be ${_cost:.2f}.")
#End