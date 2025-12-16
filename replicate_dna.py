#Purpose: Simulates the DNA replication process, returning the complementary DNA strand.

#dna_sequence: The original DNA sequence.
dna_seq="GGGGGGGGGGGTTTTTTTTAAAAAAAAAAAAACCCCCCCCATAGATAGATAGATAGGGGGGAGACCT"
#replicates dna into its complementary strand
complementary_dna=(dna_seq.translate(str.maketrans("ATCG", "TAGC")))
print(complementary_dna)


