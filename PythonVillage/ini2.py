"""
Created on Sat Jun 12 16:31:54 2021
@author: dillonchewwx
Solution to ini2 on rosalind.info
"""
def main():
    file = open("rosalind_ini2.txt")
    numbers = file.read().split(' ')
    a = int(numbers[0])
    b = int(numbers[1])
    print(a**2 + b**2)
    file.close()
    return 

if __name__ == "__main__":
    main()



