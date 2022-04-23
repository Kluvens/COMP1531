from functools import reduce
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

items = ['a', 'b', 'c', 'd']
for i in range(len(items)):
    print(items[i])

for item in items:
    print(item)

for idx, item in enumerate(items):
    print(f"{idx}: {item}")

# Map: creates a new array with the results of calling a provided function on every element in the calling array
def shout(string):
    return string.upper() + '!'
better_items = list(map(shout, items))
print(better_items)

# Filter: creates a new array with all elements that pass the test implemented by the provided function
filtered_items = list(filter(lambda m: m != 'b', items))
print(filtered_items)

# Reduce: executes a reducer function (that you provide) on each member of the array resulting in a single output value
studentMarks = [55, 43, 34, 23, 22, 10, 26]
total = reduce(lambda a, b: a+b, studentMarks)
print(total)
