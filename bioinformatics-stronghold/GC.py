# GC-content of a DNA string is given by percentage of guanine
# and cytosine in a DNA string

# usually a string in FASTA format is labeled by '>' and then a label
# Rosalind's implementation labels the first line with:
# ">Rosalind_xxxx" where xxxx will be between 0000 and 9999

# given: at most 10 DNA strings
# return: ID of string with highest GC-content and GC-content

def max_gc_content(gc_file):
    lines = list(open(gc_file, "r"))
    id_and_gc, i = {}, 0
    while i < len(lines):
        if lines[i][0] == ">":
            j = i + 1
            dna_string = ''
            while j < len(lines) and lines[j][0] != ">":
                dna_string = dna_string + lines[j].strip("\n")
                j += 1
            id_and_gc[lines[i].strip(">").strip("\n")] = gc_content(dna_string)
        i += 1
    max_key = max(id_and_gc, key= lambda k: id_and_gc[k])
    return max_key, id_and_gc[max_key]

def gc_content(dna_string):
    num_gc = 0
    for char in dna_string:
        if char == 'C' or char == 'G':
            num_gc += 1
    return num_gc / len(dna_string) * 100
