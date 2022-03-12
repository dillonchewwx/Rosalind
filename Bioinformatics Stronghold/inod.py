# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:37:22 2022
@author: dillonchewwx
Solution to inod on rosalind.info
"""
def main():
    with open("Data/rosalind_inod.txt") as file:
        lines = file.read().splitlines()
    n = int(lines[0])
    print(intNodes(n))
    
def intNodes(n):
# Takes in a positive integer n, 3≤n≤10000 and returns the number of internal nodes of any unrooted binary tree having n leaves.
    return n-2

if __name__ == "__main__":
    main()