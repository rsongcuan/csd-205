# Ryan Songcuan, 9/19/21, Module 8 Assignment
#The purpose is to convert the user's number of miles driven into kilometers and display both numbers.
def converter(miles):
	"""Convert miles into kilometers."""
	miles = float(miles)
	kilometers = miles*1.609344
	return kilometers

while True:
	print("\nTell me the distance driven in miles: ")
	print("(enter 'q' at any time to quit)")

	distance = input("Miles driven: ")
	if distance == 'q':
		break

	try:
		converted_distance = converter(distance)
		print(f"\nThe distance driven is equal to {converted_distance} kilometers.")
	except ValueError:
		print("\nPlease type in numbers rather than letters.")

# Reference
# Matthes, E. (2019). Files and Exceptions. In Python crash course: A hands-on, project-based introduction to programming (pp. 194–197). essay, No Starch Press. 