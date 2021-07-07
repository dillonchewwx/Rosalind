# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:21:43 2021
@author: dillonchewwx
Solution to iev on rosalind.info
"""
def main():
    file = open("Data/rosalind_iev.txt")
    numbers = [int(x) for x in file.read().split(' ')]
    print(expectedOffspring(numbers))
    file.close()

def expectedOffspring(numbers):
    AAAA = numbers[0] # P(dominant) = 1
    AAAa = numbers[1] # P(dominant) = 1
    AAaa = numbers[2] # P(dominant) = 1
    AaAa = numbers[3] # P(dominant) = 0.75
    Aaaa = numbers[4] # P(dominant) = 0.5
    aaaa = numbers[5] # P(dominant) = 0
    return (AAAA*1 + AAAa*1 + AAaa*1 + AaAa*0.75 + Aaaa*0.5 + aaaa*0)*2
    
if __name__ == "__main__":
    main()
