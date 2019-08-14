#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 14th August 2019: Added exception handling
Description: Program  reads the contents of file 'tempfile.txt', takes user input for number of grams and print the ngrams for the filr
'''

try:
    inp_file = open("tempfile.txt")
    n = int(input("Enter number grams"))

    for line in inp_file:
        count = 0
        words = line.split()
        for word in words[:-n + 1]:
            print(" ".join(words[count:count + n]))
            count += 1



except FileNotFoundError:
    print("tempfile.txt not found")

except PermissionError:
    print("Permission denied to read/write file")

except FileExistsError:
    print("tempfile.txt already exists and cannot be overwritten")

except IsADirectoryError:
    print("Requested file is a directory")

finally:
    try:
        inp_file.close()

    except AttributeError:
        pass

