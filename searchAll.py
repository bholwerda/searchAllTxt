
# Program to accept user input and search all .txt files for said input

import re, sys, pprint, os
	
def searchFiles():
	''' Asks the user for input, searchs the txt files passed,
	 stores the results into a list'''
	location = []
	results = []
	userAskFor = input('What would you like to search all the text files for? ')
	searchForRegex = re.compile(userAskFor)
	allFiles = os.listdir(os.path.expanduser('~/Documents'))
	for i in allFiles:
		if i.endswith('.txt'):
			path = os.path.join(os.path.expanduser('~/Documents'), i)
			location.append(path)
			with open(path) as file:
				content = file.read()
				found = searchForRegex.findall(content)
				results.append(found)
	return (results, userAskFor, location)

results, userAskFor, location = searchFiles()
for x in range(len(results)):
	print('\nThere were %s Occurances of %s in %s.' % (len(results[x]), userAskFor, location[x]))
input('Press Enter to Exit')
