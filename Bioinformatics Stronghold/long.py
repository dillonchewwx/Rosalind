# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 02:21:12 2021
@author: dillonchewwx
Solution to long on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_long_test.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    print(Overlap(sequences))
    file.close()
    
def shortestSuperstring(sequences):
    # Takes in a list of sequences and returns the shortest superstring by gluing overlaps.
    shortestStr = sequences
    while len(shortestStr) > 1:
        # Find most overlapping string pair in shortestStr and replace the pair with the string obtained after combining them.
        
        
    return sequences

def Prefix(Pattern, i):
    return Pattern[:len(Pattern)-1]

def Suffix(Pattern, i):
    return Pattern[1:]

def findOverlappingPair(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    # Two strings are overlapping if prefix of one is the same as the suffix of the other and vice versa.  
    # Check suffix of str1 matches with prefix of str2
    for i in range(min(len1,len2)):
        if Suffix(str1, i) == Prefix(str2, i):
            maxlen = i
            str = seq1+Prefix(seq2,i)


if __name__ == "__main__":
    main()

