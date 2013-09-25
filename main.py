# main.py
import itertools

def readFasta(filename):
#Takes a location/filename as a string input. Opens the file and converts
#the alignment file to either a matrix of the characters, or a list of lists.
#Returns the fasta in python architecture. Implemeneted by Neville
  line_int=-1
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
  print char_mat2[4]
  return char_mat

readFasta("alignments/ha/alignment.fasta")
def processFasta(char_mat):
    """Takes the read Fasta from readFast. Calls a scoring function for each line  
    of the alignment. Returns the consensus sequence as a list and a corresponding
    list of the conservation values.
    """
    return None

def visualizeData(consensus_residues, conservation_scores):
        return None

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

scoreDict = makeScoreDict('blosum62.dat')
print scoreDict[('A','A')]

#test_readFasta()

# 
# scoreDict = makeScoreDict('blosum62.dat')
# 
# 
# my_column = ['A', 'A', 'A', ]
# print scoreColumn (my_column, scoreDict)
