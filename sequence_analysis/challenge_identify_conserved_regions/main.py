def find_conserved_positions(alignment):
    conserved_positions = []
    if not alignment:
        return conserved_positions
    seq_length = len(alignment[0])
    for i in range(seq_length):
        column = [seq[i] for seq in alignment]
        if all(base == column[0] for base in column):
            conserved_positions.append(i)
    return conserved_positions

# Sample calls
alignment1 = [
    "ATGCT",
    "ATGCT",
    "ATGCT"
]
result1 = find_conserved_positions(alignment1)
print(result1)

alignment2 = [
    "ATGCT",
    "ATGCA",
    "ATGCC"
]
result2 = find_conserved_positions(alignment2)
print(result2)

alignment3 = [
    "AACGTA",
    "AACGTA",
    "AACGTA"
]
result3 = find_conserved_positions(alignment3)
print(result3)

alignment4 = [
    "AACGTA",
    "AGCGTA",
    "AACGTA"
]
result4 = find_conserved_positions(alignment4)
print(result4)
