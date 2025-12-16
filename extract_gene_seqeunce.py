
#dictionary for gene_id and sequences thorugh direct copying and pasting
genome_data={"AX_1000" : "ATGCTACTATCATCATACTGCGGCGGCGCGCGCGCGCGCGGCGCGCGCGATGCATCGATCGATCAGCTAGCATAGACTGA", 
	"AX_1001" : "ATGTATATTTAGACTGCTAGCATAGTACGATCGATACGATCGATGTACGTGTCAGCTCGATCGATACGTCGTAGCTAGTCGACT" , 
	"AX_1002" : "ATGCTCTCATCTAATCGATAGCTAGACGCGCGCTAGCATCGTCGATCGATCGATCACGATCGATCAG", 
	"AX_1003" : "ATGCCGCGCCGCTACGTGCTAGCTAGCATGATTTTTTATATATATGCCGCCGCACACAGTCAGATGCAGTCA", 
	"AX_1004" : "ATGGGGGGGGGCCCCCCCCTATATACGACATGATCGATAGTCAAAAAAA" } 

print("AX_1000:", genome_data["AX_1000"])
print("AX_1001:",genome_data["AX_1001"])

print("AX_1003:",genome_data["AX_1003"])
print("AX_1004:", genome_data["AX_1004"])

print("AX_1002:", genome_data["AX_1002"])


#biopython importation





#sequences=SeqIO.parse(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence1.fasta''' , '''fasta''')


from Bio import SeqIO
with open(r'''C:\Users\elfin\OneDrive\Masaüstü\fastax\sequence1.fasta''' ) as fasta_file:  # Will close handle cleanly
    identifiers = []
    lengths = []
#read Sequence from FASTA file
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):  # (generator)
        identifiers.append(str(seq_record.seq))
        lengths.append(len(seq_record.seq))
#store sequence in DataFrame
d = {'Sequence':identifiers,'Len':lengths}
data= pd.DataFrame(d)
data['label']="MERS"
data

