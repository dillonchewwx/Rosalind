# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 01:30:04 2021
@author: dillonchewwx
Solution to fibd on rosalind.info
"""

def main():
    file = open("rosalind_fibd.txt")
    numbers = file.read().split(' ')
    n = int(numbers[0])
    m = int(numbers[1])
    print(mortal_fibonacci_rabbits(n, m)) 
    file.close()

def mortal_fibonacci_rabbits(n, m):
    # When n > m, recurrence relation here is F(n,m) = F(n-1) + F(n-2) - F(n-(m+1))
    ages = [1] + [0]*(m-1) # If m=3, then [1, 0, 0] indicates the number of rabbits which are 1, 2 and 3 months old respectively. 
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

if __name__ == "__main__":
    main()



