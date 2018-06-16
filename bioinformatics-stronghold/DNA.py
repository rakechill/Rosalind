#Given: A DNA string s of length at most 1000 nt (nucleotides)
#Return: Four integers (separated by spaces) counting the
#        respective number of times that the symbols 'A',
#        'C', 'G', and 'T' occur in s.

def num_base_pair(s):
    A = 0
    C = 0
    G = 0
    T = 0
    for i in range(len(s)):
        if s[i] == 'A':
            A = A + 1
        elif s[i] == 'C':
            C = C + 1
        elif s[i] == 'G':
            G = G + 1
        else:
            T = T + 1
    print(A, C, G, T)
