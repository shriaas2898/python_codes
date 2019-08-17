#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 17th August 2019

Description: Program defines a class Person to read data from file whose path is supplied by user and perform the specified operations.
'''
#class to store records present in file supplied by user
class Person(object):

    def __init__(self,first_name='fn',last_name='ln',phone_no="pn"):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no

    def show_details(self):
        return self.first_name+","+self.last_name+","+self.phone_no

try:
    # opening filename supplied by user in read mode
    inp_file = open(input("Enter path of the file"))

    persons = []

    #storing records from file as list of Person objects
    for line in inp_file:
            person = line.split(",")
            persons.append(Person(person[0],person[1],person[2].strip()))


    print("\nUnique first names records")
    first_uniques = []
    for person in persons:
        if person.first_name not in first_uniques:
            first_uniques.append(person.first_name)
            print(person.show_details())

    print("\nSurnames without phone number starting with 9")
    for person in persons:
        if person.phone_no[0] is not '9':
            print(person.last_name)

    print("\nLast name greater the 4 charcter and 3rd character is between a and m")
    for person in persons:
        if len(person.last_name)>3 and person.last_name[2] not in "abcdefghijklm":
            print(person.show_details())

    print("\nPhone numbers first and last number is odd")
    for person in persons:
        if int(person.phone_no[0])%2==1 and int(person.phone_no[-1])%2==1:
            print(person.show_details())

    print("\nDiffrence between First characters of first and last name is at least 5")
    for person in persons:
        if abs(ord(person.first_name[0].upper())-ord(person.last_name[0].upper())) >4:
            print(person.show_details())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied to read file")

except IsADirectoryError:
    print("Requested file is a directory")

except ValueError:
    print("Invalid value found please check records in file")

except IndexError:
    print("File may have some incomplete records please check")
finally:
    try:
        inp_file.close()

    except AttributeError:
        pass