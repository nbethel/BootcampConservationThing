# main.py


def makeScoreDict(filepath):
	file = open(filepath, 'r')
	
	dict = {}

	for i in file:
		line = i.split()
		dict[(line[0], line[1])] = line[2]
	
	return dict
	
def scoreColumn(column_list):
	# 
	
	
	
	
	score = 0
	return score

scoreDict = makeScoreDict('blosum62.dat')
print scoreDict[('A','A')]