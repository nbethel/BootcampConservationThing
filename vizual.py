import os

def Visualization(consensus_residues, conservation_scores):
	with open('data.dat', 'w') as f:
		lis=[consensus_residues, conservation_scores]
		n=1
		for x in zip(*lis):
        		f.write("%i {0} {1}\n" .format(*x) % n)
			n+=1
	os.system("gnuplot plotting.plt")

Visualization(AA, score_list)
