# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 01:30:23 2022
@author: dillonchewwx
Solution to kmp on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_kmp.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s = sequences[0]
    with open("Data/rosalind_kmp_out.txt", 'w') as output:
        output.write(" ".join([str(x) for x in KMPFailureArray(s)]))
    
def KMPFailureArray(s: str):
    # input: an array of characters, s (which is the sequence) with length n
    # output: an array of integers, P (which is the failure array)
    # The failure array is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is equal to some prefix s[1:k-j+1] where j does not equal 1. By convention, P[1]=0. 
    
    # Define n and P
    n = len(s)
    P = [0]*n
    
    # j is the prefix pointer
    j = 0
    
    for i in range(1, n):
        
        # reset j until match or beginning of pattern is reached
        while j and (s[i] != s[j]):
            j = P[j-1]
            
        # if match, record for current i and move j
        if s[j]==s[i]:
            j+=1
            P[i]=j
    return(P)

if __name__ == "__main__":
    main()