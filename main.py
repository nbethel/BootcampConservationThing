# main.py
import numpy


def readFasta(filename):
#Takes a location/filename as a string input. Opens the file and converts
#the alignment file to either a matrix of the characters, or a list of lists.
#Returns the fasta in python architecture. Implemeneted by Neville
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
#"""Takes the read Fasta from readFast. Calls a scoring function for each line
#of the alignment. Returns the consensus sequence as a list and a corresponding
#list of the conservation values."""
  
  return 1
