# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:40:36 2022
@author: dillonchewwx
Solution to corr on rosalind.info
"""
def main():
    from Bio import SeqIO
    with open("Data/rosalind_corr.txt") as file:
        sequences = [str(sequence.seq) for sequence in list(SeqIO.parse(file, 'fasta'))]
    correct, incorrect = checkCorrectIncorrect(sequences)
    corrections = makeCorrections(correct, incorrect)
    # Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
    with open("Data/rosalind_corr_out.txt", 'w') as output:
        for pair in corrections:
            output.write("->".join([seq for seq in pair]))
            output.write('\n')
        output.truncate(output.tell()-2)
        output.close()
    file.close()
        
def hammingDistance(s,t):
    return sum(a != b for a, b in zip(s,t))

def reverseComplement(DNAstring):
    trans = DNAstring.maketrans('ACGT', 'TGCA')
    return DNAstring[::-1].translate(trans)

def checkCorrectIncorrect(s):
    # For each read s in the dataset
    # s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
    correct = []
    temp = []
    incorrect = []
    from collections import Counter
    counts = Counter(s)
    for i in counts:
        if counts[i] >= 2:
            correct.append(i)
        elif i in s:
            temp.append(i)
    temprev = [reverseComplement(seq) for seq in temp]
    import itertools
    filteredseqs = list(itertools.chain(*[temp, temprev]))
    filteredcounts = Counter(filteredseqs)
    for j in filteredcounts:
        if filteredcounts[j] >= 2 and reverseComplement(j) not in correct:
            correct.append(j)
        elif j in s and reverseComplement(j) not in correct:
            incorrect.append(j)
    return correct, incorrect

def makeCorrections(correct, incorrect):
    # s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
    corrections = []
    for s in incorrect:
        for t in correct:
            if hammingDistance(s, t) == 1:
                corrections.append([s,t])
            elif hammingDistance(s, reverseComplement(t)) == 1:
                corrections.append([s, reverseComplement(t)])
    return corrections
    
if __name__ == "__main__":
    main()