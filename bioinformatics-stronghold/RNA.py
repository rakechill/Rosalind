#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

def make_rna(dna):
    rna = ''
    for nt in dna:
        if nt == 'T':
            rna = rna + 'U'
        else:
            rna = rna + nt
    print(rna)
