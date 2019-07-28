#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 27th JULY 2019

Description: Program reads file supplied by user, takes an intger value n from user and writes the file contents in new file
without every nth character on each line.
'''


try:
    inp_file = open(input("Enter file name"))
    out_file = open("tempout.txt", "w")
    size = int(input("Enter character number to skip"))
    for line in inp_file:
        start = 0
        end = size - 1
        while (start <= len(line)):
            out_file.write(line[start:end])
            start = end + 1
            end += size

    inp_file.close()
    out_file.close()
except FileNotFoundError:
    print("File not found please check the file name and try executing program again")
except TypeError:
    print("Character number must be an integer please execute the program again and enter a valid value")