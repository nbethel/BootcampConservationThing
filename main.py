# main.py
import itertools
import pylab
import python

def readFasta(filename):
  """Takes a location/filename as a string input. Opens the file and converts
  the alignment file to either a matrix of the characters, or a list of lists.
  returns the fasta in python architecture. Implemented by Neville.
  """
  line_int=0
  char_mat = []
  file=open(filename,"r")
  dict=python.makeCodonLib()
  for i in file:
    listy=list(i)
    if listy[0]!=">":
      jj=0
      while jj <= len(listy)-4:
        codon=listy[jj]+listy[jj+1]+listy[jj+2]
        amino=dict[codon]
        char_mat[line_int].append(amino)
        jj=jj+3
    elif listy[0]==">":
      char_mat.append([])
      line_int=line_int+1
  char_mat2=[]
  for k in range(len(char_mat[1])):
    char_mat2.append([])
    for l in range(len(char_mat)):
      char_mat2[k].append(char_mat[l][k])
  return char_mat2

def processFasta(Fastafile):
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
# score_dict = make_score_dict('blosum62.dat')


def score_column_pairwise(column_list, score_dict):
	# a column scoring function based on all pairwise conservation scores
	score = 0
	residue_pairs = itertools.combinations(column_list, 2)
	for i,j in residue_pairs:
		new_score = score_dict[tuple(sorted([i, j]))]
		score = score + new_score
		
	n_terms = len(column_list) * (len(column_list) - 1)
	normalized_score = score / n_terms
	return normalized_score
# score_dict = make_score_dict('blosum62.dat')
# column = ['A', 'A', 'A', 'C']
# score = score_column(residues, column)


def find_column_consensus(column_list):
	return max(set(column_list), key=column_list.count)
# residues = ['A', 'A', 'A', 'C']
# print(find_column_consensus(residues))

def find_all_consensus(all_column_lists):
	return map(lambda col_list: find_column_consensus(col_list), all_column_lists)
# all_columns = [['A', 'A', 'A', 'C'], ['C', 'C', 'C', 'A']]
# print find_all_consensus(all_columns)

