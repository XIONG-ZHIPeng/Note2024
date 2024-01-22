seq1 = "GACTACGATCCGTATACGCACA---GGTTCAGAC"
seq2 = "GACTACAGCTCGTATACGCACACATGGTTCAGAC"
# Define the scoring matrix
scoring_matrix = {
    'A': {'A': 1, 'C': -1, 'G': -1, 'T': -1},
    'C': {'A': -1, 'C': 1, 'G': -1, 'T': -1},
    'G': {'A': -1, 'C': -1, 'G': 1, 'T': -1},
    'T': {'A': -1, 'C': -1, 'G': -1, 'T': 1}
}

# Define the gap penalty values
gap_open_penalty = -6
gap_extension_penalty = -6

# Initialize the score
score = 0

# Iterate through the aligned sequences
for base1, base2 in zip(seq1, seq2):
    if base1 == '-' or base2 == '-':
        # Gap penalty
        score += gap_extension_penalty
    elif base1 == base2:
        # Match
        score += scoring_matrix[base1][base2]
    else:
        # Mismatch
        score += scoring_matrix[base1][base2]

# Print the final score
print("Score:", score)

# The score is 5
