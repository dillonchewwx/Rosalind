# -*- coding: utf-8 -*-
"""
Created on Wed Jul 7 15:12:55 2021
@author: dillonchewwx
Solution to lcsm on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_lcsm.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    print(longestCommonSubstring(sequences))
    file.close()
    
def longestCommonSubstring(sequences):
    # First sort sequences by length from longest to shortest
    sequences.sort(key=len, reverse=True)
    # Create a list of substrings from the longest sequence and sort it from longest to shortest
    longestSeq = sequences.pop(0)
    subStrings = [longestSeq[i:j] for i in range(len(longestSeq)) for j in range(len(longestSeq), i, -1)]
    subStrings.sort(key=len, reverse=True)
    # Check if substrings from longest to shortest are present in the next longest string. If it is not in the next longest string, then break the loop. If it passes all checks, then it is the longest substring. 
    for subString in subStrings:
        for sequence in sequences:
            if subString not in sequence:
                break
        else:
            return subString
            break
    
if __name__ == "__main__":
    main()
