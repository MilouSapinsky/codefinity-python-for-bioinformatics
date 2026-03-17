def find_motif_positions(sequence, motif):
    if motif == "":
        return []
    position = []
    for i in range (len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            position.append(i + 1)
    return position

sequence = "ATGCGATATCGATCGATCG"
motif = "ATCG"

positions = find_motif_positions(sequence, motif)
print(positions)
