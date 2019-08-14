functions = dir(list)
l = [1,2,4,1,2,5,7,84,25]
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
