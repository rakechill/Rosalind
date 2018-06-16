# given: a DNA string s of length at most 1000 bp (combo of 2
# bonded complementary bases)
# return: the reverse complement s^c of s

def reverse_complement(dna):
    reverse, comp = dna[::-1], ''
    for nt in reverse:
        if nt == 'A':
            comp = comp + 'T'
        elif nt == 'T':
            comp = comp + 'A'
        elif nt == 'G':
            comp = comp + 'C'
        else:
            comp = comp + 'G'
    return comp
