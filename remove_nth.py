#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 27th JULY 2019
               7th August 2019: added exception handling
Description: Program reads file supplied by user, takes an intger value n from user and writes the file contents in new file
without every nth character on each line.
'''



try:
    #opening connection to file which user entered
    inp_file = open(input("Enter file name"))
    out_file = open("tempout.txt", "w")
    skip_char = int(input("Enter character number to skip"))

    #reading file line by line
    for line in inp_file:
        start = 0
        end = skip_char - 1
        #writing the contents to output file and skipping the nth character
        while (start <= len(line)):
            out_file.write(line[start:end])
            start = end + 1
            end += skip_char


#possible exceptions program may encounter
except FileNotFoundError:
    print("File not found please check the file name and try executing program again")
except TypeError:
    print("Character number must be an integer please execute the program again and enter a valid value")
except PermissionError:
    print("Permission denied to read/write file")
except FileExistsError:
    print("tempout.txt already exists and cannot be overwritten")
except IsADirectoryError:
    print("Requested file is a directory")

#closing the file
finally:
    try:
        inp_file.close()
        out_file.close()
    except AttributeError:
        pass