# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:14:34 2021
@author: dillonchewwx
Solution to pper on rosalind.info
"""

def main():
    file = open("Data/rosalind_pper.txt")
    numbers = file.read().split(' ')
    n, k = int(numbers[0]), int(numbers[1])
    print(partialPermutations(n, k))
    file.close()
    
def partialPermutations(n, k):
    import math
    return math.perm(n, k) % 1000000

    
if __name__ == "__main__":
    main()