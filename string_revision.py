string = "hello.hello.hey.are-you_okay"
# index method to search the first occurence, and return error if not found
print(string.index("llo"))
# rindex method to search the last occurence, and return error if not found(r means from right)
print(string.rindex("llo"))
# index method to search the first occurence, and return -1 if not found
print(string.find("llo"))
print(string.find("lllo"))
# index method to search the last occurence, and return -1 if not found
print(string.rfind("llo"))
print(string.rfind("lllo"))

# id() function returns the identity of the object.
print(id(string))

# first character to be capitalized
print(string.capitalize())
# every first character of a word to be capitalized
print(string.title())
# swap lower and upper case
print(string.swapcase())

# split the string and return a list (maxsplit from left)
left = string.split(".")
print(left)
left_max = string.split(".", maxsplit = 1)
print(left_max)
# split the string and return a list (maxsplit from right)
right = string.rsplit(".")
print(right)
right_max = string.rsplit(".", maxsplit = 1)
print(right_max)

# replace method(what we have, what we want, maximum time to be replaced)
print(string.replace("hello", "youh", 1))

# reverse a string
str[::-1]

f = 3.1415926
print("{:.3f}".format(f))
