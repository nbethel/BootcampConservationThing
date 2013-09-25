# main.py
import itertools


def readFasta():
	"""Takes a location/filename as a string input. Opens the file and converts
	the alignment file to either a matrix of the characters, or a list of lists.
	Returns the fasta in python architecture."""


def processFasta():
	"""Takes the read Fasta from readFast. Calls a scoring function for each line
	of the alignment. Returns the consensus sequence as a list and a corresponding
	list of the conservation values."""



def VisualizeData(consensus_residues, conservation_scores):

def makeScoreDict(filepath):
	file = open(filepath, 'r')
	
	dict = {}

	for i in file:
		line = i.split()
		dict[(line[0], line[1])] = float(line[2])
	
	return dict

def scoreColumn(column_list, scoreDict):
	# 
	residue_pairs = itertools.combinations(column_list, 2)
	score = 0
	
	for i in residue_pairs:
		new_score = scoreDict[i]
		score = score + new_score
		
	return score

# 
# scoreDict = makeScoreDict('blosum62.dat')
# 
# 
# my_column = ['A', 'A', 'A', ]
# print scoreColumn (my_column, scoreDict)

