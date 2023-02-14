"""  write a python program to demostrate the creation of a dictionary student with the name , age and branch of a student.
1. demonstrate the updation of python dictionary.
2. demonstrate the removal of element from the python dictionary.
3. demonstrate the use of following dictionary methods - clear() , copy() , get(), items(), popitem(), and values().
 """


my_dict={"std_name":"Ankit Patil",
    "std_branch":"CSE",
    "std_DOB":"15/03/2005"}
print(my_dict)

print ("Update Dictionary")
my_dict["std_name"]="Shivam Maisuriya"
print(my_dict)

print ("Delete  ")
del my_dict["std_DOB"]
print(my_dict)


print ("Copy Dictionary")
my_dict1=my_dict.copy()
print(my_dict1)

print ("Get")
my_dict_get = my_dict.get("std_name")
print(my_dict_get)

print ("Item")
my_dict_items=my_dict.items()
print(my_dict_items)

print ("Values")
my_dict_values= my_dict.values()
print(my_dict_values)

print ("Keys")
my_dict_keys= my_dict.keys()
print(my_dict_keys)

print ("popitem")
my_dict.popitem()
print(my_dict)


my_dict.clear()
print(my_dict)
