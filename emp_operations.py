import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["office"]
mycol = mydb["employee"]
choice = "y"

try:

    while (choice != "n"):
        print("\n\n1.Add record\n2.Delete Record\n3.Update Record\n4.Search")
        ans = int(input("enter your choice : "))

        if (ans == 1):
            prevColCount = mycol.count()
            emp_id = input("enter id :")
            emp_name = input("enter Employee name : ")
            dept = input("enter dept name : ")
            doj = input("enter date of joining in dd/mm/yyyy form : ")
            salary = float(input("enter salary : "))
            my_record = {"emp_id": emp_id, "emp_name": emp_name, "dept": dept, "doj": doj,
                         "salary": salary}
            mycol.insert_one(my_record)
            print("\nrecord inserted\n")

        elif (ans == 2):
            ans = input("\nenter emp_id you want to Delete : ")
            myquery = {"emp_id": ans}

            for x in mycol.find(myquery):
                print(x)

            verify = input("\nDo you want to delete above record?(y/n) : ")
            if (verify == "y"):
                mycol.delete_one(myquery)
                print("\n\nRecord deleted succesfully\n\n")

        elif (ans == 3):
            emp_id = input("\nenter emp ID you want to update : ")
            myquery = {"emp_id": emp_id}

            record = mycol.find_one(myquery)

            if record is not None:
                for x in mycol.find(myquery):
                    print(x)

                field = input("\nEnter field name you want to update : ")
                new_data = input("\nEnter the new Data : ")
                verify = input("\nDo you want to update above record ?(y/n) : ")
                if (verify == "y"):
                    mycol.update_one({"emp_id": emp_id}, {"$set": {field: new_data}})
                    print("\n\nRecord Updated succesfully\n\n")

                for x in mycol.find(myquery):
                    print(x)

            else:
                print("\n\nRecord not Found")

        elif (ans == 4):
            emp_id = input("\nenter emp ID you want to Display : ")
            myquery = {"emp_id": emp_id}

            record = mycol.find_one(myquery)
            if record is not None:
                for x in mycol.find(myquery):
                    print(x)
            else:
                print("\n\nRecord Not Found\n\n")

        print("\nDo you Want to Continue ?\n")
        choice = input("your choice(y/n) : ")

except pymongo.errors.DuplicateKeyError:
    print("duplicate values identified while inserting")
