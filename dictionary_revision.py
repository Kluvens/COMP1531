# dictionary
dic = {
    "COMP1511" : "Programming Fundamentals",
    "COMP1521" : "OS Fundamentals",
    "COMP1531" : "Software Fundamentals"
}
print(dic)

# looping in dictionary
for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)

# copy a dictionary
dic2 = dic.copy()
print(dic2)

# get a matching value
print(dic.get("COMP1511"))

# see all items as tuples
# ('COMP1511', 'Programming Fundamentals')
t1 = dic.items()
print(t1)

# see all keys
print(dic.keys())

# pop the last item
dic.popitem()
print(dic)

# pop an item
dic.pop("COMP1521")
print(dic)

# see all values
print(dic.values())

# increase an item
dic.update({"COMP1521": "Operating System Fundamentals"})
print(dic)

# The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
print(dic.setdefault("COMP1511", 21))
print(dic.setdefault("COMP1531", 22))
print(dic)

# clear the dictionary
dic.clear()
print(dic)

# if not exist set to 0 if exists plus one
result = {}
for c in input:
    result[c] = result.get(c,0) + 1
return result

# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
