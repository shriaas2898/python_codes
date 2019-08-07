#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 28th JULY 2019
               7th August 2019: added exception handling

Description: Program extracts usernames from  /etc/passwd file and stores in usernames.txt file
'''

try:
    # opening passwd file in read mode
    inp_file = open("/etc/passwd")
    # opening usernames.txt file in write mode
    out_file = open("usernames.txt", "w")

    # reading file line by line
    for line in inp_file:
        # printing extracted username in the file
        out_file.write(line.split(":")[0] + "\n")  # since the first value on very line of passwd file is username

    # closing connections to the file

except FileNotFoundError:
    print("/etc/passwd not found")

except PermissionError:
    print("Permission denied to read/write file")

except FileExistsError:
    print("Username.txt already exists and cannot be overwritten")

except IsADirectoryError:
    print("Requested file is a directory")

finally:
    try:
        inp_file.close()
        out_file.close()
    except AttributeError:
        pass