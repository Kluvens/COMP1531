# extract unique values dictionary values and finally return as a list
def extract_values(this_dict):
    result = []
    for key in this_dict.keys():
        for value in this_dict[key]:
            if value not in result:
                result.append(value)

    return sorted(result)

# find the sum of all items in a dictionary
def sum_values(this_dict):
    sum = 0
    for key in this_dict.keys():
        sum += this_dict[key]

    return sum

# remove a key from a dictionary
def remove_key(this_dict, this_key):
    this_dict.pop(this_key)
    return this_dict

# sort a list of dictionaries by a specific value('age')
def sort_dict_by_values(this_list):
    return sorted(this_list, key= lambda i: i['age'])

# merge two dictionaries
def merge_dicts(dict_one, dict_two):
    dict_one.update(dict_two)
    return dict_one

# Given a dictionary, perform append of keys followed by values in list.
def keys_plus_values(this_dict):
    return list(this_dict.keys()) + list(this_dict.values())

# sort dictionary key and values list
def sort_with_key_values(this_dict):
    result = {}
    for key in sorted(this_dict):
        result[key] = sorted(this_dict[key])

    return result
