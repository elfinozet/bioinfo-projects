#find_regulatory_elements(genome_sequence)


#genome_sequence (str): The genome sequence to be analyzed.
dna_sequence='GAAGACATCGATCGATCGACTACTGTATAACCGATGCATCGATGTACGATCGATGCTGCTCGATCAGTCGATCAGCTGATCGATCACGCCCCCGCGCGCCGGCGCTATATATATACGATCATGATCGATCGCTACGACTGCTCGATCGATCGGCATCACGCTAGTACGATCGTCAGCTACGACTG'

#tatabox
tata_box= dna_sequence.find("TATAA")
if tata_box==tata_box:
 print("TATAA box found.")
 print('The position of TATA box:', tata_box)

#primer
primer=dna_sequence.find("GATCGATCACGCCCCCGCGCGCCGGCGCTATATATATACG")
if primer==primer:
 print("Primer found.")
 print('The starting position of primer:', primer)

#enhancer
enhancer=dna_sequence.find('ACGATCGATGCTG')
if enhancer==enhancer:
 print("Enhancer is found.")
 print("The starting position of enhancer:", enhancer)


   

   


