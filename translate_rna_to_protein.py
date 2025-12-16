#Purpose: Translates an RNA sequence into a protein (amino acid sequence).

#amino acid dictionary
amino_acid_dictionary ={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

#detects the triplet nucleotides codon in the sequence 
def rna_to_amino_acid(rna_sequence):
    amino_acid_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = amino_acid_dictionary[codon]
        if amino_acid == 'STOP':
            break
        amino_acid_sequence += amino_acid
    return amino_acid_sequence

#rna_sequence: The RNA sequence to be translated.
rna_sequence = 'AUGUUCCUUAAGAAGGGAAUUCGCUUUAAAGGAGCA'
amino_acid_sequence = rna_to_amino_acid(rna_sequence)
print('RNA sequence:', rna_sequence)
print('Amino acid sequence:', amino_acid_sequence)


