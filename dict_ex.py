# extract unique values dictionary values and finally return as a list
def extract_values(this_dict):
    result = []
    for key in this_dict.keys():
        for value in this_dict[key]:
            if value not in result:
                result.append(value)

    return sorted(result)
