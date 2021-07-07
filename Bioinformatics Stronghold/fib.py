# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:06:33 2021
@author: dillonchewwx
Solution to fib on rosalind.info
"""
def main():
    file = open("Data/rosalind_fib.txt")
    numbers = file.read().split(' ')
    n = int(numbers[0])
    k = int(numbers[1])
    print(fibonacci_rabbits(n,k)) 

def fibonacci_rabbits(n,k):
    child, adult = 1,0
    for i in range(n-1):
        child, adult = adult*k, adult + child
    return child + adult

if __name__ == "__main__":
    main()



