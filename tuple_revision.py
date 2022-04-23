# tuple
# tuple is immutable
t = (1, "this", 3.6, True)
# count the number of matching item
num = t.count(1)
print(num)
# search the index for matching item
match = t.index("this")
print(match)

items = [(1, 'a'), (2, 'b'), (3, 'c')]

for number, char in items:
    print(f"{number} {char}")
