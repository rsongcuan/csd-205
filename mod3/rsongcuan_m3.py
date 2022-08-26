# Ryan Songcuan, 8/29/21, Module 3 Assignment
# Calculate cost of installing fiber optic cable at a cost of $0.87 for a company
#Start
welcome = "Welcome to the Fiber Optic Cable Cost Calculator!"
print(welcome)
_name = input("What is your company's name?\n")
_feet = input("What is the total length, in feet, of fiber optic cable you wish to install?\n")
_feet = float(_feet)
_cost = _feet*0.87
print(f"The cost for {_name} will be ${_cost:.2f}.")
#End

# References
# Matthes, E. (2019). User input and while loops. In Python crash course: A hands-on, project-based 
#	introduction to programming (2nd ed., pp. 114–116). No Starch Press. 
# Sayon, S. (n.d.). How to Limit Floats to Two Decimal Points in Python? Finxter. 
#	https://blog.finxter.com/limit-floats-to-two-decimal-points-python/. 