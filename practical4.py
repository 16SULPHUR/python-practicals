my_list=[1,2,6,85,216,237]
print("0) DataType of my_list\n=> {0}\n".format(type(my_list)))

my_list.append(201)
print("1) list after appending\n=> {0}\n".format(my_list))

my_list.extend([125,224])
print("2) list after extending\n=> {0}\n".format(my_list))

my_list.insert(183,184)
print("3) list after inserting\n=> {0}\n".format(my_list))

my_list.remove(237)
print("4) list after removeing\n=> {0}\n".format(my_list))

indix_of_85=my_list.index(85)
print("5) Index position of element 85 is\n=> {0}\n".format(indix_of_85))

count_85=my_list.count(85)
print("6) Element 85 occurs for {0} time in my_list\n".format(count_85))

my_list.sort()
print("7) list after sorting\n=> {0}\n".format(my_list))

my_list.reverse()
print("8) list after revers operation\n=> {0}\n".format(my_list))

# my_list1=my_list.copy()
# print("9) copy of my list\n=> {0}\n".format(my_list1))

my_list.pop(2)
print("9) list removeing elementt from 2nd position\n=> {0}\n".format(my_list))

my_list_min=min(my_list)
my_list_max=max(my_list)
print("10) {0} is minimum value of my_list\n".format(my_list_min))
print("11) {0} is maximum value of my_list\n".format(my_list_max))
