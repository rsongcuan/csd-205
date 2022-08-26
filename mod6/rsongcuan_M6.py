# Ryan Songcuan, 9/7/21, Module 6 Assignment
# This program allows users to select a key from the dictionary to display that key's value
nfl_states = {
	'arizona': 'Arizona Cardinals',
	'california': 'Los Angeles Rams, Los Angeles Chargers, and San Francisco 49ers',
	'colorado': 'Denver Broncos',
	'florida': 'Jacksonville Jaguars, Miami Dolphins, and Tampa Bay Buccaneers',
	'georgia': 'Atlanta Falcons',
	'illinois': 'Chicago Bears',
	'indiana': 'Indianapolis Colts',
	'louisiana': 'New Orleans Saints',
	'maryland': 'Baltimore Ravens and Washington Football Team',
	'massachusetts': 'New England Patriots',
	'michigan': 'Detroit Lions',
	'minnesota': 'Minnesota Vikings',
	'missouri': 'Kansas City Chiefs',
	'nevada': 'Las Vegas Raiders',
	'new jersey': 'New York Giants and New York Jets',
	'new york': 'Buffalo Bills',
	'north carolina': 'Carolina Panthers',
	'ohio': 'Cincinnati Bengals and Cleveland Browns',
	'pennsylvania': 'Philadelphia Eagles and Pittburgh Steelers',
	'tennessee': 'Tennessee Titans',
	'texas': 'Dallas Cowboys and Houston Texans',
	'washington': 'Seattle Seahawks',
	'wisconsin': 'Green Bay Packers',
	}

print("\nWelcome! The states below are home to one or more teams in the National Football League.\n")
for state in nfl_states:
	print(state.title())
state = input("\nEnter one of the options above to see what NFL team (or teams) play their home games in that state:\n   ")
print("\n")
print(nfl_states[state.lower()])
print("\n")
