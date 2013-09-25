# main.py

def readFasta():
"""Takes a location/filename as a string input. Opens the file and converts
the alignment file to either a matrix of the characters, or a list of lists.
Returns the fasta in python architecture."""


def processFasta():
"""Takes the read Fasta from readFast. Calls a scoring function for each line
of the alignment. Returns the consensus sequence as a list and a corresponding
list of the conservation values."""


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


