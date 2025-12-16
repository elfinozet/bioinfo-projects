#importation of biophyon
import Bio as Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo


#fasta files downloaded from ncbi 
a1=SeqIO.read(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence1.fasta''' , '''fasta''')
a2=SeqIO.read(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence2.fasta''' , '''fasta''')
a3=SeqIO.read(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence3.fasta''' , '''fasta''')
a4=SeqIO.read(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence4.fasta''' , '''fasta''')
a5=SeqIO.read(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence5.fasta''' , '''fasta''')

#checking files if it is right
print(a1.description)
print(a2.description)
print(a3.description)
print(a4.description)
print(a5.description)

species=SeqIO.write([a1, a2, a3, a4, a5], 'species.fasta' , 'fasta')


#https://www.ebi.ac.uk/Tools/services/web_muscle/toolresult.ebi?jobId=muscle-E20240119-103456-0179-66114660-p1m&analysis=alignments alignment analysis downloaded
with open (r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\results.aln''' , "r" ) as aln:
  alignment=AlignIO.read(aln,'clustal')
  print(type(alignment))

from Bio.Phylo.TreeConstruction import DistanceCalculator
Calculator= DistanceCalculator('identity')

distance_matrix=Calculator.get_distance(alignment)
print(distance_matrix)


from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor=DistanceTreeConstructor(Calculator)

#build the tree
species_tree=constructor.build_tree(alignment)
species_tree.rooted= True
print(species_tree)

#save the tree into a new file
Phylo.write(species_tree, 'species_tree.xml', 'phyloxml')

#import matplotlib and create basic tree
import matplotlib
import matplotlib.pyplot as plt
fig=Phylo.draw(species_tree)


