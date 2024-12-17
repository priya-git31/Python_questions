
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


# # 2 Python Program to Remove Odd Indexed Characters in a string
# string_temp = "Acotara"
# print(string_temp[0::2])


# # 17 Python Program to Check if the Substring is Present in the Given String
# string_input = input("Enter a string: ")
# string_substring = input("Enter a word: ")

# def check_substring(string_input,string_substring): 
#     if string_substring in string_input: 
#         return "True"
#     else: 
#         return "False"
    
# result = check_substring(string_input,string_substring)
# print(result)


# # 22 Python Program to Create a New String Made up of First and Last 2 Characters
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

# LOOPS 
# given_string = input("Enter a word: ")

# empty_string = 0

# for i in given_string: 
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         empty_string = empty_string + 1
# print(empty_string)


# # 11 Python Program to Count Number of Lowercase Characters in a String

# given_string = input("Enter a word: ")

# empty_string = 0 

# for i in given_string: 
#     if i == i.lower():
#         empty_string = empty_string + 1
# print(empty_string)

# given_string = input("Enter a word: ")

# count = 0 

# for i in given_string:
#     if i.islower(): 
#         count = count + 1
# print(count)

# 11 Python Program to Count the Number of Digits and Letters in a String

# given_string = "Apple is 4"

# count_letter = 0 
# count_digit = 0 

# for i in given_string: 
#     if i.isdigit(): 
#         count_letter = count_letter + 1
#     else: 
#         if i.isalpha(): 
#             count_digit = count_digit + 1
# print(count_letter)
# print(count_digit)

# 13 Python Program to Count Number of Uppercase and Lowercase Letters in a String
# given_string = input("Enter a word: ")

# lower_count = 0 
# upper_count = 0 

# for i in given_string: 
#     if i.islower(): 
#         lower_count = lower_count + 1 
#     else: 
#         if i.isupper(): 
#             upper_count = upper_count + 1 
# print(f"lower count is {lower_count}")
# print(f"upper count is {upper_count}")

# 28 Python Program to Check if a Given String is Palindrome
# given_string = "yooy"

# def is_palindrome(given_string): 
#     if given_string == given_string[::-1]: 
#         return "Palindrome"
#     else: 
#         return "Not Palindrome"
    
# result = is_palindrome(given_string)
# print(result)


#7 Python Program to Reverse a String Without using Recursion
# given_string = input("Enter a word: ")

# def reverse_string(given_string): 
#     result = given_string[::-1]
#     return result 

# result = reverse_string(given_string)
# print(result)


#9 Python Program to Find the Length of a String without Library Function

# given_string = input("Enter a word: ")

# count = 0 
# for i in given_string: 
#     count = count + 1 
# print(count)

# 23 Python Program to Find the Larger String without using Built-in Functions

# string_1 = "Facebook"
# string_2 = "Instagram"

# count_1 = 0 
# count_2 = 0 

# for i in string_1: 
#     count_1 = count_1 + 1 

# for i in string_2: 
#     count_2 = count_2 + 1 

# if count_1 > count_2: 
#     print("String_1 greater than string_2")
# elif count_1 == count_2 :
#     print("String_1 and String_2 are equal")
# elif count_2 > count_1: 
#     print("String_2 is greater than String_1")

# Python Program to Find Common Characters in Two Strings
# string_1 = "Hello"
# string_2 = "World"

# common_characters = set(string_1) & set(string_2)
# print(common_characters)

# # Python Program to Print All Letters Present in Both Strings
# string_1 = "Hello"
# string_2 = "World"

# all_characters = set(string_1) | set(string_2)
# print(all_characters)

# Python Program that Displays which Letters are in First String but not in Second
# string_input=input("Enter string_1:") 
# string_input_2=input("Enter string_2:") 

# def all_string_1(string_input,string_input_2): 
#     string_difference = set(string_input) - set(string_input_2)
#     return string_difference 

# result = all_string_1(string_input,string_input_2)
# print(result)

# Python Program that Displays Letters that are not Common in Two Strings
# string_input=input("Enter string_1:") 
# string_input_2=input("Enter string_2:")

# def not_common_strings(string_input,string_input_2): 
#     difference_strings = set(string_input) ^ set(string_input_2)
#     return difference_strings

# result = not_common_strings(string_input, string_input_2)
# print(result)

# Python Program to Swap the First and the Last Character of a String
#  string_input=input("Enter string_1:") 

string_1 = "Hello"

def swap_first_last(string_1): 
    if len(string_1) <= 1: 
        return string_1
    return string_1[-1] + string_1[1:-1] + string_1[0]
  
result = swap_first_last(string_1)
print(result)

