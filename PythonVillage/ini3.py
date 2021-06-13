"""
Created on Sat Jun 12 17:20:49 2021
@author: dillonchewwx
Solution to ini3 on rosalind.info
"""
def main():
    file = open("rosalind_ini3.txt")
    lines = file.readlines()
    text = lines[0]
    index = lines[1].split(' ')
    file.close()
    print(text[int(index[0]):int(index[1])+1] + ' ' + text[int(index[2]):int(index[3])+1])
    return 

if __name__ == "__main__":
    main()

