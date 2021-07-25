# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:57:04 2021
@author: chew.dw
Solution to pmch on rosalind.info
"""

def main():
    from Bio import SeqIO
    with open("Data/rosalind_pmch.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    print(perfectMatching(sequences))
    file.close()
    
def perfectMatching(sequences):
    # Since the string provided has the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G', all we need to do is just to find the number of combinations of {'A', 'U'} and {'C', 'G'}
    from math import factorial
    for sequence in sequences:
        return factorial(sequence.count("A")) * factorial(sequence.count("C"))
    
if __name__ == "__main__":
    main()