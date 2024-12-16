#2Python Program to Check if a Key Exists in a Dictionary or Not

# dict_temp = dict(A=1, B=2, C=3)

# key=input("Enter a key to check:")

# if key in dict_temp.keys(): 
#     print("Yes, key exists")
# else:
#     print("No, key is not present")


# 4 Python Program to Find the Sum of All the Items in a Dictionary
# dict_temp = {"Math": 85, "Science": 97 , "History": 80}

# def find_sum(dict_name): 
#     dict_values = dict_name.values()
#     dict_sum = sum(dict_values)
#     return dict_sum

# result = find_sum(dict_temp)
# print(result)

# Python Program to Multiply All the Items in a Dictionary
# dict_temp={'A':10,'B':10,'C':239}
# total = 1 

# for values in dict_temp.values(): 
#     total = values * total 
# print(total)


# Python Program to Remove a Key from a Dictionary

# dict_temp={'A':10,'B':10,'C':239}

# print(dict_temp)

# key_del=input("Enter a key to be deleted(A,B,C,D): ")

# if key_del in dict_temp: 
#     del dict_temp[key_del]
#     print(dict_temp)
# else: 
#     if key_del not in dict_temp: 
#         print("Key not found")

# Python Program to Add a Key-Value Pair to the Dictionary

# key = input("Enter a key:")
# value = input("Enter a value:")
# temp_dict = {}

# temp_dict.update({key:value})
# print(temp_dict)

# Python Program to Concatenate Two Dictionaries
# dict1 = {'a': 10, 'b': 20}
# dict2 = {'c': 30, 'd': 40}

# dict_merged = dict1 | dict2
# print(dict_merged)

# Python Program to Map Two Lists into a Dictionary
# toys = ["teddy bear", "car", "doll", "robot"]
# prices = [10, 15, 12, 20]

# combined_dict = dict(zip(toys,prices))
# print(combined_dict)


# Python Program to Create a Dictionary with Key as First 
# Character and Value as Words Starting with that Character

# words = ['apple', 'banana', 'ant', 'ball', 'cat']
# result = {}

# for word in words:
#     first = word[0]  
#     if first in result:
#         result[first].append(word)
#     else:
#         result[first] = [word]

# print(result)


# Python Program to Create Dictionary that Contains Number

# numbers = {}

# for i in range(1,6): 
#     numbers[i] = i * i
# print(numbers)

text = "hello world hello python world python"

word_count = {}

# Python Program to Count the Frequency of Each Word in a String using Dictionary
for word in text.split():
    if word in word_count:
        word_count[word] = word_count[word] + 1   
    else:
        word_count[word] = 1     

print(word_count)