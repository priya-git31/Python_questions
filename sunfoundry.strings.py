
# # 4 Python Program to Replace All Occurrences of ‘a’ with $ in a String
# string_input = input("Enter a string: ")

# def replace_string(given_string,existing,replaced): 
#     result = given_string.replace(existing, replaced)
#     return result

# result = replace_string(string_input, "a", "$")
# print(result)   


# # 5 Python Program to Replace Every Blank Space with Hyphen in a String
# string_input = input("Enter a string: ")

# def replace_string(given_string,existing,replaced): 
#     result = given_string.replace(existing, replaced)
#     return result

# result = replace_string(string_input, " ", "-")
# print(result) 


# 2 Python Program to Remove Odd Indexed Characters in a string
# string_temp = "Acotara"
# print(string_temp[0::2])


# 17 Python Program to Check if the Substring is Present in the Given String
# string_input = input("Enter a string: ")
# string_substring = input("Enter a word: ")

# def check_substring(string_input,string_substring): 
#     if string_substring in string_input: 
#         return "True"
#     else: 
#         return "False"
    
# result = check_substring(string_input,string_substring)
# print(result)


# 22 Python Program to Create a New String Made up of First and Last 2 Characters
# original_string = input("Enter a word: ")

# def creating_new(original_string): 
#     new_string = original_string[0] + original_string[-2:]
#     return new_string 

# result = creating_new(original_string)
# print(result)

# 12 Python Program to Count the Number of Vowels in a String

# given_string = "Facebook"

# def count_vowels(given_string): 
#     empty_string = 0
#     for i in given_string: 
#             if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#                  empty_string = empty_string + 1
#     return empty_string 

# result = count_vowels(given_string)
# print(result)

#LOOPS 
# given_string = input("Enter a word: ")

# empty_string = 0

# for i in given_string: 
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         empty_string = empty_string + 1
# print(empty_string)


# # 11 Python Program to Count Number of Lowercase Characters in a String

given_string = input("Enter a word: ")

empty_string = 0 

for i in given_string: 
    if i == i.lower():
        empty_string = empty_string + 1
print(empty_string)