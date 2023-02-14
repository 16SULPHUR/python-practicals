my_string = raw_input("Enter string: ")

print("1) Data type of entered string: {0}".format(type(my_string)))

# split()
split_str = my_string.split()
print("2) Split string: {0}\n".format(split_str) )

# lower()
lower_str = my_string.lower()
print("3) Lowercase string: {0}\n".format(lower_str))

# upper()
upper_str = my_string.upper()
print("4) Uppercase string: {0}\n".format( upper_str))

# capitalize()
capitalize_str = my_string.capitalize()
print("5) Capitalized string: {0}\n".format( capitalize_str))

# title()
title_str = my_string.title()
print("6) Titlecase string: {0}\n".format( title_str))

# join()
words = ["Hello", "World"]
join_str = " ".join(words)
print("7) Join string: {0}\n".format( join_str))

# find()
find_str = my_string.find("is")
print("8) Index of 'is': {0}\n".format(find_str))

# replace()
replace_str = my_string.replace("is", "was")
print("9) Replaced string: {0}\n".format( replace_str))

# is
print("10) 'Hello' is my_string: {0}\n".format( 'Hello' is my_string))

# is not
print("11) 'Hello' is not my_string: {0}\n".format( 'Hello' is not my_string))

# in
print("12) 'Hello' in my_string: {0}\n".format(  'Hello' in my_string))

# not in
print("13) 'Hello' not in my_string: {0}\n".format(  'Hello' not in my_string))

# is upper
print("14) my_string is uppercase: {0}\n".format(my_string.isupper()))

# is lower
print("15) my_string is uppercase: {0}".format(my_string.islower()))
