import csv
import math

motif_length = 10
sequences_coloumn_length = 200
sequences_row_length = 100
filepath = "E:/Personal/2023/Waseda/curriculum/Bioinformatics/Hw4/proteins.csv"
amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
amino_acids_length = 20

sequences = []

with open(filepath, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "-1":
            continue
        protein_sequence = row[1:101]
        sequences.append(protein_sequence)

#a)	Randomly initialize the starting positions for all the sequences.
def index_init():
    import random
    index = []
    for i in range(0, sequences_coloumn_length):
        index.append(random.randint(0, 90))
    return index

#b)	Given the positions, you can extract the motif from each protein.
def motif_extract(index):
    motifs = []
    for i in range(0, sequences_coloumn_length):
        motifs.append(sequences[i][index[i]:index[i] + motif_length])
    return motifs


#d)	Implement the PSSM (Position-Specific Scoring Matrix) to describe the statistical model.
def pssm(motifs):
    pssm_matrix = []
    overall_frequency = [0] * amino_acids_length
    for i in range(motif_length):
        column = []
        for j in range(amino_acids_length):
            count = 0
            for k in range(sequences_coloumn_length):
                if amino_acids[j] == motifs[k][i]:
                    count += 1
            overall_frequency[j] += count
            column.append(count)

        column = [x / sequences_coloumn_length for x in column]
        pssm_matrix.append(column)
    
    overall_frequency = [x / (sequences_coloumn_length*motif_length) for x in overall_frequency]
    pssm_matrix = [[math.log(x) if x > 0 else -10 for x in y] for y in pssm_matrix]
    return pssm_matrix

#Expextion step
def expectation(pssm_matrix):
    expectation_matrix = []
    for i in range(sequences_coloumn_length):
        probability = 0
        for j in range(sequences_row_length - motif_length):
            for k in range(motif_length):
                probability += pssm_matrix[k][amino_acids.index(sequences[i][j + k])]
            probability = probability / motif_length
            expectation_matrix.append(probability)
    return expectation_matrix

#c)	Implement the Expectation-Maximization algorithm to update the starting positions.
def maximization(expectation_matrix):
    updated_index = []
    for i in range(sequences_coloumn_length):
        x = expectation_matrix.index(max(expectation_matrix[i*90:(i+1)*90])) % 90
        updated_index.append(x)
    return updated_index

#d)	Choose the positions that has the highest probability as the updated starting position.
index = index_init()
temp = []
while True:
    motifs = motif_extract(index)
    pssm_matrix = pssm(motifs)
    print(pssm_matrix)
    expectation_matrix = expectation(pssm_matrix)
    updated_index = maximization(expectation_matrix)
    print("The updated starting position is: ", updated_index)
    if updated_index == index or temp == updated_index:
        print("The final starting position is: ", updated_index)
        break
    else:
        temp = index
        index = updated_index