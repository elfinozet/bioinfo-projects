#Purpose: Transcribes a DNA sequence into its corresponding RNA sequence.

#dna_sequence (str): The DNA sequence to be transcribed.
dna_seq="TTTTTTTTTTTTTTTTTTTGATCGATCGACTGCTAGCTACGATCGTGACGCAGCTACGTACGATCGACTAGTAG"
#trancribes DNA to RNA by changing T into U
rna_seq=dna_seq.translate(str.maketrans("TACG","UACG"))
print(rna_seq)					  