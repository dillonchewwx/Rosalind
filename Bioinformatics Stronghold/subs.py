# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:06:27 2021
@author: dillonchewwx
Solution to subs on rosalind.info
"""

def main():
    file = open("Data/rosalind_subs.txt")
    lines = file.read().splitlines()
    s = lines[0]
    t = lines[1]
    file.close()
    print(motifFinder(s,t))
    
def motifFinder(s,t):
    location = ""
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            location += str(i+1) + " "
    return location

if __name__  == "__main__":
    main()

