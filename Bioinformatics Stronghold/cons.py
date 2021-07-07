# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:25:07 2021
@author: dillonchewwx
Solution to cons on rosalind.info
"""
def main():
    seqs = readFasta("Data/rosalind_cons.txt")
    output = open("Data/rosalind_cons_out.txt", 'w')
    result = consensus(seqs.values())
    output.write("".join([str(item) for item in result[0]]) + "\n")
    output.write("A: " + " ".join([str(item) for item in result[1][0]]) + "\n")
    output.write("C: " +  " ".join([str(item) for item in result[1][1]]) + "\n")
    output.write("G: " + " ".join([str(item) for item in result[1][2]]) + "\n")
    output.write("T: " + " ".join([str(item) for item in result[1][3]]))
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

def consensus(sequences):
    import numpy as np
    consensus_lengths = [len(x) for x in sequences]
    consensus_matrix = [[0 for i in range(consensus_lengths[0])] for j in range(4)]
    for sequence in sequences:
        for k in range(len(sequence)):
            if sequence[k] == "A":
                consensus_matrix[0][k] += 1
            elif sequence[k] == "C":
                consensus_matrix[1][k] += 1
            elif sequence[k] == "G":
                consensus_matrix[2][k] += 1
            elif sequence[k] == "T":
                consensus_matrix[3][k] += 1
    consensus_sequence_index = np.argmax(consensus_matrix, axis=0)
    consensus_sequence = [IndexToLetter(l) for l in consensus_sequence_index]
    return consensus_sequence, consensus_matrix
    
def IndexToLetter(index):
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
    
if __name__ == "__main__":
    main()

