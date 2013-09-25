# main.py
import itertools
import pylab


def readFasta():
	"""Takes a location/filename as a string input. Opens the file and converts
	the alignment file to either a matrix of the characters, or a list of lists.
	Returns the fasta in python architecture."""


def processFasta():
	"""Takes the read Fasta from readFast. Calls a scoring function for each line
	of the alignment. Returns the consensus sequence as a list and a corresponding
	list of the conservation values."""



def VisualizeData(consensus_residues, conservation_scores):
	# 
	print 'poop'

def make_score_dict(filepath):
	
	file = open(filepath, 'r')
	dict = {}
	
	for i in file:
		line = i.split()
		dict[(line[0], line[1])] = float(line[2])
	
	return dict

def score_column(column_list, score_dict):
	# 
	residue_pairs = itertools.combinations(column_list, 2)
	score = 0.0
	

	for i,j in residue_pairs:
		new_score = score_dict[tuple(sorted([i, j]))]
		score = score + new_score
		
	n_terms = len(column_list) * (len(column_list) - 1)
	normalized_score = score / n_terms
	return normalized_score



# 
# score_dict = make_score_dict('blosum62.dat')
# 
# residues = ['A', 'A', 'A', 'C']
# print residues * 4
# my_list = []
# 
# for i in range(20):
# 	my_list.append(score_column(residues * (i+1), score_dict))
# 
# pylab.plot(my_list)
# pylab.show()