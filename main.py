# main.py
import itertools
import pylab

def readFasta(filename):
    """Takes a location/filename as a string input. Opens the file and converts
    the alignment file to either a matrix of the characters, or a list of lists.
    returns the fasta in python architecture. Implemented by Neville.
    """
  line_int=0
  char_mat = []
  file=open(filename,"r")
  next(file)
  for i in file:
    char_mat.append([])
    char_mat[line_int].append(list(i))
    del char_mat[line_int][0][-1]
    line_int=line_int+1
  print char_mat[0]
  return char_mat

def processFasta(char_mat):
    """Takes the read Fasta from readFast. Calls a scoring function for each line  
    of the alignment. Returns the consensus sequence as a list and a corresponding
    list of the conservation values.
    """
    return None


def visualizeData(consensus_residues, conservation_scores):
        return None


def make_score_dict(filepath):
	
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

	

	for i,j in residue_pairs:
		new_score = score_dict[tuple(sorted([i, j]))]
		score = score + new_score
		
	n_terms = len(column_list) * (len(column_list) - 1)
	normalized_score = score / n_terms
	return normalized_score



scoreDict = makeScoreDict('blosum62.dat')
print scoreDict[('A','A')]

#test_readFasta()

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
