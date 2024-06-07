seq1 = "GACTACGATCCGTATACGCACA---GGTTCAGAC"
seq2 = "GACTACAGCTCGTATACGCACACATGGTTCAGAC"
# Define the scoring matrix
scoring_matrix = {
    'A': {'A': 2, 'C': -7, 'G': -5, 'T': -7},
    'C': {'A': -7, 'C': 2, 'G': -7, 'T': -5},
    'G': {'A': -5, 'C': -7, 'G': 2, 'T': -7},
    'T': {'A': -7, 'C': -5, 'G': -7, 'T': 2}
}

# Define the gap penalty values
gap_open_penalty = -11
gap_extension_penalty = -1

# Initialize the score and gap flag
score = 0
gap_flag = False

# Iterate through the aligned sequences
for base1, base2 in zip(seq1, seq2):
    if base1 == '-' or base2 == '-':
        if not gap_flag:
            # Gap open penalty
            score += gap_open_penalty
            gap_flag = True
        else:
            # Gap extension penalty
            score += gap_extension_penalty
    elif base1 == base2:
        # Match
        score += scoring_matrix[base1][base2]
        gap_flag = False
    else:
        # Mismatch
        score += scoring_matrix[base1][base2]
        gap_flag = False

# Print the final score
print("Score:", score)

# the score is 20
