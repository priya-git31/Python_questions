# # len(string): Returns the length (number of characters) of the string.
# # string.upper(): Converts all characters in the string to uppercase.
# # string.lower(): Converts all characters in the string to lowercase.
# # string.capitalize(): Capitalizes the first character of the string.
# # string.title(): Converts the string to title case where the first letter of each word is capitalized.

# # string.strip(): Removes leading and trailing whitespace characters from the string.
# # string.startswith(prefix): Returns True if the string starts with the specified prefix.
# # string.endswith(suffix): Returns True if the string ends with the specified suffix.
# # string.replace(old, new): Replaces all occurrences of the old substring with the new substring.
# # string.split(separator): Splits the string into a list of substrings based on the separator.

# # string.join(iterable): Joins a list of strings into one string using the original string as a separator.
# # string.find(substring): Returns the index of the first occurrence of a substring in the string.
# # string.rfind(substring): Returns the index of the last occurrence of a substring in the string.
# # string.isalpha(): Returns True if all characters in the string are alphabetic.
# # string.isdigit(): Returns True if all characters in the string are digits.

# # string.isalnum(): Returns True if all characters in the string are alphanumeric.
# # string.islower(): Returns True if all characters in the string are lowercase.
# # string.isupper(): Returns True if all characters in the string are uppercase.
# # string.isnumeric(): Returns True if all characters in the string are numeric.
# # string.count(substring): Returns the number of non-overlapping occurrences of a substring in the string.

# # ------------------------ Questions on string 1
# this_string = "Hello, World!"


# # How can you convert "Hello, World!" to all lowercase characters?
# print(this_string.lower())

# # What method would you use to check if String 1 starts with "Hello"?
# print(this_string.startswith("Hello"))
      
# # How do you find the index of the first occurrence of "o" in String 1?
# print(this_string.find("o"))

# # What is the result of replacing "Hello" with "Hi" in String 1?
# print(this_string.replace("Hello", "Hi"))

# # How can you remove leading and trailing whitespace characters from String 1?
# stripped_string = this_string.strip()
# print(stripped_string )

# # What is the output of splitting String 1 by ","?
# print(this_string.split(","))

# # How would you join the list ["Hello", "World!"] into a single string using a space as a separator?
# joined_string = ' '.join(["Hello", "World"])
# print(joined_string)

# # How do you check if String 1 contains only alphanumeric characters?
# isalphanum = this_string.isalnum()
# print(isalphanum)

# # What is the count of "l" characters in String 1?
# count_l = this_string.count("l")
# print(count_l)

# # Is String 1 ending with an exclamation mark?
# ends_with = this_string.endswith("!")
# print(ends_with)

# # ------------------------ Questions on string 2
# another_string = "Python Programming"

# # How can you capitalize the first letter of each word in String 2?
# # string.capitalize(): Capitalizes the first character of the string.

# capitalize_string = another_string.title()
# print(capitalize_string)

# # What method allows you to check if String 2 contains only digits?
# # string.isdigit(): Returns True if all characters in the string are digits.

# is_digits = this_string.isdigit()
# print(is_digits)

# # How would you verify if String 2 is a valid identifier (variable name) in Python?
# print(this_string.isidentifier())


# # What is the result of replacing "Python" with "Java" in String 2?
# replaced_string = another_string.replace("Python", "Java")
# print(replaced_string)


# # What method is used to swap the case of characters in String 2?
# swapped_string = another_string.swapcase()
# print(swapped_string)

# # How do you determine if String 2 starts with any of the prefixes "Py" or "Java"?
# result = another_string.startswith("Py","Java")
# print(result)


# Python Program to Replace All Occurrences of ‘a’ with $ in a String
# string_input=input("Enter a word: ")

# def replaced_string(string_input,given_word,replaced_word): 
#     if given_word in string_input: 
#         new_string = string_input.replace(given_word,replaced_word)
#         return new_string 
    
# result = replaced_string(string_input,"a", "$")
# print(result)

# Python Program to Replace Every Blank Space with Hyphen in a String
# string_input=input("Enter a word: ")

# def replaced_blank_space(string_input,existing, replaced):
#     if existing in string_input: 
#         new_string = string_input.replace(existing,replaced)
#         return new_string 
    
# result = replaced_blank_space(string_input," ", "-")
# print(result)

# Python Program to Reverse a String Without using Recursion
# string_input=input("Enter a word: ")

# reversed_string = string_input[::-1]

#9 Python Program to Find the Length of a String without Library Function
# string_input=input("Enter a word: ")

# count = 0 
# for i in string_input: 
#     count = count + 1
# print(count)

# Python Program to Count Number of Lowercase Characters in a String
# string_input=input("Enter a word: ")

# count_lower = 0 
# for i in string_input: 
#     if i.islower(): 
#         count_lower = count_lower + 1
# print(count_lower)


# Python Program to Count the Number of Vowels in a String
# string_input=input("Enter a word: ")

# vowels = ["a", "e", "i", "o", "u"]
# vowels_count = 0 

# for i in string_input: 
#     if i.lower() in vowels: 
#         vowels_count = vowels_count + 1 
# print(vowels_count)


# Python Program to Count Number of Uppercase and Lowercase Letters in a String
# string_input=input("Enter a word: ")

# count_lower = 0 
# count_upper = 0 

# for i in string_input: 
#     if i.islower(): 
#         count_lower = count_lower + 1 
#     elif i.isupper(): 
#         count_upper = count_upper + 1 
# print(count_lower, count_upper)

# Python Program to Count the Number of Digits and Letters in a String

# string_input=input("Enter a word: ")

# count_digits = 0 
# count_letters = 0 

# for i in string_input: 
#     if i.isdigit(): 
#         count_digits = count_digits + 1 
#     elif i.isalpha(): 
#         count_letters = count_letters + 1 

# print(count_digits,count_letters)

# Python Program to Check if the Substring is Present in the Given String
# string_input=input("Enter a word: ")
# string_input2=input("Enter a word: ")

# def check_strings(string_input,string_input2): 
#     if string_input2 in string_input.lower(): 
#         return True
#     else: 
#         return False

# result = check_strings(string_input,"lah")
# print(result)

# Python Program to Find Common Characters in Two Strings
string_input1=input("Enter a word:")
string_input2=input("Enter a word:")

common_chars = set(string_input1) & set(string_input2)
print(common_chars)


# Python Program to Print All Letters Present in Both Strings

string_input1=input("Enter a word:")
string_input2=input("Enter a word:")

common_chars = set(string_input1) | set(string_input2)
print(common_chars)

# Python Program that Displays which Letters are in First String but not in Second
# Python Program that Displays Letters that are not Common in Two Strings
# Python Program to Create a New String Made up of First and Last 2 Characters
# Python Program to Find the Larger String without using Built-in Functions
# Python Program to Swap the First and the Last Character of a String