# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:28:41 2021
@author: dillonchewwx
Solution to lgis on rosalind.info
"""
def main():
    file = open("Data/rosalind_lgis.txt")
    lines = file.read().splitlines()
    n = int(lines[0])
    permutation_list = [int(num) for num in lines[1].split()]
    LIS = LongestIncreasingSubsequence(n, permutation_list)
    LDS = LongestDecreasingSubsequence(n, permutation_list)
    output = open("Data/rosalind_lgis_out.txt", "w")
    output.write(" ".join([str(x) for x in LIS]))
    output.write("\n")
    output.write(" ".join([str(x) for x in LDS]))
    output.close()
    file.close()

 # v2 which uses dynamic programming rather than iteration.
def LongestIncreasingSubsequence(n, list):
    # Input: list of integers (list) of length n
    # Define a vector L[i] which contains the LIS that ends with list[i]
    L = []
    for i in range(n):
        # L[i] = for j < i and list[j] < list[i], pick L[j] with the maximum length and add list[i] to the end.
        L.append(max([L[j] for j in range(i) if L[j][-1] < list[i]] or [[]], key=len) + [list[i]])
    return max(L, key=len)

def LongestDecreasingSubsequence(n, list):
    # Input: list of integers (permutation_list) of length n
    # Define a vector L[i] which contains the LDS that ends with list[i]
    L = []
    for i in range(n):
        # L[i] for j < i and list[j] > list[i], pick L[j] with the maximum length and add list[i] to the end.
        L.append(max([L[j] for j in range(i) if L[j][-1] > list[i]] or [[]], key=len) + [list[i]])
    return max(L, key=len)
    
if __name__ == "__main__":
    main()

