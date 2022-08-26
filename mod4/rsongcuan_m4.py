# Ryan Songcuan, 8/29/21, Module 4 Assignment
# Tuples

#big10schools is a tuple including universities in the big ten conference

#1: Initialize with values
big10schools = ('illinois', 'indiana', 'iowa', 'maryland', 'minnesota', 'michigan', 'michigan state', 'minnesota', 'nebraska', 'northwestern', 'ohio state', 'penn state', 'purdue', 'rutgers', 'wisconsin')

#2: Display the contents in a single statement
print(big10schools)

#3: Iterate through the collection displaying the output as a complete sentence using each value
for university in big10schools:
	print(f"\n{university.title()} is a member of the Big Ten Conference.")

#4: Repeat the output in reverse order using a different context string
backwords = reversed(big10schools)
b10reversed = tuple(backwords)
for university in b10reversed:
	print(f"\n{university.title()}'s football team competes in the NCAA Division I Football Bowl Subdivision (FBS).")

# References
# Matthes, E. (2019). Working with lists. In Python crash course: A hands-on, project-based
#	introduction to programming (2nd ed., pp. 65–67). essay, No Starch Press. 
# Python - Update Tuples. W3 Schools. (n.d.). https://www.w3schools.com/python/python_tuples_update.asp. 