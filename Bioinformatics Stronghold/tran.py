# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 13:23:20 2021
@author: dillonchewwx
Solution to tran on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_tran.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s1 = sequences[0]
    s2 = sequences[1]
    ratio = transitionTransversionRatio(s1, s2)
    with open("Data/rosalind_tran_out.txt", 'w') as output:
        output.write(str(ratio))

def transitionTransversionRatio(s1, s2):
    # Takes in two DNA strings (s1, s2) of same length and returns the transition/transversion ratio. 
    # A transition substitutes one purine for another (A to G) or a pyrimidine for another (C to T)
    # A transversion is the interchange of a purine for a pyrimidine or vice versa. 
    length = len(s1)
    transition = 0
    transversion = 0
    for i in range(length):
        if s1[i] == "A" and s2[i] == "G":
            transition += 1
        elif (s1[i] == "A" or s1[i] == "G") and (s2[i] == "C" or s2[i] == "T"):
            transversion += 1
        elif s1[i] == "G" and s2[i] == "A":
            transition += 1
        elif s1[i] == "C" and s2[i] == "T":
            transition += 1
        elif (s1[i] == "C" or s1[i] == "T") and (s2[i] == "A" or s2[i] == "G"):
            transversion += 1
        elif s1[i] == "T" and s2[i] == "C":
            transition += 1
    return(round(transition/transversion, 6))
    
if __name__ == "__main__":
    main()


