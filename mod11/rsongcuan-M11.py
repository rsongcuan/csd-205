# Ryan Songcuan, 10/8/21, Module 11 Assignment
# Debug
# Purpose of this program is to stop any cats from making it inside!

#For my birthday this year, my son wanted all the kids in the neighborhood to bring their pets over for a party.
#Everyone started showing up, so we looked outside to see what kind of animals would be coming in.
pets_outside = ['Dog', 'Cat', 'Snake', 'Golfish', 'Dog', 'Ferret', 'Cat', 'Iguana', 'Rabbit', 'Dog']
pets_inside = []

#We just realized that the invitations forgot to mention that my son is extremely allergic to cats!
#We want to make sure that the pets outside make it inside for the party, but we need to stop any cats from coming in.
while pets_outside:
	pets_outside.remove('cat')
	pet_at_door = pets_outside.pop()
	pets_inside.append(pet_at_door)

#Let's take a look around and make sure no cats got in!
print(pets_inside)