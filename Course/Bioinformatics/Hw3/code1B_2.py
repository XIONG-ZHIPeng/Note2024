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
gap_open_penalty = -6
gap_extension_penalty = -6

# Initialize the score and gap count
score = 0
gap_count = 0

# Iterate through the aligned sequences
for base1, base2 in zip(seq1, seq2):
    if base1 == '-' or base2 == '-':
        # Gap penalty
        if gap_count == 0:
            score += gap_open_penalty
        else:
            score += gap_extension_penalty
        gap_count += 1
    elif base1 == base2:
        # Match
        score += scoring_matrix[base1][base2]
        gap_count = 0
    else:
        # Mismatch
        score += scoring_matrix[base1][base2]
        gap_count = 0

# Print the final score
print("Score:", score)

# the score is 17
