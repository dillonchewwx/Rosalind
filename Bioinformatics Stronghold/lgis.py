# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:32:34 2021
@author: dillonchewwx
Solution to lgis on rosalind.info
"""
def main():
    file = open("Data/rosalind_lgis.txt")
    lines = file.read().splitlines()
    n = int(lines[0])
    permutation = lines[1].replace(" ", "")
    permutation_list = [int(num) for num in permutation]
    LIS = LongestIncreasingSubsequence(n, permutation_list)
    LDS = LongestDecreasingSubsequence(n, permutation_list)
    output = open("Data/rosalind_lgis_out.txt", "w")
    output.write(" ".join([str(x) for x in LIS]))
    output.write("\n")
    output.write(" ".join([str(x) for x in LDS]))
    output.close()
    file.close()

# The two functions below takes extremely long to run finish for N < 10000. Have to use an alternative method to solve this in less than 5 minutes.

def LongestIncreasingSubsequence(n, permutation_list):
    # Input: list of integers (permutation_list) of length n
    from itertools import combinations
    for length in range(n, 0, -1): # search in terms of decreasing length 
        for sub in combinations(permutation_list, length): # generate all combinations
            if list(sub) == sorted(sub):
                return sub
                break

def LongestDecreasingSubsequence(n, permutation_list):
    # Input: list of integers (permutation_list) of length n
    from itertools import combinations
    for length in range(n, 0, -1): # search in terms of decreasing length
        for sub in combinations(permutation_list, length): # generate all combinations
            if list(sub) == sorted(sub, reverse=True):
                return sub
                break
    
if __name__ == "__main__":
    main()
