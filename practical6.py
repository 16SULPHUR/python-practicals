my_set = {2,5,2,8}

print("1) DataType of my_set is\n=> {0}\n".format(type(my_set)))

print("2) my_set = {0}\n".format(my_set))

# my_set.add(55)
my_set.add(55)
print("3) my_set.add(55)\n=> my_set = {0}\n".format(my_set))

# my_list = [45,35]
my_list = [45,35]
my_set.update(my_list)
print("4) my_list = [45,35]\n   my_set.update(my_list)\n=> my_set = {0}\n".format(my_set))

# my_set.discard(55)
my_set.discard(55)
print("5) my_set.discard(55)\n=> my_set = {0}\n".format(my_set))

# my_set_copy = my_set.copy()
my_set_copy = my_set.copy()
print("6) my_set_copy = my_set.copy()\n=> my_set_copy = {0}\n\n".format(my_set_copy))

temp_set1 = {35,45,55}
temp_set2 = {8,2}
temp_set3 = {11,89,99}
print("<--- my_set = {0} --->\n".format(my_set))
print("<--- temp_set1 = {0} --->\n\n".format(temp_set1))

# diffrence = my_set.difference(temp_set1)
diffrence = my_set.difference(temp_set1)
print("7) \"my_set\" has following elements that \"temp_set1\" dosen't\n=> {0}\n".format(diffrence))

# intersection_set = my_set.intersection(temp_set1)
intersection_set = my_set.intersection(temp_set1)
print("8) Common elements of \"my_set\" and \"temp_set1\"\n=> {0}\n".format(intersection_set))

union_set = my_set.union(temp_set1)
print("9) {0} + {1} \n=> {2}\n".format(my_set,temp_set1,union_set))

print("\n<--- my_set = {0} --->\n".format(my_set))
print("<--- temp_set1 = {0} --->\n".format(temp_set1))
print("<--- temp_set2 = {0} --->\n".format(temp_set2))
print("<--- temp_set3 = {0} --->\n\n".format(temp_set3))

# temp_set1.issubset(my_set)
print("10.1) Is \"temp_set1\" subset of \"my_set\"\n=> {0}\n".format(temp_set1.issubset(my_set)))

# temp_set2.issubset(my_set)
print("10.2) Is \"temp_set2\" subset of \"my_set\"\n=> {0}\n".format(temp_set2.issubset(my_set)))


# temp_set1.isdisjoint(my_set)
print("11.1) Is \"temp_set1\" intersection of \"my_set\"\n=> {0}\n".format(temp_set1.isdisjoint(my_set)))

# temp_set3.isdisjoint(my_set)
print("11.2) Is \"temp_set3\" intersection of \"my_set\"\n=> {0}\n".format(temp_set3.isdisjoint(my_set)))

# my_set.issuperset(temp_set1)
print("12.1) Is \"my_set\" superset of \"temp_set1\"\n=> {0}\n".format(my_set.issuperset(temp_set1)))
# my_set.issuperset(temp_set2)
print("12.2) Is \"my_set\" superset of \"temp_set2\"\n=> {0}\n".format(my_set.issuperset(temp_set2)))
# my_set.issuperset(temp_set3)
print("12.3) Is \"my_set\" superset of \"temp_set3\"\n=> {0}\n".format(my_set.issuperset(temp_set3)))

# my_set.clear()
my_set.clear()
print("13) Clearing my_set , Now my_set = {0}\n".format(my_set))
