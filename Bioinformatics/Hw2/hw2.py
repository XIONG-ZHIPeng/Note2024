import numpy as np
import matplotlib.pyplot as plt

# Define sequences
seq1 = "COELACANTH"
seq2 = "PELICAN"

# Define scoring scheme
scoring_scheme = {('A', 'A'): 1, ('C', 'C'): 1, ('E', 'E'): 1, ('H', 'H'): 1, ('L', 'L'): 1, ('N', 'N'): 1, ('O', 'O'): 1, ('P', 'P'): 1, ('T', 'T'): 1, ('I', 'I'): 1, ('S', 'S'): 1, ('D', 'D'): -1, ('F', 'F'): -1, ('G', 'G'): -1, ('K', 'K'): -1, ('M', 'M'): -1, ('Q', 'Q'): -1, ('R', 'R'): -1, ('V', 'V'): -1, ('W', 'W'): -1, ('Y', 'Y'): -1, ('-', '-'): -1}

# Define function to calculate score of two amino acids
def get_score(aa1, aa2):
    return scoring_scheme.get((aa1, aa2), -1)

# Implement Needleman-Wunsch algorithm
n = len(seq1)
m = len(seq2)
score_matrix = np.zeros((n+1, m+1))
for i in range(1, n+1):
    score_matrix[i][0] = score_matrix[i-1][0] - 1
for j in range(1, m+1):
    score_matrix[0][j] = score_matrix[0][j-1] - 1
for i in range(1, n+1):
    for j in range(1, m+1):
        match_score = score_matrix[i-1][j-1] + get_score(seq1[i-1], seq2[j-1])
        delete_score = score_matrix[i-1][j] - 1
        insert_score = score_matrix[i][j-1] - 1
        score_matrix[i][j] = max(match_score, delete_score, insert_score)

# Print global alignment
alignment1 = ""
alignment2 = ""
i = n
j = m
while i > 0 or j > 0:
    if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i-1][j-1] + get_score(seq1[i-1], seq2[j-1]):
        alignment1 = seq1[i-1] + alignment1
        alignment2 = seq2[j-1] + alignment2
        i -= 1
        j -= 1
    elif i > 0 and score_matrix[i][j] == score_matrix[i-1][j] - 1:
        alignment1 = seq1[i-1] + alignment1
        alignment2 = "-" + alignment2
        i -= 1
    else:
        alignment1 = "-" + alignment1
        alignment2 = seq2[j-1] + alignment2
        j -= 1

# Print global alignment
print(alignment1)
print(alignment2)

# Plot scoring matrix
fig, ax = plt.subplots()
ax.set_xticks(np.arange(len(seq1)+1))
ax.set_yticks(np.arange(len(seq2)+1))
ax.set_xticklabels(['-'] + list(seq1))
ax.set_yticklabels(['-'] + list(seq2))
for i in range(len(seq2)+1):
    for j in range(len(seq1)+1):
        ax.text(j, i, int(score_matrix[j][i]), ha="center", va="center", color="w")
plt.imshow(score_matrix, cmap='cool', interpolation='nearest')
plt.show()

