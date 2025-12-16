
#original_sequence (str): The original DNA or RNA sequence
original_sequence="ATGAGAGAGATTTTAGAGAGACACACATACACACA"
A=len(original_sequence)
print("Length of Original Sequnce:", A)
#mutated_sequence (str): The mutated DNA or RNA sequence.
mutated_sequence="ATGAGACAGATTATAGAGAGACACACATACACACA"
B=len(mutated_sequence)
print("Length of mutated sequence:", B)
difference=2

#Returns: A float representing the mutation rate (percentage of changes).
print("Difference:", difference)
if A ==B:
 mutation_rate=float(difference/A)*100

 print("Mutation rate:" , mutation_rate)





