from dict_ex import extract_values
from dict_ex import sum_values
from dict_ex import remove_key
from dict_ex import sort_dict_by_values
from dict_ex import merge_dicts
from dict_ex import keys_plus_values
from dict_ex import sort_with_key_values

def test_extract_values():
    test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
    assert extract_values(test_dict) == [1, 2, 5, 6, 7, 8, 10, 11, 12]

def test_sum_values():
    test_dict = {'a': 100, 'b': 200, 'c': 300}
    assert sum_values(test_dict) == 600

def test_remove_key():
    test_dict = {'a': 100, 'b': 200, 'c': 300}
    assert remove_key(test_dict, 'a') == {'b': 200, 'c': 300}

def test_sort_dict_by_values():
    test_dict = [{ "name" : "Nandini", "age" : 20},
                { "name" : "Manjeet", "age" : 20 },
                { "name" : "Nikhil" , "age" : 19 }]
    assert sort_dict_by_values(test_dict) == [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

def test_merge_dicts():
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    assert merge_dicts(dict1, dict2) == {'a': 10, 'b': 8, 'd': 6, 'c': 4}

def test_keys_plus_values():
    assert keys_plus_values({"Gfg" : 1, "is" :  3, "Best" : 2}) == ['Gfg', 'is', 'Best', 1, 3, 2]

def test_sort_keys_values():
    assert sort_with_key_values({"gfg": [7, 6, 3], "is": [2, 10, 3], "best": [19, 4]}) == {"best": [4, 19], "gfg": [3, 6, 7], "is": [2, 3, 10]}
