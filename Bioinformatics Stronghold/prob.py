# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:35:18 2021
@author: dillonchewwx
Solution to prob on rosalind.info
"""

def main():
    with open("Data/rosalind_prob.txt") as file:
        lines = [line.rstrip() for line in file]
    sequence = lines[0] 
    array = [float(num) for num in lines[1].split(' ')]
    output = open("Data/rosalind_prob_out.txt", "w")
    output.write(" ".join([str(prob) for prob in sequenceProbability(sequence, array)]))
    file.close()
    output.close()
    
def sequenceProbability(sequence, array):
    """
    Returns an array B having the same length as array A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match sequence s exactly.
    """
    import math
    B = []
    for gc in array:
        prob = 0
        log_gc = math.log(gc/2, 10)
        log_at = math.log((1-gc)/2, 10)
        for base in sequence:
            if base == "A" or base == "T":
                prob += log_at
            elif base == "G" or base == "C":
                prob += log_gc
        B.append(round(prob,3))
    return B
    
def gcContent(dna):
    return (dna.count('C') + dna.count('G'))/len(dna)

if __name__ == "__main__":
    main()