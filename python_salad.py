#1 apple is fruit - return this in such a way that it prints fruit is apple 

#2 malayalam - check if this string is palindrome
# def palindrome(given_word): 
#     if given_word[::-1] == given_word:
#         return ("It is Palindrome")
#     else: 
#         return ("It is not Palindrome")

# result = palindrome("malayalam")
# print(result)

# result2 = palindrome("Python")
# print(result2)

#3 numbers = 1234321 - check if the given number is palindrome
# def palindrome(given_numbers): 
#    if given_numbers[::-1] == given_numbers:
#      return ("It is Palindrome")
#    else: 
#      return ("It is not Palindrome")

# result = palindrome("1234321")
# print(result)

# result2 = palindrome("1234325")
# print(result2)


# #4 find those pair of numbers such that their sum is divisible by 2
# numbers_list = [(10,22), (20, -15), (8,8), (1,2)]
# result = [(x,y) for (x,y) in numbers_list if (x + y ) % 2 == 0 ]
# print(result)

# #5 find those pair of numbers such that their sum is divisible by 3
# odd_list = [(10,22), (20, -15), (8,8), (1,2)]
# result = [(x,y) for (x,y) in numbers_list if (x + y ) % 3 == 0 ]
# print(result)

# #6 Use list comprehensions to find the square and cubes of numbers that are 
# # between 10 and 50 and also that are multiples of 3

# import math
# numbers = [ x for x in range(1,51) if x % 3 == 0]
# print(numbers)
# result = [(math.sqrt(x), pow(x,3)) for x in numbers]
# print(result)