"""
Created on Sat Jun 12 17:34:03 2021
@author: dillonchewwx
Solution to ini4 on rosalind.info
"""

def main():
    file = open("rosalind_ini4.txt")
    numbers = file.read().split(' ')
    numList=[num for num in list(range(int(numbers[0]), int(numbers[1])+1, 1)) if num % 2 ==1]
    print(sum(numList))
    return 

if __name__ == "__main__":
    main()


