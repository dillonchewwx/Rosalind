# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:55:25 2021
@author: dillonchewwx
Solution to sseq on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_sseq.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s = sequences[0]
    t = sequences[1]
    indexes = subsequenceIndex(s, t)
    with open("Data/rosalind_sseq_out.txt", 'w') as output:
        output.write(" ".join([str(index) for index in indexes]))

def subsequenceIndex(s, t):
    # Takes in two DNA strings (s, t) and returns a collection of indices of s in which the symbols of t appear as a subsequence of s.
    s_index = 0
    index_list = []
    for i in range(len(t)):
        for j in range(len(s)): 
            if t[i] == s[j] and j > s_index:
                s_index = j
                index_list.append(j+1)
                break
    return index_list
    
if __name__ == "__main__":
    main()

