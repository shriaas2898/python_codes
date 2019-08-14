#!/usr/bin/python3

'''
Author: Aastha Shrivastava
PRN: 19030142001
Date modified: 13th August 2019: Added documentation
Description: Program  takes function name from user, if it is a valid list method it executes it and display the result
'''

functions = dir(list)
l = [1,2,4,1,2,5,7,84,25]
print("Current List:"+str(l))
func_name = input("Enter function's name")

if func_name in functions:
    if func_name in "append extend index":
        arg = input("Enter parameter value for %s"%func_name)
        print("Function return value: "+str(eval("l." + func_name + "('"+str(arg)+"')")))
        print("Updated list:"+str(l))

    elif func_name == "insert":
        pos = int(input("Enter index at which you want to enter"))
        val = input("Enter value to be Inserted ")
        print("Function return value: "+str(eval("l." + func_name + "(" + str(pos) + ",'" + val + "')")))
        print("Updated list:" + str(l))

    else:
        print("Function return value: "+str(eval("l." + func_name + "()")))
        print("Updated list:"+str(l))

else:
    print("Function name is not available for list")
