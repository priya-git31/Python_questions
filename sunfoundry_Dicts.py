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