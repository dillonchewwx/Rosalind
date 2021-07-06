# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:56:28 2021
@author: dillonchewwx
Solution to grph on rosalind.info
"""
def main():
    sequences = readFasta("Data/rosalind_grph.txt")
    output = open("Data/rosalind_grph_out.txt", 'w')
    for pair in adjacency_list(sequences, 3):
        output.write(" ".join([str(item) for item in pair]) + '\n')
    output.truncate(output.tell()-2) # remove trailing newline
    output.close()
    
def readFasta(fileName):
    file = open(fileName)
    dict = {}
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            words = line.split()
            name = words[0][1:]
            dict[name] = ''
        else:
            dict[name] += line
    file.close()
    return(dict)    

def adjacency_list(sequences, k):
    dictPrefix = {id: prefix(sequence, k) for (id, sequence) in sequences.items()}
    dictSuffix = {id: suffix(sequence, k) for (id, sequence) in sequences.items()}
    list = []
    for id1, suffixseq in dictSuffix.items():
        for id2, prefixseq in dictPrefix.items():
            if suffixseq == prefixseq and id1 != id2:
                list.append((id1, id2))
    return list

def prefix(sequence, k):
    return sequence[:k]

def suffix(sequence, k):
    return sequence[-k:]
    
if __name__ == "__main__":
    main()

