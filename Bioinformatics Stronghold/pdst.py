# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:45:11 2022
@author: dillonchewwx
Solution to pdst on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_pdst.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    result = pDistanceMatrix(sequences)
    with open("Data/rosalind_pdst_out.txt", 'w') as output:
        output.write('\n'.join([' '.join([str(cell) for cell in row]) for row in result]))

def pDistanceMatrix(sequences):
    # Input: A collection of n DNA strings s1, s2, ..., sn of equal length
    # Output: A matrix D corresponding to the p-distance on the strings
    # For two strings s1 and s2 of equal length, the p-distance is the proportion of corresponding symbols that differ between s1 and s2.
    
    length = len(sequences)
    seq_length = len(sequences[0])
    output = [[0 for j in range(length)] for i in range(length)] 
    
    for i in range(0,length):
        for j in range(0,length):
           output[i][j] += round(hammingDistance(sequences[i], sequences[j])/seq_length, 5)
    return(output)

def hammingDistance(s,t):
    return sum(a != b for a, b in zip(s,t))
    
if __name__ == "__main__":
    main()
