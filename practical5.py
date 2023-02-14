tpl=(5,7,9,9,66,66,66,66)

count_66= 66
count=tpl.count(count_66)

index_of_9= 9
index=tpl.index(index_of_9)

print("\n1) The element {0} occurs for {1} time in my tpl.\n".format(count_66, count))
print("2) The index of {0} in tpl is {1}.\n".format(index_of_9, index))

print("3) The element at 1st index in tpl is {0}.\n".format(tpl[1]))
print("4) The element from 0 to 2 in tpl is {0}.\n".format(tpl[0:2]))

element_to_update_at_2= 55
list1=list(tpl)
list1[2]= 55
tpl= tuple(list1)
print("5) The element at 2nd position is {0}.\n".format(tpl[2]))
