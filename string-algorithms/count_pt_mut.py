#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

#Return: The Hamming distance dH(s,t).

def hamming_distance(s, t):
    return sum([1 for i in zip(s, t) if i[0] != i[1]])
