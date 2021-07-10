# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:24:29 2021
@author: dillonchewwx
Solution to perm on rosalind.info
"""
def main():
    file = open("Data/rosalind_perm.txt")
    numbers = file.read().split(' ')
    n = int(numbers[0])
    result = permutations(n)
    print()
    output = open("Data/rosalind_perm_out.txt", 'w')
    output.write(str(result[0]))
    output.write('\n')
    for y in range(len(result[1])):
        output.write(" ".join([str(x) for x in result[1][y]]) + '\n')
    output.truncate(output.tell()-2) # remove trailing newline
    file.close()

def permutations(n):
    import itertools
    import math
    return math.factorial(n), list(itertools.permutations(range(1,n+1)))

if __name__ == "__main__":
    main()




