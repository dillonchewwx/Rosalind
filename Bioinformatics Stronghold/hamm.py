# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 01:26:10 2021
@author: dillonchewwx
Solution to hamm on rosalind.info
"""

def main():
    file = open("Data/rosalind_hamm.txt")
    lines = file.readlines()
    s = lines[0]
    t = lines[1]
    file.close()
    print(hammingDistance(s, t))    

def hammingDistance(s,t):
    return sum(a != b for a, b in zip(s,t))

if __name__ == "__main__":
    main()

