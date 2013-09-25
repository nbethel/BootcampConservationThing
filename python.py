def makeCodonLib():

	import math
	import numpy

	dict={}
	file=open("../assignment/dna-codons.dat","r")
	for i in file:
	  line=i.split()
	  dict[line[0]]=line[1]

	return dict
