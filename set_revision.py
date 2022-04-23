# set
se1 = {1, 3.0, "this"}
se2 = {True, "this", "is", 6.2}

# add an element
se1.add("hi")
print(se1)

# difference() returns the difference between two sets which is also a set. It doesn't modify the original sets.
print(se1.difference(se2))

# remove an element. If the element is not a member, raises a KeyError
se1.remove('hi')
print(se1)
se1.remove('this')
print(se1)

# pop the last element
se1.pop()
print(se1)

# if the two sets are disjoint
print(se1.isdisjoint(se2))

# if is subset
print(se1.issubset(se2))

# if is superset
print(se1.issuperset(se2))

# intersection
print(se1.intersection(se2))

# The intersection_update() updates the set calling intersection_update() method with the intersection of sets.
se1.intersection_update(se2)
print(se1)

# union
print(se1.union(se2))

# join two sets
se1.update(se2)
print(se1)

# discard() Removes an element from the set if it is a member. (Do nothing if the element is not in set)
se1.discard("this")
print(se1)

# The Python symmetric_difference() method returns the symmetric difference of two sets.
print(se1.symmetric_difference(se2))
