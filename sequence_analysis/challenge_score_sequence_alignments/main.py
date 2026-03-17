def score_alignment(seq1, seq2):
    matches = 0
    mismatches = 0
    gaps = 0
    for a, b in zip(seq1, seq2):
        if a == '-' or b == '-':      # 1) check for actual gap character
            gaps += 1
        elif a == b:
            matches += 1
        else:
            mismatches += 1
    return matches, mismatches, gaps

result1 = score_alignment("ATG-C", "AT-AC")  # (3, 0, 2)
print(result1)

result2 = score_alignment("A--GC", "ATAGC")  # (3, 0, 2)
print(result2)

result3 = score_alignment("ACGT", "TGCA")    # (0, 4, 0)
print(result3)