# main.py
import itertools
import pylab
import os
from matplotlib import pyplot as plt

def readFasta(filename):
  """Takes a location/filename as a string input. Opens the file and converts
  the alignment file to either a matrix of the characters, or a list of lists.
  returns the fasta in python architecture. Implemented by Neville.
  """
  line_int=0
  char_mat = []
  file=open(filename,"r")
  for i in file:
    listy=list(i)
    if listy[0]!=">":
      for jj in range(len(listy)-1):
        char_mat[line_int].append(listy[jj])
    elif listy[0]==">":
      char_mat.append([])
      line_int=line_int+1
  char_mat2=[]
  for k in range(len(char_mat[1])):
    char_mat2.append([])
    for l in range(len(char_mat)):
      char_mat2[k].append(char_mat[l][k])
  return char_mat2

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
# score = score_column_pairwise(column, score_dict)

def score_all_columns_pairwise(all_columns_list, score_dict):
	return map(lambda col_list: score_column_pairwise(col_list, score_dict),
		all_columns_list)
# score_dict = make_score_dict('blosum62.dat')
# all_columns = [['A', 'A', 'A', 'C'], ['C', 'C', 'C', 'A']]
# score_list = score_all_columns_pairwise(all_columns, score_dict)
# print score_list


def find_column_consensus(column_list):
	return max(set(column_list), key=column_list.count)
# column = ['A', 'A', 'A', 'C']
# print(find_column_consensus(residues))

def find_all_consensus(all_columns_lists):
	return map(lambda col_list: find_column_consensus(col_list),
		all_columns_lists)
# all_columns = [['A', 'A', 'A', 'C'], ['C', 'C', 'C', 'A']]
# consensus = find_all_consensus(all_columns)
# print consensus

def score_column_fraction_consensus(column_list):
	consensus = find_column_consensus(column_list)
	count = column_list.count(consensus)
	fraction = float(count) / float(len(column_list))
	return fraction
# column = ['A', 'A', 'A', 'C']
# score = score_column_fraction_consensus(column)

def score_all_columns_fraction_consensus(all_columns_list, score_dict):
	return map(lambda col_list: score_column_pairwise(col_list, score_dict),
		all_columns_list)
# score_dict = make_score_dict('blosum62.dat')
# all_columns = [['A', 'A', 'A', 'C'], ['C', 'C', 'C', 'A']]
# score_list = score_all_columns_pairwise(all_columns, score_dict)
# print score_list


def visualization(consensus_residues, conservation_scores):
	with open('data.dat', 'w') as f:
		lis=[consensus_residues, conservation_scores]
		n=1
		for x in zip(*lis):
        		f.write("%i {0} {1}\n" .format(*x) % n)
			n+=1
	os.system("gnuplot plotting.plt")
# visualization(consensus, score_list)


def visualization_k(consensus_residues, conservation_scores, output_file):
	fig, ax = plt.subplots()
	
	
	
	test = ax.bar(range(len(conservation_scores)), conservation_scores, 1)
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
    
    # 	plt.show()
	plt.savefig(output_file)	
# visualization_k(consensus, score_list, 'test.png')
