try:
    myFile = open("Employee.txt", "r")
    # do something here... inside this opena nd close function.
    # looping the files
    for name_of_emp in myFile.readlines():
        print(name_of_emp)
    # print(myFile.read())
    myFile.close()

    new_file = open("Html.html" , "r")
    new_file.read()
except ValueError as err:
    print(err)

