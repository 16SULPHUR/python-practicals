"""  write a python program to demostrate the creation of a dictionary student with the name , age and branch of a student.
1. demonstrate the updation of python dictionary.
2. demonstrate the removal of element from the python dictionary.
3. demonstrate the use of following dictionary methods - clear() , copy() , get(), items(), popitem(), and values().
 """


My_Dictionary={"Stdudent_Name":"Ankit Patil",
    "Stdudent_Branch":"CSE",
    "Stdudent_DOB":"15/03/2005"
}

# type(My_Dictionary)
print("1) DataType of My_Dictionary is : {0}\n".format(type(My_Dictionary)))

# My_Dictionary
print("2) My_Dictionary : {0}\n".format(My_Dictionary))

# My_Dictionary["Stdudent_Name"]="Shivam Maisuriya"
My_Dictionary["Stdudent_Name"]="Shivam Maisuriya"
print("3) After Updating student's name to \"Shivam Maisuriya\"\n=> Now My_Dictionary is : {0}\n".format(My_Dictionary))

# My_Dictionary["Stdudent_Name"]="Shivam Maisuriya"
# del My_Dictionary['Student_DOB']
# print("4) After Deleting student's DOB\n=> Now My_Dictionary is : {0}\n".format(My_Dictionary))


# My_Dictionary=My_Dictionary.copy()
Temp_Dictionary=My_Dictionary.copy()
print("5) After coping \"My_Dictionary\" in \"Temp_Dictionary\"\n=> Now Temp_Dictionary is : {0}\n".format(Temp_Dictionary))

# My_Dictionary_get = My_Dictionary.get("Student_Name")
# My_Dictionary_get = My_Dictionary.get('Student_Name')
# print("6) Getting \"Student_Name\" from \"My_Dictionary\"\n=> Now Temp_Dictionary is : {0}\n".format(My_Dictionary_get))

print ("Item")
My_Dictionary_items=My_Dictionary.items()
print(My_Dictionary_items)

# print ("Values")
# My_Dictionary_values= My_Dictionary.values()
# print(My_Dictionary_values)

# print ("Keys")
# My_Dictionary_keys= My_Dictionary.keys()
# print(My_Dictionary_keys)

# print ("popitem")
# My_Dictionary.popitem()
# print(My_Dictionary)


# My_Dictionary.clear()
# print(My_Dictionary)
