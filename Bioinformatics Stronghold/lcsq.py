# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:27:02 2022
@author: dillonchewwx
Solution to lcsq on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_lcsq.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    s = sequences[0]
    t = sequences[1]
    with open("Data/rosalind_lcsq_out.txt", 'w') as output:
        output.write("".join([str(x) for x in longestCommonSubsequence(s, t)]))

def longestCommonSubsequence(s, t):
    # Input: Two DNA strings s and t (each having length at most 1 kbp)
    # Output: A longest common subsequence of s and t.
    # A string, u, is a common subsequence of strings s and t if the symbols of u appear in order as a subsequence of both s and t. 
    # For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA"
    
    # A brute force approach is to generate all possible subsequences in both strings and find the longest matching subsequence. This however will have an exponential time complexity. We will probably have to solve this with dynamic programming.
    
    # Create 2D table.
    # Make a table with dimensions len(s)+1, len(t)+1. 
    # Insert a null column and row to represent the end of the string.
    # Insert zeros in all first rows and columns.
    
    LCS = [[0 for x in range(len(t)+1)] for x in range(len(s)+1)]
    
    # Fill current cell by adding one to the diagonal element if the character equivalent to the current row and column matches. 
    # Otherwise, fill current field with the largest value from preceding column and row element. 
    
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i==0 or j==0:
                LCS[i][j] = 0
            elif s[i-1] == t[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
          
    # Length of longest common subsequence is in the final row and column
    LCS_length = LCS[len(s)][len(t)]
    
    # Create character array to store string
    u = [""] * (LCS_length+1)
    
    # Start from the bottom right corner and store characters. 
    a = len(s)
    b = len(t)
    
    while a > 0 and b > 0:
        # If current character are similar, then it is part of u
        if s[a-1] == t[b-1]:
            u[LCS_length-1] = s[a-1]
            a -= 1
            b -= 1
            LCS_length -= 1
        # If different, find larger and go in that direction
        elif LCS[a-1][b] > LCS[a][b-1]:
            a -= 1
        else: 
            b -= 1
            
    return(u)
    

if __name__ == "__main__":
    main()

