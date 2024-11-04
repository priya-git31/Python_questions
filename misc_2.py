# Sample data
fruits = ["apple", "banana", "cherry", "apple", "banana", "date"]
prices = [1.2, 0.5, 2.5, 1.2, 0.5, 3.0]
inventory = {"apple": 10, "banana": 5, "cherry": 7, "date": 3}
users = {"Alice": ["apple", "banana"], "Bob": ["cherry", "date"], "Charlie": ["apple", "date"]}
unique_numbers = {1, 2, 3, 4, 4, 5, 6}
grocery_list = ["apple", "egg", "milk", "banana", "orange", "egg", "banana"]
string_data = "Welcome to Python learning session!"

# Functions
def fruit_total_price(fruit, quantity):
    """Returns the total price for a given fruit and quantity."""
    if fruit in inventory:
        price_per_unit = prices[fruits.index(fruit)]
        return price_per_unit * quantity
    return 0

# Question 1: What is the unique count of items in the `fruits` list using a set?
def unique_set(list_name): 
    result = set(list_name)
    return result 

result = unique_set(fruits)
print(result)

# Question 2: Can you find the sum of all prices in the `prices` list?

def sum_prices(list_name): 
    result = sum(list_name)
    return result 

result = sum_prices(prices)
print(result)

# Question 3: How can you find the most frequent item in the `fruits` list using `Counter`?
from collections import Counter

def most_frequent(list_name): 
    result = Counter(list_name) 
    return result

result = most_frequent(fruits)
print(result)

# Question 4: How would you access the inventory count for "cherry" in the `inventory` dictionary?
def inventory_count(dictionary_name,item_name): 
    result = dictionary_name[item_name]
    return result 

result = inventory_count(inventory,"cherry")
print(result)

# Question 5: Write a line to add a new item "grape" with a count of 8 in the `inventory` dictionary.
def new_item_add(dictionary_name, item_name, item_count): 
    dictionary_name.update({item_name: item_count})
    return dictionary_name

result = new_item_add(inventory,"grape", 8)
print(result)


# Question 6: How would you create a list of unique items in the `grocery_list` using a set?
def unique_items(list_name): 
    result = set(list_name)
    return result 

result = unique_items(grocery_list)
print(result)

# Question 7: What will be the result of applying `fruit_total_price("apple", 3)`?
inventory = {"apple": 10, "banana": 5, "cherry": 7, "date": 3}

def fruit_price(fruit_name,quantity): 
    fruit_price_get = inventory[fruit_name]
    total = fruit_price_get * 3 
    return total 

result = fruit_price('apple', 3)
print(result)

# Question 8: Can you find the intersection between `unique_numbers` and `{4, 5, 6, 7}`?
unique_numbers = {1, 2, 3, 4, 4, 5, 6}
tem_numbers = {4,5,6,7}

def intersection_two(unique_numbers,tem_numbers): 
    result = unique_numbers.intersection(tem_numbers)
    return result

result = intersection_two(unique_numbers,tem_numbers)
print(result)

# Question 9: How would you split the `string_data` into words?
string_data = "Welcome to Python learning session!"

def split_data(string_name): 
    result = string_name.split()
    return result

result = split_data(string_data)
print(result)

# Question 10: How can you check if "egg" is in the `grocery_list`?
grocery_list = ["apple", "egg", "milk", "banana", "orange", "egg", "banana"]

def check_item(list_name,item_name): 
    result = item_name in list_name
    return result 

result = check_item(grocery_list, "egg")
print(result)

# Question 11: What is the total number of characters in `string_data` without counting spaces?
string_data = "Welcome to Python learning session!"

def count_char(string_name): 
    remove_space = string_name.replace(" ", "")
    result = len(remove_space)
    return result 

result = count_char(string_data)
print(result)

# Question 12: Write a line to remove "banana" from the `grocery_list` using a list method.
grocery_list = ["apple", "egg", "milk", "banana", "orange", "egg", "banana"]

def remove_item(list_name,item_name):
    while item_name in list_name: 
        list_name.remove(item_name)
    return list_name
    
result = remove_item(grocery_list,'banana')
print(result)
print(grocery_list)

# # Question 13: How would you reverse the order of items in the `grocery_list` list?
def reverse_list(list_name): 
    result = list_name.reverse()
    return result 

result = reverse_list(grocery_list)
print(result)
print(grocery_list)

# Question 14: How can you combine keys and values from `inventory` into a list of tuples?
inventory = {"apple": 10, "banana": 5, "cherry": 7, "date": 3}

def combine_tuple(dictionary_name): 
    dict_keys = dictionary_name.keys()
    dict_values = dictionary_name.values()
    combined_tuple = tuple(zip(dict_keys,dict_values))
    return combined_tuple

result = combine_tuple(inventory)
print(result)

# Question 15: Write a line to update "Alice's" favorite fruits to include "date".
users = {"Alice": ["apple", "banana"], "Bob": ["cherry", "date"], "Charlie": ["apple", "date"]}

def update_dict(dictionary_name, item_name, items): 
    dictionary_name[item_name].append(items)
    return dictionary_name

result = update_dict(users,"Alice", 'date')
print(result)

# Question 16: What code would you write to find the minimum and maximum numbers in `unique_numbers`?
unique_numbers = {1, 2, 3, 4, 4, 5, 6}

def max_min(set_name): 
    max_num = max(set_name)
    min_num = min(set_name)
    return max_num, min_num

result = max_min(unique_numbers)
print(result)

# Question 17: Write a line to remove duplicates from the `fruits` list using a set and convert it back to a list.
fruits = ["apple", "banana", "cherry", "apple", "banana", "date"]

def remove_duplicates(list_name): 
    convert_to_set = set(list_name)
    convert_to_list = list(convert_to_set)
    return convert_to_list

result = remove_duplicates(fruits)
print(result)

# Question 18: How can you merge `users` and another dictionary `{"David": ["milk", "banana"]}` into one dictionary?
another_dictionary =  {"David": ["milk", "banana"]}

def combine_dictionaries(orginal_dict,dict_2): 
    combined = orginal_dict | dict_2 
    return combined

result = combine_dictionaries(users,another_dictionary)
print(result)

# Question 19: How would you find the total quantity of "apple" from `inventory` and "Alice's" list?
# inventory = {"apple": 10, "banana": 5, "cherry": 7, "date": 3}
# users = {"Alice": ["apple", "banana"], "Bob": ["cherry", "date"], "Charlie": ["apple", "date"]}

# def total_quantity(dict1,dict2,item): 
#     dict_1_total = dict1[item]
#     dict_2_total = dict2[item].count(item)
#     total = dict_1_total + dict_2_total 
#     return total 

# result = total_quantity(inventory,users,"apple")
# print(result)


# Question 20: Can you write a lambda function to multiply each number in a list by 2 and apply it to `[1, 2, 3, 4]`?
# new_list = [1, 2, 3, 4]

# def lambda_function(list_name): 
#     result = (lambda x : x * 2, list_name)
#     return result 

# result = lambda_function(new_list)
# print(result)

new_list = [1, 2, 3, 4]

def lambda_function(list_name): 
    result = list(map(lambda x : x * 2, list_name))
    return result 

result = lambda_function(new_list)
print(result)


users = {"Alice": ["apple", "banana"], "Bob": ["cherry", "date"], "Charlie": ["apple", "date"]}

inventory = {"apple": 10, "banana": 5, "cherry": 7, "date": 3}

fruits = ["apple", "banana", "cherry", "apple", "banana", "date"]

for fruit in enumerate(fruits): 
    print(fruit)

unique_numbers = {1, 2, 3, 4, 4, 5, 6}
fruits = ["apple", "banana", "cherry", "d", "e", "f"]

result = fruits.remove(fruits[-2])
print(result)
print(fruits)


import this 

import math 
result = math.log(25)
print(result)
