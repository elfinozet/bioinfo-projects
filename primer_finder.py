
#In this project, I tried to find the spesific primer in given sequence input.
#pseudocode:
#define dna string as input
#detection of 'ATGTCGCTGATCAGTCTACTAGA' pattern in dna input
#if pattern exist within the dna input then print 'primer is found'
#if pattern does not exist within the dna input then print 'primer is not found'


#define dna string as input
dna=input('Please enter the sequence:' )
#checks if primer sequence find in dna input with lowercase sensitivty
y=dna.find('ATGTCGCTGATCAGTCTACTAGA') or dna.find('atgtcgctgatcagtctactaga')
if 'ATGTCGCTGATCAGTCTACTAGA' in dna or 'atgtcgctgatcagtctactaga' in dna:
 print('Primer is found.')
else:
 print('Primer is not found.')


#Reporting
#DNA sequence taken as input. The spesific pattern, the primer defined and checked within the DNA input string. 
#The results of checking expressed throguh 'primer is found.' or 'primer is not found.'
#This algorithm can be applied to primer, spesific gene parts like TATAbox, promoters and etc. 
# The potential challenge is  the correct way to annotate. The starting #point of reading the sequence may cause problem. It is not just
# the detection of pattern at given string but find it through the right CONTEXT!
# If we are looking for spesific places like TATABOX, we have to keep in mind that the reading may
#shift in regards: NNNNTATATTATATATATAATNNNN Therefore the index location and the context information is needed to the algorithm to add spesific parameters for detection.
