# list
l = [1, 2, 3, "this", 5.6, False, True]

# append an item
l.append("hello")
print(l)

# get a copy of l called l2
l2 = l.copy()
print(l2)

# get the number of given item
# True is also 1, 1 is also True
print(l.count(1))
print(l.count(True))

# get the item at the first appearance
print(l.index(1))

# append another list
l.extend(l2)
print(l)

# insert at a given position
l.insert(0, 'h')
print(l)

# remove at a given position
l.pop(-1)
print(l)

# reverse a list
l.reverse()
print(l)

# sort the list
l3 = [5, 1, 3]
l3.sort()
print(l3)

# remove the first matching element
l.remove("this")
print(l)

# completely clear a list
l.clear()
print(l)

# slicing
print(l2[1:5])
